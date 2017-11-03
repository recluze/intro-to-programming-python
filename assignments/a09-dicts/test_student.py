try:
    from a09 import get_types
except ImportError:
    pass


try:
    from a09 import get_types_counts
except ImportError:
    pass

try:
    from a09 import get_author_count
except ImportError:
    pass



d_1 = {
        "articles": [{
            "slug": "how-to-train-your-mule",
            "title": "How to train your mule",
            "description": "Ever wonder how?",
            "body": "It takes a Jacobian",
            "tagList": ["mules", "training"],
            "createdAt": "2016-02-18T03:22:56.637Z",
            "updatedAt": "2016-02-18T03:48:35.824Z",
            "favoritesCount": 0,
            "author": {
              "username": "jake",
              "bio": "I work at statefarm",
              "following": False
            }
        }, {
            "slug": "and another article",
            "body": "I'm getting bored",
            "tagList": ["bored", "article"],
            "createdAt": "2016-02-18T03:22:56.637Z",
            "updatedAt": "2016-02-18T03:48:35.824Z",
            "favoritesCount": 20,
            "author": {
              "username": "cap",
              "following": True
            }
        }],
        "tweets": [{
            "body": "See my article on training mules.",
            "author": {
              "username": "jake"
            }
        }]
    }

d_2 = {
        "articles": [{
            "slug": "how-to-train-your-mule",
            "title": "How to train your mule",
            "description": "Ever wonder how?",
            "body": "It takes a Jacobian",
            "tagList": ["mules", "training"],
            "createdAt": "2016-02-18T03:22:56.637Z",
            "updatedAt": "2016-02-18T03:48:35.824Z",
            "favoritesCount": 0,
            "author": {
              "username": "jake",
              "bio": "I work at statefarm",
              "following": False
            }
        }],
        "books": [{
            "body": "See my article on training mules.",
            "author": {
              "username": "jake"
            }
        }],
        "papers": []
    }

def test_get_types_s_1():
    ret_val = get_types(d_1)
    for i in ['tweets', 'articles']:
        assert i in ret_val
    assert len(ret_val) == 2

def test_get_types_s_2():
    ret_val = get_types({})
    assert ret_val == []

def test_get_types_s_3():
    ret_val = get_types(d_2)
    for i in ['books', 'articles', 'papers']:
        assert i in ret_val
    assert len(ret_val) == 3

def test_get_types_counts_s_1():
    ret_val = get_types_counts(d_1)
    assert len(ret_val) == 2
    assert ret_val['articles'] == 2
    assert ret_val['tweets'] == 1


def test_get_types_counts_s_2():
    ret_val = get_types_counts(d_2)
    assert len(ret_val) == 3
    assert ret_val['articles'] == 1
    assert ret_val['books'] == 1
    assert ret_val['papers'] == 0

def test_get_types_counts_s_3():
    ret_val = get_types_counts({})
    assert len(ret_val) == 0

def test_get_author_count_s_1():
    ret_val = get_author_count(d_1, 'jake')
    assert ret_val == 2

def test_get_author_count_s_2():
    ret_val = get_author_count(d_1, 'cap')
    assert ret_val == 1


def test_get_author_count_s_3():
    ret_val = get_author_count({}, 'whoever')
    assert ret_val == 0

def test_get_author_count_s_4():
    ret_val = get_author_count({}, 'missing')
    assert ret_val == 0

def test_get_author_count_s_5():
    ret_val = get_author_count(d_2, 'cap')
    assert ret_val == 0



# output capturing decorator
def capture_output(fn):
    def wrapper(*args, **kwargs):
        import StringIO
        import sys
        orig_stdout = sys.stdout
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput

        v = fn(*args, **kwargs)

        sys.stdout = orig_stdout # don't rely on __stdout__

        # print 'Captured', capturedOutput.getvalue()
        output_val = capturedOutput.getvalue()
        return v, output_val

    return wrapper
