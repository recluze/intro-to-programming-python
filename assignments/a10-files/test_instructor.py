try:
    from a10 import line_count
except ImportError:
    pass


try:
    from a10 import character_count
except ImportError:
    pass

try:
    from a10 import move_lines
except ImportError:
    pass


input_file = "dummyfile.txt"

def setup_module(module):
    with open(input_file, 'w') as f:
        f.write("""This is a test file and \nhas some very interesting bits\nOf course, the students never see this file\n so we can put whatever we want to put in it.\n\nAnd more...  """)

def test_line_count_i_1():
    assert line_count('.', input_file, True) == 5


def test_line_count_i_2():
    try:
        line_count('.', 'missing.txt', True) == 32
        assert False, "How are you reading a missing file?"
    except IOError:
        pass

def test_character_count_i_1():
    assert character_count('.', input_file) == 160


def test_character_count_i_2():
    assert character_count('.', input_file, True) == 124



def test_move_lines_i_1():
    move_lines(input_file, 'out-i.txt', 3)
    with open('out-i.txt', 'r') as f:
        assert f.read() == """This is a test file and \nhas some very interesting bits\nOf course, the students never see this file"""

def test_move_lines_i_2():
    move_lines(input_file, 'out-i.txt', 1)
    with open('out-i.txt', 'r') as f:
        assert f.read() == """This is a test file and """


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
