cd /build

apk add yarn

mkdir /test-results
export JEST_JUNIT_OUTPUT_DIR=/test-results
export JEST_JUNIT_OUTPUT_NAME=results.xml

yarn install

yarn lint -o /test-results/lint.xml -f junit

yarn unittest
