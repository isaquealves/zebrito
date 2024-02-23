#!/bin/sh

# Install gatling


GATLING_VERSION=3.10.3
GATLING_REPO_URL=https://repo1.maven.org/maven2/io/gatling/highcharts/gatling-charts-highcharts-bundle

get_sudo() {
    echo "We need superuser permissions, please, inform your sudo passwd (Confia!!)"
    sudo [   2>/dev/null
}

get_sudo;

curl -L $GATLING_REPO_URL/$GATLING_VERSION/gatling-charts-highcharts-bundle-$GATLING_VERSION-bundle.zip > /tmp/gatling-charts-highcharts-bundle-$GATLING_VERSION-bundle.zip

sudo dnf install unzip -y

cd /tmp/

unzip gatling-charts-highcharts-bundle-$GATLING_VERSION-bundle.zip
sudo mv gatling-charts-highcharts-bundle-$GATLING_VERSION /opt/gatling

echo "Now go to the /opt/gatling/bin/ directory and run gatling.sh with 'sudo bash gatling.sh'"