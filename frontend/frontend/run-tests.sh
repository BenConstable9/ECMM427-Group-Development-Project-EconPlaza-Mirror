cd /build

mkdir /test-results
export JEST_JUNIT_OUTPUT_DIR=/test-results
export JEST_JUNIT_OUTPUT_NAME=results.xml

yarn install

yarn test
