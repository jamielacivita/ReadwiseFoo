import API
import schema as sfoo



class HighlightsList:
    def __init__(self):
        hl = API.HighlistsList()

    def request(self):
        hl.makeRequest()

    def print_results(self):
        print(hl)


def foo():
    return "foo"

def test():
    #create a blank highlights list object.
    hl = API.HighlistsList()
    #hl.set_highlighted_at__gt("2023-01-15T00:00:00.0Z")
    #hl.set_highlighted_before(2023,1,14,0,0,0)
    #set a paramater for the request
    hl.set_highlighted_after(2023,1,15,0,0,0)
    #hl.highlightedDaysAgo()
    #peform the request - this will populate the object.
    hl.makeRequest()
    #print out the results.
    #hl.print_results_simple()
    hl.print_results_simple_delta()


def test_time():
    sfoo.calculate_time_delta()

def main():
    print("running Highlights list")

if __name__ == "__main__":
    test()
    #test_time()

    #bl = API.BooksList() #create the BooksList API object.
    #bl.set_category("books")
    #bl.makeRequest() # this requests the data and sets it on the self.data property and parses self.data to add attributes to the object.
    #print(bl) # print out to check our results.







