import os
import requests

# Constants
NGINX_HOST = os.getenv("NGINX_HOST", "localhost")
RESULTS_DIR = os.getenv("RESULTS_DIR", "./test-results")
LOGS_DIR = f'{RESULTS_DIR}/logs/'
ARTIFACT_DIR = f'{RESULTS_DIR}/artifacts/'
PORT_8080 = 8080
PORT_9090 = 9090
EXPECTED_STATUS_8080 = 200
EXPECTED_CONTENT_8080 = "Custom HTML Response"
EXPECTED_STATUS_9090 = 503
SUCCESS_FILE = "succeeded"
FAIL_FILE = "fail"
LOG_FILE = "test_log.txt"


# Helper function to write results
def write_result(path, filename, content):
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join(path, filename)
    with open(filepath, "w") as f:
        f.write(content)


def test_server():
    try:
        # Test port 8080 for custom HTML response
        url_8080 = f"http://{NGINX_HOST}:{PORT_8080}"
        response_8080 = requests.get(url_8080)
        assert response_8080.status_code == EXPECTED_STATUS_8080, f"Unexpected status code {response_8080.status_code} on {url_8080}"
        assert EXPECTED_CONTENT_8080 in response_8080.text, "Custom HTML not found in response"

        # Test port 9090 for HTTP error
        url_9090 = f"http://{NGINX_HOST}:{PORT_9090}"
        response_9090 = requests.get(url_9090)
        assert response_9090.status_code == EXPECTED_STATUS_9090, f"Unexpected status code {response_9090.status_code} on {url_9090}"

        # Write success
        write_result(ARTIFACT_DIR, SUCCESS_FILE, "Tests passed successfully.\n")
        write_result(LOGS_DIR, LOG_FILE, f"Port 8080 and 9090 tests passed.\n")
    except Exception as e:
        # Write failure
        write_result(ARTIFACT_DIR, FAIL_FILE, "Tests failed.\n")
        write_result(LOGS_DIR, LOG_FILE, f"Error occurred: {str(e)}\n")


if __name__ == "__main__":
    test_server()
    print('Test script finished')
