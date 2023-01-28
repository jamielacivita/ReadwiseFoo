import requests
import os
import logging
import parse
import datetime

formatString = "%(asctime)s in %(name)s > %(message)s"
fo = logging.Formatter(formatString)
sh = logging.StreamHandler()
sh.setFormatter(fo)
l = logging.getLogger(__name__)
l.setLevel(logging.DEBUG)
l.addHandler(sh)

class auth:
    def __init__(self):
        pass

    def auth(self):
        """
        utilty to test auth token
        :param token: readwise token
        :return: true if authenticaiton sucessful, false otherwise
        """
        token = os.getenv('ReadwiseToken')
        l.debug(f"API Token From Enviroment Variable: {token}")
        r = requests.post(
            url="https://readwise.io/api/v2/highlights/",
            headers={"Authorization": f"Token {token}"})

        status_code = r.status_code
        l.debug(f"Status Code : {status_code}")

        # Evaulate Status Code
        if status_code == 401:
            return False
        else:
            return True


class BooksList:
    def __init__(self):
        self.token = os.getenv('ReadwiseToken')
        self.data = None
        self.results = [] # a list of results objects.

        #query paramaters
        self.page_size = None
        self.page = None
        self.category = None
        self.source = None
        self.num_highlights = None
        self.num_highlights__lt = None
        self.num_highlights__gt = None
        self.updated__lt = None
        self.updated__gt = None
        self.last_highlight_at__lt = None
        self.last_highlight_at__gt = None

        l.debug(f"self.token: {self.token}")
        return None

    def set_category(self, category):
        self.category = category
        return None

    def __str__(self):
        for r in self.results:
            print(r)
        return "\n"

    def set_page_size(self,ps):
        self.page_size = ps
        return None

    def makeRequest(self):
        # getting highlights from a particular book
        # made after February 1st, 2020, 21:35:53 UTC
        querystring = {
            "category":self.category
        }

        response = requests.get(
            url="https://readwise.io/api/v2/books/",
            headers={"Authorization": f"Token {self.token}"},
            params=querystring
        )

        self.data = response.json()
        #l.debug(self.data)
        self.add_results()

        return None

    def add_results(self):
        self.results = parse.results_object(self.data)
        l.debug(f"number of results objects made {len(self.results)}")

class HighlistsList:
    def __init__(self):
        self.token = os.getenv('ReadwiseToken')
        self.data = None
        self.results = []

        #paramaters for search
        self.page_size = None
        self.page = None
        self.book_id = None
        self.updated__lt = None
        self.updated__gt = None
        self.highlighted_at__lt = None
        self.highlighted_at__gt = None

        l.debug(f"self.token: {self.token}")
        return None

    def __str__(self):
        print(f"token : {self.token}")
        print(f"data : {self.data}")
        print(f"results : {self.results}")

        print(f"page_size : {self.page_size}")
        print(f"page : {self.page}")
        print(f"book id : {self.book_id}")
        print(f"updated__lt : {self.updated__lt}")
        print(f"updated_gt : {self.updated__gt}")
        print(f"highlighted_at__lt : {self.highlighted_at__lt}")
        print(f"highlighted_at__gt : {self.highlighted_at__gt}")
        return "\n"

    def makeRequest(self):
        querystring = {
            #"category":self.category,
            "highlighted_at__lt":self.highlighted_at__lt,
            "highlighted_at__gt":self.highlighted_at__gt
        }

        response = requests.get(
            url="https://readwise.io/api/v2/highlights/",
            headers={"Authorization": f"Token {self.token}"},
            params=querystring
        )

        self.data = response.json()
        l.info("response data: ")
        l.info(self.data)

        self.add_results()

        return None

    def add_results(self):
        self.results = parse.results_object_highlights(self.data)
        l.debug(f"number of results objects made {len(self.results)}")

    def set_highlighted_at__lt(self, dateTime):
        self.highlighted_at__lt = dateTime
        return None

    def set_highlighted_at__gt(self, dateTime):
        self.highlighted_at__gt = dateTime
        return None


    def set_highlighted_before(self,year,month,day,hour,min,sec):
        self.set_highlighted_at__lt(datetime.datetime(year,month,day,hour,min,sec,0).isoformat())


    def set_highlighted_after(self,year,month,day,hour,min,sec):
        self.set_highlighted_at__gt(datetime.datetime(year,month,day,hour,min,sec,0).isoformat())


    def highlightedDaysAgo(self,daysAgo):
        dt = datetime.datetime.utcnow() - datetime.timedelta(days=daysAgo)
        self.set_highlighted_at__gt(dt)


    def print_results_simple(self):
        for r in self.results:
            r.print_simple()

    def print_results_simple_delta(self):
        for r in self.results:
            r.print_simple_delta()