# Set script to exit on command error
set -e

# Install Test Requirements

pip install -r ../requirements-test.txt

mkdir /test-results

export TEST_OUTPUT_DIR=/test-results
export TEST_OUTPUT_FILE_NAME=results.xml
export DEVELOPMENT=True

# Run tests and generate coverage reports
coverage run --source='.' manage.py test
coverage report
coverage xml -o $TEST_OUTPUT_DIR/coverage.xml

black . --check
