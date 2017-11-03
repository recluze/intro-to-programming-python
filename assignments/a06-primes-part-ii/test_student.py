try:
    from a06 import output_prime_factors, get_nth_prime
except ImportError:
    pass




def test_output_prime_factors_1():
    v, out = capture_output(output_prime_factors)(23)
    assert out == '\n'.join([str(x) for x in [23]]) + "\n"

def test_output_prime_factors_2():
    v, out = capture_output(output_prime_factors)(230)
    assert out == '\n'.join([str(x) for x in [2, 5, 23]]) + "\n"


def test_output_prime_factors_3():
    v, out = capture_output(output_prime_factors)(230.6)
    assert out == '\n'.join([str(x) for x in [3, 7, 11]]) + "\n"


def test_get_nth_prime_1():
    out = get_nth_prime(2)
    assert out == 3

def test_get_nth_prime_1():
    out = get_nth_prime(2.1)
    assert out == None

def test_get_nth_prime_3():
    out = get_nth_prime(29)
    assert out == 109


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
