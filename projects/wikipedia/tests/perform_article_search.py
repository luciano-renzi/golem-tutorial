
description = 'Perform a search for an article, verify that the title is correct'

pages = ['article',
         'home']

def setup(data):
    pass

def test(data):
    navigate(data.env.url)
    send_keys(home.search_input, data.input)
    click(home.search_button)
    verify_text_in_element(article.title, data.title)
    capture('Final result')


def teardown(data):
    pass
