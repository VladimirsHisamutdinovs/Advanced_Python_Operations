import requests
import xml.sax

class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.slideCount = 0
        self.itemCount = 0
        self.isInTitle = 0

    def startElement(self, tagName, attrs):
        if tagName == "slideshow":
            print("slideshow title: " + attrs['title'])
        elif tagName =='slide':
            self.slideCount += 1
        elif tagName == "item":
            self.itemCount += 1
        elif tagName == "title":
            self.isInTitle = True
    
    def endElement(self, tagName):
        if tagName == "title"    :
            self.isInTitle = False

    def characters(self, chars):
        if self.isInTitle:
            print("Title: " + chars)

    def startDocument(self):
        print("Document Starts!")

    def endDocument(self):
        print("Document Ends!")




def main():
    handler = MyContentHandler()

    url = "http://httpbin.org/xml"
    res = requests.get(url)
    
    xml.sax.parseString(res.text, handler)

    print(f'Slide elements count: {handler.slideCount}')
    print(f'Item elements count: {handler.itemCount}')


if __name__ == "__main__":
    main() 