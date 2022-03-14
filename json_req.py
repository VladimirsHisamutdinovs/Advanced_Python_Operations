import json
import requests

def main():
    url = "http://httpbin.org/json"
    res = requests.get(url)

    dataobj = res.json()
    print(json.dumps(dataobj, indent=3))

    print(list(dataobj.keys()))

    print(dataobj['slideshow']['title'])
    
    print(f"Slides number is: {len(dataobj['slideshow']['slides'])}")



if __name__ == "__main__":
    main() 