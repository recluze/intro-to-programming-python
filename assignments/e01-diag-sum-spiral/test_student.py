try:
    from e01 import get_diag_sum
except ImportError:
    pass


def test_get_diag_sum_1():
    v = 0
    assert get_diag_sum(v) == None


def test_get_diag_sum_2():
    v = [2, 4, 6, 8, 10, 1090]
    for i in v:
        assert get_diag_sum(i) == None


def test_get_diag_sum_3():
    v = 5
    assert get_diag_sum(v) == 101


def test_get_diag_sum_4():
    v = 15
    assert get_diag_sum(v) == 2381


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
