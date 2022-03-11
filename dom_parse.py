from xml import dom
import requests
import xml.dom.minidom


def main():
    url = "http://httpbin.org/xml"
    res = requests.get(url)

    dom_tree = xml.dom.minidom.parseString(res.text)
    root_node = dom_tree.documentElement

    print(f'Root element is {root_node.nodeName}')
    print(f'Title: {root_node.getAttribute("title")}')

    items = dom_tree.getElementsByTagName("item")
    print(f'There are {items.length} item tags')

    new_item = dom_tree.createElement("item")
    new_item.appendChild(dom_tree.createTextNode("BOBABOBABOBA!"))

    first_slide = dom_tree.getElementsByTagName("slide")[0]
    first_slide.appendChild(new_item)

    items = dom_tree.getElementsByTagName("item")
    print(f'There are {items.length} item tags')

if __name__ == "__main__":
    main() 