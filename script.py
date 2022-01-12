import requests


def main():
    print(f"Requests Version: {requests.__version__}")

    result = requests.get("http://www.google.com")
    print(result.status_code)


if __name__ == "__main__":
    main()
