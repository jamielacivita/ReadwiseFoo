import API

class HighlightsList:
    def __init__(self):
        hl = API.HighlistsList()

    def request(self):
        hl.makeRequest()

    def print_results(self):
        print(hl)


def foo():
    return "foo"

def main():
    print("JWTO")

if __name__ == "__main__":
    main()

    #bl = API.BooksList() #create the BooksList API object.
    #bl.set_category("books")
    #bl.makeRequest() # this requests the data and sets it on the self.data property and parses self.data to add attributes to the object.
    #print(bl) # print out to check our results.

    hl = API.HighlistsList()
    hl.makeRequest()
    print(hl.results[1])
    print(hl.results[1].text)





