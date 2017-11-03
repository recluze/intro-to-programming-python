try: 
    from a02 import get_area, output_parameter
except ImportError: 
    pass 

epsilon = 0.001 # precision needed


def test_float():
    r = 2.0
    result = 12.566

    assert abs(get_area(r) - result) < epsilon


def test_int():
    r = 0
    result = 0

    assert abs(get_area(r) - result) < epsilon


def test_parameter_float():
    val = 1.0
    v, out = capture_output(output_parameter)(val)

    assert out.startswith("The parameter of the circle with radius 1.0 is 6.28")



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
