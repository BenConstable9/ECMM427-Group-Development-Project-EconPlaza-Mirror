# Install Test Requirements

pip install -r ../requirements-test.txt

mkdir /test-results

export TEST_OUTPUT_DIR=/test-results
export TEST_OUTPUT_FILE_NAME=results.xml
export DEVELOPMENT=True

python manage.py run test
