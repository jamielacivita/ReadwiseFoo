import datetime

class Result:
    def __init__(self):
        self.asin = None
        self.author = None
        self.category = None
        self.cover_image_url = None
        self.highlights_url = None
        self.id = None
        self.last_highlight_at = None
        self.num_highlights = None
        self.source = None
        self.source_url = None
        self.tags = []
        self.title = None
        self.updated = None

    def __str__(self):
        print(f"id : {self.id}")
        print(f"title : {self.title}")
        print(f"author : {self.author}")
        print(f"category : {self.category}")
        print(f"cover image URL : {self.cover_image_url}")
        print(f"highlights URL : {self.highlights_url}")
        print(f"last highlight at : {self.last_highlight_at}")
        print(f"number of highlights : {self.num_highlights}")
        print(f"source URL : {self.source_url}")
        print(f"updated : {self.updated}")
        return("\n")


    def set_id(self, id):
        self.id = id
        return None

    def get_id(self):
        return self.id

    def set_title(self, title):
        self.title = title
        return None

    def get_title(self):
        return self.title


class Result_Highlight:
    def __init__(self):
        self.book_id = None
        self.color = None
        self.highlighted_at = None
        self.id = None
        self.location = None
        self.location_type = None
        self.note = None
        self.tags = None
        self.text = None
        self.updated = None
        self.url = None

    def __str__(self):
        print(f"book_id : {self.book_id}")
        print(f"color : {self.color}")
        print(f"highlighted_at : {self.highlighted_at}")
        print(f"id : {self.id}")
        print(f"location : {self.location}")
        print(f"location_type : {self.location_type}")
        print(f"note : {self.note}")
        print(f"tags : {self.tags}")
        print(f"text : {self.text}")
        print(f"updated : {self.updated}")
        print(f"url : {self.url}")
        return("\n")

    def print_simple(self):
        print(f"{self.highlighted_at} : {self.text} ({self.note})\n")
        return("\n")

    def print_simple_delta(self):
        print(f"{calculate_time_delta(self.highlighted_at)} : {self.text} ({self.note})\n")
        return("\n")

## Helper Function Go Here

def calculate_time_delta(input_time="2023-01-23T21:40:22.320832Z"):
    """

    :param input_time: A time string in the format 2023-01-23T21:40:22.320832Z
    :return: A time delta like 4 days, 20:45:53.472612
    """
    print("In calculate time delta.")
    #we need to remove the trailing Z from the timestamp becasue the datetime function wont parse it correctly with it.
    input_time = input_time.split("Z")[0]
    d = datetime.datetime.fromisoformat(input_time)
    #d is a datetime.datetime object.
    n = datetime.datetime.utcnow()
    delta = n-d
    return delta

