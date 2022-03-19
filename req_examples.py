import requests

def main():
    # url = 'http://httpbin.org/xml'
    # res = requests.get(url)
    # print_results(res)

    # url_post = 'http://httpbin.org/post'
    # data_vals = {
    #     'key1': 'Ave',
    #     'key2': 'Coder'
    # }

    # #get_res = requests.get(url_get, params=data_vals)
    # post_res = requests.post(url_post, data=data_vals)
    # print_results(post_res)


    url_get = 'http://httpbin.org/get'
    header_vals = {
        'author': 'Ave Coder'
                   }

    get_res = requests.get(url_get, headers=header_vals)
    
    print_results(get_res)


def print_results(res):
    print(f'Result: {res.status_code}')
    print(f'Headers: {res.headers}')
    print(f'Data: {res.text}')




if __name__ == "__main__":
    main()
