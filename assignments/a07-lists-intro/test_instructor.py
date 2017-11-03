try:
    from a07 import calculate_sgpa, calculate_sgpa_weighted
except ImportError:
    pass

epsilon = 1e-2

def test_calculate_sgpa_9():
    assert calculate_sgpa(['A', 'A-', 'A-', 'D+']) == 3.1675

def test_calculate_sgpa_10():
    assert calculate_sgpa(['C+', 'B', 'D', 'C', None]) == None

def test_calculate_sgpa_11():
    assert calculate_sgpa(['P', 'A', 'C-', 'D+', 'C']) == None

def test_calculate_sgpa_12():
    assert abs(calculate_sgpa(['D+', 'A-', 'B+', 'D+', 'C+', 'A-', 'A+', 'D+', 'C+']) - 2.59) < epsilon

def test_calculate_sgpa_13():
    assert calculate_sgpa(['D', 'A', 'C-', 'D+', 1.0]) == None

def test_calculate_sgpa_14():
    assert calculate_sgpa(['A', 'B', 'C', 'D']) == 2.5

def test_calculate_sgpa_15():
    assert calculate_sgpa(['C+', 'B+', 'C-', 'D+']) == 2.165

def test_calculate_sgpa_16():
    assert calculate_sgpa(['A', 'B-', 'C-', 'D+']) == 2.4175


def test_calculate_sgpa_2_2():
    assert calculate_sgpa(None) == None

def test_calculate_sgpa_2_3():
    assert calculate_sgpa('A+') == 4.0

def test_calculate_sgpa_2_4():
    assert calculate_sgpa('D+') == 1.33

def test_calculate_sgpa_2_5():
    assert calculate_sgpa('C-') == 1.67


def test_calculate_sgpa_weighted_i_1():
    assert calculate_sgpa_weighted('D+', 4) == 1.33

def test_calculate_sgpa_weighted_i_2():
    assert calculate_sgpa_weighted('C-', 3) == 1.67

def test_calculate_sgpa_weighted_i_3():
    assert abs(calculate_sgpa_weighted(['D+', 'C-'], [3, 4]) - 1.52) < epsilon

# def test_calculate_sgpa_weighted_i_4():
#     assert abs(calculate_sgpa_weighted(['B+', 'A-'], [4, 2]) - 3.44) < epsilon

def test_calculate_sgpa_weighted_i_5():
    assert calculate_sgpa_weighted(['A', 'D-'], [1]) == None

def test_calculate_sgpa_weighted_i_6():
    assert calculate_sgpa_weighted(['A'], [1, 6]) == None


def test_calculate_sgpa_weighted_i_8():
    assert calculate_sgpa_weighted(['D+', 'A-', 'C+', 'G'], [3, 3, 1, 2]) == None

def test_calculate_sgpa_weighted_i_9():
    assert calculate_sgpa_weighted(['T', 'A-', 'C+', 'G'], [3, 3, 1, 2]) == None


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
