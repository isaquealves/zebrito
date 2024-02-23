FROM python:3.12-slim-bookworm

WORKDIR /app

RUN useradd appuser && chown appuser /app

RUN pip install --upgrade pip && \
    pip install --no-cache-dir poetry

COPY --chown=appuser poetry.lock pyproject.toml README.md /app/

RUN poetry export -f requirements.txt -o requirements.txt && \
    pip uninstall --yes poetry && \
    pip install --require-hashes -r requirements.txt

COPY --chown=appuser . /app

USER appuser

ENTRYPOINT [ "scripts/entrypoint.sh" ]
