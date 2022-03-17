import requests
from requests.auth import HTTPBasicAuth

def main():
    url = "http://httpbin.org/basic-auth/AveCoder/AvePassword"
    creds = HTTPBasicAuth("AveCoder","AvePassword")
    res = requests.get(url, auth=creds)
    print_results(res)


def print_results(res):
    print(f'Result: {res.status_code}')
    print(f'Data: {res.text}')



if __name__ == "__main__":
    main()