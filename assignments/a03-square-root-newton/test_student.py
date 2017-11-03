try:
    from a03 import sqrt, average, improve_guess
except ImportError:
    pass

epsilon = 1e-4  # precision needed


def test_avg_float():
    a = 1.0
    b = 3.0

    assert abs(average(a, b) - 2.0) < epsilon


def test_avg_int():
    a = 1
    b = 2

    assert abs(average(a, b) - 1.5) < epsilon


def test_sqrt_int():
    v = 36
    assert abs(sqrt(v) - 6) < epsilon


def test_improve_guess():
    n = 36
    g = 4
    assert abs(improve_guess(g, n) - 6.5) < epsilon
