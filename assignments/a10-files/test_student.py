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



def test_line_count_s_1():
    assert line_count('.', 'essay.txt') == 32


def test_line_count_s_3():
    assert line_count('.', 'essay.txt', True) == 20

def test_line_count_s_2():
    try:
        line_count('.', 'missing.txt') == 32
        assert False, "How are you reading a missing file?"
    except IOError:
        pass

def test_character_count_s_1():
    assert character_count('.', 'essay.txt') == 2632


def test_character_count_s_2():
    assert character_count('.', 'essay.txt', True) == 2178



def test_move_lines_s_1():
    move_lines('essay.txt', 'out.txt', 3)
    with open('out.txt', 'r') as f:
        assert f.read() == """Write a title that summarizes the specific problem\n\nThe title is the first thing potential answerers will see."""

def test_move_lines_s_2():
    move_lines('essay.txt', 'out.txt', 1)
    with open('out.txt', 'r') as f:
        assert f.read() == """Write a title that summarizes the specific problem"""


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
