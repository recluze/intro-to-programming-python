from a01 import code_holder

def test_third():
    assert code_holder(15, 39) == 15+39

def test_negatives():
    assert code_holder(-12, -19) == -12 + -19


# def test_output() :
#     import StringIO
#     import sys
#     orig_stdout = sys.stdout
#     capturedOutput = StringIO.StringIO()
#     sys.stdout = capturedOutput
#     code_holder(3, 35)
#     sys.stdout = orig_stdout # don't rely on __stdout__
#
#     print 'Captured', capturedOutput.getvalue()
#     output_val = capturedOutput.getvalue().strip()
#     assert output_val == 'ok'
