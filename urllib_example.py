import urllib.request
import urllib.parse



def main():
    url = "http://httpbin.org/xml"
    url_get = "http://httpbin.org/get"
    url_post = "http://httpbin.org/post"

    args = {
        "name": "Ave Coder",
        "is_author": True
    }

    data = urllib.parse.urlencode(args)

    res = urllib.request.urlopen(url_get + "?" + data)

    d_enc = data.encode()
    post_res = urllib.request.urlopen(url_post, data=d_enc)

    print(f'Status: {post_res.status}')
    print(post_res.read().decode("utf-8"))
    # print(f'Headers: {res.getheaders()}')
    # print(f'Data: {res.read()}')
    

    # with urllib.request.urlopen('http://httpbin.org/xml') as f:
    #     print(f'Status: {res.status}')

    




if __name__ == "__main__":
    main()
