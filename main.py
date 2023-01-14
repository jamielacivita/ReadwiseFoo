import API
import parse

def main():
    print("JWTO")

if __name__ == "__main__":

    bl = API.BooksList() #create the BooksList API object.
    bl.makeRequest() # this requests the data and sets it on the self.data property and parses self.data to add attributes to the object.
    print(bl) # print out to check our results.




