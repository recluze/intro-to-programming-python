try: 
    from a02 import get_area, output_parameter
except: 
    pass 

epsilon = 0.001 # precision needed

import math

def test_floats():
    vals = [2.0, 2.9, 1.9, 22.0, 3.09]

    for v in vals:
        assert abs(get_area(v) - (math.pi * v * v)) < epsilon


def test_parameter_float():
    val = 1.999
    v, out = capture_output(output_parameter)(val)

    assert out.startswith("The parameter of the circle with radius 1.999 is 12.560")



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
