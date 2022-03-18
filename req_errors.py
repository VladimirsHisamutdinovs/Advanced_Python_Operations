import requests
from requests import HTTPError, Timeout

def main():
    try:
        #url = "http://httpbin.org/status/404"
        url = "http://httpbin.org/delay/5"
        res = requests.get(url, timeout=2)
        res.raise_for_status()
        print_results(res)
    except HTTPError as err:
        print(f"Error: {err}")
    except Timeout as err:
        print(f'Request timed out: {err}')



def print_results(res):
    print(f'Result: {res.status_code}')
    print(f'Data: {res.text}')



if __name__ == "__main__":
    main()