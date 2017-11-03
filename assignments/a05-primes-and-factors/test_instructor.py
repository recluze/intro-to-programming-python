try:
    from a05 import is_prime, get_largest_prime, output_factors
except:
    pass

def test_isprime_float_1():
    assert is_prime(6.1) == False

def test_isprime_float_2():
    assert is_prime(19.01) == False

def test_isprime_float_3():
    assert is_prime(2.0) == True

def test_isprime_float_4():
    assert is_prime(3.0) == True


def test_isprime_neg_1():
    assert is_prime(-2) == None


# largest_prime

def test_get_prime_1():
    assert get_largest_prime(1.0) == None

def test_get_prime_2():
    assert get_largest_prime(2.05) == 2

# output factors

def test_output_factors_1():
    v, out = capture_output(output_factors)(867)
    assert out == '\n'.join([str(x) for x in [1, 3, 17, 51, 289, 867]]) + "\n"


def test_output_factors_2():
    v, out = capture_output(output_factors)(7658)
    assert out == '\n'.join([str(x) for x in [1, 2, 7, 14, 547, 1094, 3829, 7658]]) + "\n"




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
