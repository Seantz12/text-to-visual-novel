from urllib.parse import urlparse
from parse import Parser
import wikipedia


def get_page_from_title(title):
    # gonna have to do some error looooppppinnngggg
    return wikipedia.page(title)

def get_page_from_url(url):
    path = urlparse(url).path
    page_title = path.split('/')[-1]
    return get_page_from_title(page_title) 
    
def get_page_from_search(search_term):
    pass

def search_page(query):
    search_results = wikipedia.search(query)
    # need to display results to user and then have a way for user to input selection
    input = 0
    return get_page_from_title(search_results[input])

def parse_text(content):
    # main thing here is that we need to find a way to remove the references section at the end... probably... or maybe it doesn't matter?
    pass

# testing
if __name__ == "__main__":
    # ok this library needs us to either parse the title from the wikipedia url, do a search, or give it the exact page title
    print("hello! we need to get the page id from a wikipedia url, or the title somehow but url is probably best!")
    # we're gonna have to do some preparsing, notably remove header lines probably? or treat them specially probably
    parser = Parser()
    test_page = get_page_from_title('Visual Novel')
    parser.parse_text(test_page.content)
    print(parser.parsed)
    print(parser.raw)
