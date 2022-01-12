import requests


def main():
    print(f"Requests Version: {requests.__version__}")

    google_result = requests.get("http://www.google.com")
    print(f"\nRequest to http://www.google.com returned code {google_result.status_code}")

    result = requests.get("https://raw.githubusercontent.com/JoshuaBillson/CMPUT-404-Assignment-1/main/script.py")

    print(f"\n{result.text}")


if __name__ == "__main__":
    main()
