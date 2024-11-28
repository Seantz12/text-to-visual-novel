from urllib.parse import urlparse
from parse import Parser
import re
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

# testing
if __name__ == "__main__":
    # ok this library needs us to either parse the title from the wikipedia url, do a search, or give it the exact page title
    print("hello! we need to get the page id from a wikipedia url, or the title somehow but url is probably best!")
    test_page = get_page_from_title('Interactive Fiction')
    sections = test_page.sections
    unnecessary_sections = ['See also', 'Notes', 'References', 'External links', 'Further Reading']
    content_sections = [section for section in sections if section not in unnecessary_sections]
    content_parsers = []
    for section in content_sections:
        content = test_page.section(section)
        # not sure how to treat empty sections, skip or just make them a blank page
        if content:
            parser = Parser()
            parser.parse_text(content)
            content_parsers.append((section, parser))
    for content in content_parsers:
        print(content[0])
        if content[1]:
            print(content[1].parsed)
        # else:
        #     # Just a header, how to deal with this thinking face...
        #     content_parsers.append((section, _))
    # need to parse to get rid of empty sections
