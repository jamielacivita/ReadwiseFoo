import ast
import schema
import logging

formatString = "%(asctime)s in %(name)s > %(message)s"
fo = logging.Formatter(formatString)
sh = logging.StreamHandler()
sh.setFormatter(fo)
l = logging.getLogger(__name__)
l.setLevel(logging.DEBUG)
l.addHandler(sh)

data = "{'count': 3, 'next': None, 'previous': None, 'results': [{'id': 22367242, 'title': 'Getting Things Done', 'author': 'David Allen', 'category': 'books', 'source': 'reader', 'num_highlights': 6, 'last_highlight_at': '2023-01-13T00:45:51.384089Z', 'updated': '2023-01-13T00:45:51.493070Z', 'cover_image_url': 'https://readwise-assets.s3.amazonaws.com/static/images/article2.74d541386bbf.png', 'highlights_url': 'https://readwise.io/bookreview/22367242', 'source_url': 'https://readwise.io/reader/document_raw_content/20981413', 'asin': None, 'tags': []}, {'id': 22276846, 'title': 'Foundations of Blockchain: Theory and Applications', 'author': 'Ahmed Imteaj', 'category': 'books', 'source': 'reader', 'num_highlights': 11, 'last_highlight_at': '2022-12-21T14:06:35.507244Z', 'updated': '2022-12-21T14:06:35.564903Z', 'cover_image_url': 'https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/19925773/Aimages_978-3-030-75025-1_CoverFigure-978-3-030-7_Z33W8cy.jpg', 'highlights_url': 'https://readwise.io/bookreview/22276846', 'source_url': 'https://readwise.io/reader/document_raw_content/19925773', 'asin': None, 'tags': []}, {'id': 21983998, 'title': 'Whole Earth: The Many Lives of Stewart Brand', 'author': 'John Markoff', 'category': 'books', 'source': 'reader', 'num_highlights': 42, 'last_highlight_at': '2022-12-16T19:50:36.081969Z', 'updated': '2022-12-16T19:50:36.177703Z', 'cover_image_url': 'https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/16925529/cover-image-9780735223950_cover_BnTh760.jpg', 'highlights_url': 'https://readwise.io/bookreview/21983998', 'source_url': 'https://readwise.io/reader/document_raw_content/16925529', 'asin': None, 'tags': []}]}"
data_dict = ast.literal_eval(data)

def print_data():
    print(data)

def print_count():
    print(data_dict["count"])
    print(len(data_dict["results"]))
    print(data_dict["results"][1])

def get_first_result_object(results_index = 1, data_dict=data_dict):
    r = schema.Result()
    r.id = data_dict["results"][results_index]["id"]
    r.title = data_dict["results"][results_index]["title"]
    r.author = data_dict["results"][results_index]["author"]
    r.category = data_dict["results"][results_index]["category"]
    r.source  = data_dict["results"][results_index]["source"]
    r.num_highlights  = data_dict["results"][results_index]["num_highlights"]
    r.last_highlight_at = data_dict["results"][results_index]["last_highlight_at"]
    r.cover_image_url = data_dict["results"][results_index]["cover_image_url"]
    r.highlights_url = data_dict["results"][results_index]["highlights_url"]
    r.source_url = data_dict["results"][results_index]["source_url"]
    r.updated = data_dict["results"][results_index]["updated"]

    return r

def results_object(data_dict=data_dict):
    results_lst = []
    for result in data_dict["results"]:
        r = schema.Result()
        r.id = result["id"]
        r.title = result["title"]
        r.author = result["author"]
        r.category = result["category"]
        r.cover_image_url = result["cover_image_url"]
        r.highlights_url = result["highlights_url"]
        r.last_highlight_at =  result["last_highlight_at"]
        r.num_highlights = result["num_highlights"]
        r.source_url = result["source_url"]
        r.updated = result["updated"]

        results_lst.append(r)
    return results_lst


def results_object_highlights(data_dict=data_dict):
    l.debug("In results object highlights")
    results_lst = []
    for result in data_dict["results"]:
        l.debug("Result: ")
        l.debug(result)
        r = schema.Result_Highlight()

        r.book_id = result["book_id"]
        r.color = result["color"]
        r.highlighted_at = result["highlighted_at"]
        r.id = result["id"]
        r.location = result["location"]
        r.note = result["note"]
        r.tags =  result["tags"]
        r.text = result["text"]
        r.updated = result["updated"]
        r.url = result["url"]

        results_lst.append(r)
    return results_lst