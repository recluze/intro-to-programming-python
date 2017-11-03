try:
    from a08 import find_cumulative_marks
except ImportError:
    pass

try:
    from a08 import find_top_student
except ImportError:
    pass

epsilon = 1e-2


def test_find_cumulative_marks_i_1():
    results = [
        ('p101111', 'Ali Khayam', 164, 75, 8.9, 125, 0),
        ('p101112', 'Mudasser Farooq', 14, 2.5, 8.3, 760),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
    ]
    results_out = [('p101111', 'Ali Khayam', 372.9), ('p101112', 'Mudasser Farooq', 784.8), ('p101113', 'Tamleek Ali', 88.6)]
    assert find_cumulative_marks(results) == results_out


def test_find_cumulative_marks_i_2():
    results = [
        ('p101111', 'Ali Khayam', 64, 7.5, 19, 25, 99),
        ('p101112', 'Mudasser Farooq', 1.4, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 870, None, 1.6),
        ('p101114', 'Jawad Mansoor', 8.7, 1.2, None, 98.6)
    ]
    results_out = [('p101111', 'Ali Khayam', 214.5), ('p101112', 'Mudasser Farooq', 188.9), ('p101113', 'Tamleek Ali', 871.6), ('p101114', 'Jawad Mansoor', 108.5)]
    assert find_cumulative_marks(results) == results_out


def test_find_cumulative_marks_i_3():
    results = [
        ('p101111', 'Ali Khayam', None, 12.5, 8, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, None, 76),
        ('p101113', 'Tamleek Ali', 87, None, None),
        ('p101114', 'Jawad Mansoor', 817, None, 908.6)
    ]
    results_out = [('p101111', 'Ali Khayam',  144.5), ('p101112', 'Mudasser Farooq', 118.5), ('p101113', 'Tamleek Ali', 87), ('p101114', 'Jawad Mansoor', 1725.6)]
    assert find_cumulative_marks(results) == results_out


def test_find_cumulative_marks_i_4():
    results = [
        ('p101111', 'Ali Khayam', None, None, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 8.5, None, 76),
        ('p101113', 'Tamleek Ali', 87, None, 19.6),
        ('p101114', 'Jawad Mansoor', None, None, None, None)
    ]
    results_out = [('p101111', 'Ali Khayam',  213), ('p101112', 'Mudasser Farooq', 98.5), ('p101113', 'Tamleek Ali', 106.6), ('p101114', 'Jawad Mansoor', 0)]
    assert find_cumulative_marks(results) == results_out

def test_find_cumulative_marks_i_5():
    results = []
    results_out = []
    assert find_cumulative_marks(results) == results_out


def test_find_cumulative_marks_i_6():
    results = [
        ('p101111', 'Ali Khayam'),
    ]
    results_out = [('p101111', 'Ali Khayam',  0)]
    assert find_cumulative_marks(results) == results_out


def test_find_top_student_i_1():
    results = [
        ('p101111', 'Ali Khayam', 64, 7, 1, None, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
    ]
    results_out = ('p101112', 'Mudasser Farooq')
    assert find_top_student(results) == results_out


def test_find_top_student_i_2():
    results = [
        ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 140, 128.5, 83, 176),
        ('p101113', 'Tamleek Ali', 87, None, 1.6),
        ('p101114', 'Jawad Mansoor', 87, None, None, 98.6)
    ]
    results_out = ('p101112', 'Mudasser Farooq')
    assert find_top_student(results) == results_out


def test_find_top_student_i_3():
    results = [
        ('p101111', 'Ali Khayam', None, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 18.5, None, 76),
        ('p101113', 'Tamleek Ali', 87, None, 19.6),
        ('p101114', 'Jawad Mansoor', 87, None, None, 9.6)
    ]
    results_out = ('p101111', 'Ali Khayam')
    assert find_top_student(results) == results_out


def test_find_top_student_i_5():
    results = [
        ('p101111', 'Ali Khayam', 0),
        ('p101112', 'Mudasser Farooq', 0),
        ('p101113', 'Tamleek Ali', 0),
    ]
    results_out = [('p101111', 'Ali Khayam'), ('p101112', 'Mudasser Farooq'), ('p101113', 'Tamleek Ali')]
    assert find_top_student(results) == results_out


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
