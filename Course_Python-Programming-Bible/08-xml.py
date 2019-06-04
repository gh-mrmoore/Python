import xml.sax

class XMLhandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.model = ""
        self.seats = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "car":
            print("---Car---")
            name = attributes["name"]
            print("Name: ", name)
    def endElement(self, tag):
        if self.CurrentData == "model":
            print("Model:", self.model)
        elif self.CurrentData == "seats":
            print("Seats:", self.seats)

        self.CurrentData = ""
        
    def characters(self, content):
        if self.CurrentData == "model":
            self.model = content
        elif self.CurrentData == "seats":
            self.seats = content

if(__name__ == "__main__"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    Handler = XMLhandler()
    parser.setContentHandler(Handler)

    parser.parse("vehicles.xml")