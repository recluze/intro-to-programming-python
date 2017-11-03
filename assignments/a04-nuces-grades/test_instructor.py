try:
    from a04 import get_grade, calculate_sgpa
except:
    pass

epsilon = 1e-3


def test_grade_float_1():
    score = 89.50
    assert get_grade(score) == 'A+'


def test_grade_float_2():
    score = 89.49
    assert get_grade(score) == 'A'

def test_grade_float_3():
    score = 89.1
    assert get_grade(score) == 'A'


def test_grade_float_4():
    score = 49.49
    assert get_grade(score) == 'F'


def test_sgpa_int_1():
    assert abs(calculate_sgpa('nothing', 'F', 'nothing') - 0) < epsilon

def test_sgpa_int_2():
    assert abs(calculate_sgpa('nothing', 'A', 'nothing') - 4.0) < epsilon

def test_sgpa_int_3():
    assert abs(calculate_sgpa('nothing', 'B+', 'A') - 3.665) < epsilon

def test_sgpa_int_4():
    assert abs(calculate_sgpa('C-', 'B+', 'nothing') - 2.5) < epsilon

def test_sgpa_int_5():
    assert abs(calculate_sgpa('C-', 'D+', 'nothing') - 1.5) < epsilon

def test_sgpa_int_6():
    assert abs(calculate_sgpa('nothing', 'nothing', 'nothing') - 0) < epsilon

def test_sgpa_int_6():
    assert abs(calculate_sgpa('D+', 'nothing', 'B+') - 2.33) < epsilon

def test_sgpa_int_6():
    assert abs(calculate_sgpa('C-', 'nothing', 'B+') - 2.5) < epsilon

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
