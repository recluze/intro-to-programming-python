try:
    from a04 import get_grade, calculate_sgpa
except ImportError:
    pass

epsilon = 1e-4

def test_grade_int_1():
    score = 90
    assert get_grade(score) == 'A+'


def test_grade_int_2():
    score = 86
    assert get_grade(score) == 'A'

def test_grade_int_3():
    score = 89
    assert get_grade(score) == 'A'


def test_grade_int_4a():
    score = 85
    assert get_grade(score) == 'A-'

def test_grade_int_4b():
    score = 82
    assert get_grade(score) == 'A-'

def test_grade_int_5a():
    score = 81
    assert get_grade(score) == 'B+'

def test_grade_int_5b():
    score = 78
    assert get_grade(score) == 'B+'


def test_grade_int_6a():
    score = 77
    assert get_grade(score) == 'B'

def test_grade_int_6b():
    score = 74
    assert get_grade(score) == 'B'


def test_grade_int_7a():
    score = 73
    assert get_grade(score) == 'B-'

def test_grade_int_7b():
    score = 70
    assert get_grade(score) == 'B-'


def test_grade_int_8a():
    score = 69
    assert get_grade(score) == 'C+'

def test_grade_int_8b():
    score = 66
    assert get_grade(score) == 'C+'

def test_grade_int_9a():
    score = 65
    assert get_grade(score) == 'C'

def test_grade_int_9b():
    score = 62
    assert get_grade(score) == 'C'

#
# def test_grade_int_10a():
#     score = 61
#     assert get_grade(score) == 'C-'

def test_grade_int_10b():
    score = 58
    assert get_grade(score) == 'C-'

# def test_grade_int_11a():
#     score = 57
#     assert get_grade(score) == 'D+'
#
# def test_grade_int_11b():
#     score = 54
#     assert get_grade(score) == 'D+'

def test_grade_int_12a():
    score = 53
    assert get_grade(score) == 'D'

def test_grade_int_12b():
    score = 50
    assert get_grade(score) == 'D'

def test_grade_int_13a():
    score = 49
    assert get_grade(score) == 'F'

# def test_grade_int_13b():
#     score = 0
#     assert get_grade(score) == 'F'


def test_sgpa_int_1():
    assert abs(calculate_sgpa('A', 'A', 'C') - 3.3333) < epsilon


def test_sgpa_int_2():
    assert abs(calculate_sgpa('F', 'F', 'F') - 0) < epsilon


def test_sgpa_int_3():
    assert abs(calculate_sgpa('A', 'C', 'F') - 2.0) < epsilon


def test_sgpa_int_4():
    assert abs(calculate_sgpa('F', 'F', 'nothing') - 0) < epsilon
