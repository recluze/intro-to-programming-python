try:
    from e01 import get_diag_sum
except ImportError:
    pass


def test_get_diag_sum_5():
    v = 0
    assert get_diag_sum(v) == None


def test_get_diag_sum_6():
    v = [18, 46, 86, 80, 158, 1490]
    for i in v:
        assert get_diag_sum(i) == None


def test_get_diag_sum_7():
    v = 25
    assert get_diag_sum(v) == 10761


def test_get_diag_sum_8():
    v = 159
    assert get_diag_sum(v) == 2692637


def test_get_diag_sum_9():
    v = 1001
    assert get_diag_sum(v) == 669171001


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
