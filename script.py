import requests


def main():
    result = requests.get("https://raw.githubusercontent.com/JoshuaBillson/CMPUT-404-Assignment-1/main/script.py")
    print(result.text)


if __name__ == "__main__":
    main()
