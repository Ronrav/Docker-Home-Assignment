import os
import requests
from http import HTTPStatus
from bs4 import BeautifulSoup

# constant variables set from config.json
NGINX_HOST = os.getenv('NGINX_HOST', 'nginx')
SERVER_PORT_HTML = os.getenv('SERVER_PORT_HTML', '8080')
SERVER_PORT_ERROR = os.getenv('SERVER_PORT_ERROR', '9090')
HTML_FILE_PATH = os.getenv('HTML_FILE_PATH', '/shared/index.html')
RESULTS_DIR = os.getenv('RESULTS_DIR', 'results')
SUCCESS_FILE_NAME = os.getenv('SUCCESS_FILE_NAME', 'succeeded')
FAIL_FILE_NAME = os.getenv('FAIL_FILE_NAME', 'fail')
SHARED_DIR = os.getenv('SHARED_DIR', 'shared')
HTML_URL = f"http://{NGINX_HOST}:{SERVER_PORT_HTML}"
HTTP_ERROR_URL = f"http://{NGINX_HOST}:{SERVER_PORT_ERROR}"


def test_html_server():
    """Test the HTML server on SERVER_PORT_HTML by verifying the response matches a given file"""

    # Read the expected HTML content from the specified file
    if not os.path.exists(HTML_FILE_PATH):
        raise FileNotFoundError(f"HTML file not found at {HTML_FILE_PATH}")

    with open(HTML_FILE_PATH, "r") as file:
        expected_content = file.read()

    # Make the HTTP request
    response = requests.get(HTML_URL)
    if response.status_code != HTTPStatus.OK:
        raise ValueError(
            f"HTML server test failed on port {SERVER_PORT_HTML}: "
            f"Expected {HTTPStatus.OK}, got {response.status_code}"
        )

    # Compare the response content with the expected content

    received_html = BeautifulSoup(response.text, "html.parser")
    expected_html = BeautifulSoup(expected_content, "html.parser")
    if received_html != expected_html:
        raise ValueError(
            f"HTML server content test failed on port {SERVER_PORT_HTML}: "
            f"The response content does not match the expected HTML file content. received:\n{response.text}\nexpected:\n{expected_content}"
        )


def test_error_server():
    """Test the error server on SERVER_PORT_ERROR"""

    response = requests.get(HTTP_ERROR_URL)
    if response.status_code != HTTPStatus.SERVICE_UNAVAILABLE:
        raise ValueError(
            f"Error server test failed on port {SERVER_PORT_ERROR}: "
            f"Expected {HTTPStatus.SERVICE_UNAVAILABLE}, got {response.status_code}"
        )


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)

    try:
        test_html_server()
        test_error_server()

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
    print('Testing Start')
    main()
    print('Finished Testing')
