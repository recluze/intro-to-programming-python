try:
    from a06 import output_prime_factors, get_nth_prime
except ImportError:
    pass




def test_output_prime_factors_4():
    v, out = capture_output(output_prime_factors)(499)
    assert out == '\n'.join([str(x) for x in [499]]) + "\n"

def test_output_prime_factors_5():
    v, out = capture_output(output_prime_factors)(9987)
    assert out == '\n'.join([str(x) for x in [3, 3329]]) + "\n"


def test_output_prime_factors_6():
    v, out = capture_output(output_prime_factors)(82465.6)
    assert out == '\n'.join([str(x) for x in [2, 41233]]) + "\n"

def test_output_prime_factors_7():
    v, out = capture_output(output_prime_factors)(82465.1)
    assert out == '\n'.join([str(x) for x in [5, 16493]]) + "\n"


def test_get_nth_prime_4():
    out = get_nth_prime(20)
    assert out == 71

def test_get_nth_prime_5():
    out = get_nth_prime(19.3)
    assert out == None

def test_get_nth_prime_6():
    out = get_nth_prime(89)
    assert out == 461


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
