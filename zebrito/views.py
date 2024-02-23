import json
from typing import Annotated, Any, Dict
from fastapi import Depends, Path, Request, routing
from fastapi.responses import JSONResponse
from contextlib import suppress

from pydantic import ValidationError
from zebrito.schemas import Transaction

router = routing.APIRouter(prefix="/clientes")

@router.get(path="/{client_id}/extrato")
async def export_acc_statement(request: Request, client_id: int|None = Annotated[int, Path(title="The client id who is requesting the statement")]) -> JSONResponse:
    if client_id:
        if client_id not in range(1,6):
            return JSONResponse(f"Client #{client_id} not found", status_code=404)
        async with request.app.state.db_pool.acquire() as connection:
                acc_statement = await connection.fetchrow("SELECT * from account_statement where client_id=$1", client_id)
                return JSONResponse(json.loads(acc_statement["acc_statement"])[0], status_code=200)
    return JSONResponse(f"Client not provided", status_code=404)


@router.post(path="/{client_id}/transacoes")
async def register_transaction(request: Request, client_id:int|None = Annotated[int, Path(title="The client id who is requesting the statement")]):
    if client_id:
        if client_id not in range(1,6):
            return JSONResponse(f"Client {client_id} not found", status_code=404)
        try:
            transaction = Transaction(**(await request.json()))
        except ValidationError:
            return JSONResponse({"detail":"Invalid operation"}, status_code=422)

        async with request.app.state.db_pool.acquire() as connection, connection.transaction():
            try:
                result = await connection.fetchrow("SELECT * from apply_operation_and_update_balance($1, $2, $3, $4)", client_id, transaction.nature, transaction.total, transaction.description)
            except Exception:
                return JSONResponse(content={"message": "Invalid operation"}, status_code=422)
            return JSONResponse(content={
                "saldo": result.get("balance", 0),
                "limite": result.get("limit", 0),
            }, status_code=200)
    return JSONResponse(f"Client not provided", status_code=404)