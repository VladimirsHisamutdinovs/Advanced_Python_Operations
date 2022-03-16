import requests
from lxml import etree

def main():
    url = "http://httpbin.org/xml"
    res = requests.get(url)

    doc = etree.fromstring(res.content)
    # print(res.text)

    # print(doc.tag)
    # print(doc.attrib['title'])

    # for el in doc.findall("slide"):
    #     print(el.tag)

    new_slide = etree.SubElement(doc, "slide")
    new_slide.text = "This is a new slide!"

    slide_count = len(doc.findall("slide"))
    item_count = len(doc.findall(".//item"))

    print(f'Number of slide elems: {slide_count}')
    print(f'Number of item elems: {item_count}')

if __name__ == "__main__":
    main() 