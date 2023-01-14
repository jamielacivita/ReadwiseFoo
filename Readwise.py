import API
import parse

def foo():
    return "foo"

def main():
    print("JWTO")

if __name__ == "__main__":

    #bl = API.BooksList() #create the BooksList API object.
    #bl.set_category("books")
    #bl.makeRequest() # this requests the data and sets it on the self.data property and parses self.data to add attributes to the object.
    #print(bl) # print out to check our results.

    hl = API.HighlistsList()
    hl.makeRequest()
    print(hl.results[1])
    print(hl.results[1].text)





