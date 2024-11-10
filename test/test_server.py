import os
import requests

# Constants
NGINX_HOST = "nginx"
PORT_8080 = 8080
PORT_9090 = 9090
EXPECTED_STATUS_8080 = 200
EXPECTED_CONTENT_8080 = "Custom HTML Response"
EXPECTED_STATUS_9090 = 503
RESULTS_DIR = "/test-results"
SUCCESS_FILE_NAME = "succeeded"
FAIL_FILE_NAME = "fail"

def test_nginx():
    os.makedirs(RESULTS_DIR, exist_ok=True)

    try:
        # Test port 8080
        url_8080 = f"http://{NGINX_HOST}:{PORT_8080}"
        response_8080 = requests.get(url_8080)
        if response_8080.status_code != EXPECTED_STATUS_8080:
            raise ValueError(f"Port {PORT_8080} test failed: Expected {EXPECTED_STATUS_8080}, got {response_8080.status_code}")
        if EXPECTED_CONTENT_8080 not in response_8080.text:
            raise ValueError(f"Port {PORT_8080} content test failed: Expected '{EXPECTED_CONTENT_8080}' in response.")

        # Test port 9090
        url_9090 = f"http://{NGINX_HOST}:{PORT_9090}"
        response_9090 = requests.get(url_9090)
        if response_9090.status_code != EXPECTED_STATUS_9090:
            raise ValueError(f"Port {PORT_9090} test failed: Expected {EXPECTED_STATUS_9090}, got {response_9090.status_code}")

        # If all tests pass
        with open(f"{RESULTS_DIR}/{SUCCESS_FILE_NAME}", "w") as success_file:
            success_file.write("All tests passed successfully.")
        print("All tests passed successfully.")

    except Exception as e:
        with open(f"{RESULTS_DIR}/{FAIL_FILE_NAME}", "w") as fail_file:
            fail_file.write(str(e))
        print(f"Test failed: {e}")
        exit(1)

if __name__ == "__main__":
    test_nginx()
