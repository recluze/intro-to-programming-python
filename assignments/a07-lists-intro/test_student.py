try:
    from a07 import calculate_sgpa, calculate_sgpa_weighted
except ImportError:
    pass

epsilon = 1e-2


def test_calculate_sgpa_1():
    assert calculate_sgpa(['A+', 'A', 'A', 'D']) == 3.25

def test_calculate_sgpa_2():
    assert calculate_sgpa(['A+', 'A', 'A', 'C', None]) == None

def test_calculate_sgpa_3():
    assert calculate_sgpa(['D', 'A', 'C-', 'D+', 'C']) == 2.0

def test_calculate_sgpa_4():
    assert calculate_sgpa(['D', 'A', 'C-', 'D+', 'X']) == None

def test_calculate_sgpa_5():
    assert calculate_sgpa(['D', 'A', 'C-', 'D+', 1.0]) == None

def test_calculate_sgpa_6():
    assert calculate_sgpa(['A', 'B', 'C', 'D']) == 2.5

def test_calculate_sgpa_7():
    assert calculate_sgpa(['C+', 'B+', 'C-', 'D+']) == 2.165

def test_calculate_sgpa_8():
    assert calculate_sgpa(['A', 'B-', 'C-', 'D+']) == 2.4175

def test_calculate_sgpa_1_1():
    assert abs(calculate_sgpa(['D+', 'A-', 'B+', 'D+', 'C+', 'A-', 'A+']) - 2.80) < epsilon

def test_calculate_sgpa_1_2():
    assert calculate_sgpa([]) == 0

def test_calculate_sgpa_1_3():
    assert calculate_sgpa(None) == None

def test_calculate_sgpa_1_4():
    assert calculate_sgpa('B') == 3.0

def test_calculate_sgpa_1_5():
    assert calculate_sgpa('B+') == 3.33



def test_calculate_sgpa_weighted_s_1():
    assert calculate_sgpa_weighted('A+', 4) == 4.0

def test_calculate_sgpa_weighted_s_2():
    assert calculate_sgpa_weighted('B', 3) == 3.0

def test_calculate_sgpa_weighted_s_3():
    assert abs(calculate_sgpa_weighted(['A', 'B'], [4, 3]) - 3.57) < epsilon

def test_calculate_sgpa_weighted_s_4():
    assert abs(calculate_sgpa_weighted(['D+', 'C+'], [3, 1]) - 1.58) < epsilon

def test_calculate_sgpa_weighted_s_5():
    assert calculate_sgpa_weighted(['B', 'C-'], [3]) == None

def test_calculate_sgpa_weighted_s_6():
    try:
        calculate_sgpa_weighted(None) == None
        assert False
    except TypeError:
        return

    assert False

def test_calculate_sgpa_weighted_s_7():
    assert abs(calculate_sgpa_weighted(['B+', 'C-', 'A+', 'C-'], [3, 1, 3, 4]) - 2.75) < epsilon

def test_calculate_sgpa_weighted_s_8():
    assert calculate_sgpa_weighted(['D+', 'A-', 'C+', 'X'], [3, 3, 1, 2]) == None


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
