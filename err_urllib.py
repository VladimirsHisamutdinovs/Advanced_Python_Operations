import urllib.request
from http import HTTPStatus
from urllib.error import HTTPError, URLError


def main():
    #url = "http://httpbin.org/html"
    #url = "http://httpbin.org/status/404"
    url = "http://no-such-server.org"

    try:
        with urllib.request.urlopen(url) as f:
            print(f'Status: {f.status}')
            if (f.getcode() == HTTPStatus.OK):
                print(f.read().decode('utf-8'))
    except HTTPError as err:
        print(f"Error: {err.code}")
    except URLError as err:
        print(f'URL doesn\'t exist {err.reason}')


if __name__ == "__main__":
    main()