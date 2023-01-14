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

    def get_titel(self):
        return self.title

