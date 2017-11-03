def sqrt(x, guess = 1.0):
    if x < 0:
        print("Got a request for square root of negative number.")
        raise ValueError

    print("Find sqrt of {} starting with guess {}".format(x, guess))
    if good_enough(guess, x):
        return guess
    else:
        print("Guess isn't good enough. Improve ...")
        new_guess = improve_guess(guess, x)
        return sqrt(x, new_guess)

def good_enough(guess, x):
    print("Checking if {} is a good enough guess.".format(guess))
    if abs(guess * guess - x) < 0.1:
        return True
    else:
        return False



def avg(a, b):
    return (a+b)/2.0

def improve_guess(guess, x):
    new_guess = avg(guess, x/guess)
    print("Improved guess to: {}".format(new_guess))
    return new_guess


print sqrt(36)

### Alternatively

# import logging
# logging.basicConfig(level=logging.DEBUG)   # DEBUG, INFO, WARN, ERROR
#
# # add: filename='sqrt.log'
#
# def sqrt(x, guess = 1.0):
#     if x < 0:
#         logging.error("Got a request for square root of negative number.")
#         raise ValueError
#
#     logging.info("Find sqrt of {} starting with guess {}".format(x, guess))
#     if good_enough(guess, x):
#         return guess
#     else:
#         logging.debug("Guess isn't good enough. Improve ...")
#         new_guess = improve_guess(guess, x)
#         return sqrt(x, new_guess)
#
# def good_enough(guess, x):
#     logging.debug("Checking if {} is a good enough guess.".format(guess))
#     if abs(guess * guess - x) < 0.1:
#         return True
#     else:
#         return False
#
#
#
# def avg(a, b):
#     return (a+b)/2.0
#
# def improve_guess(guess, x):
#     new_guess = avg(guess, x/guess)
#     logging.debug("Improved guess to: {}".format(new_guess))
#     return new_guess
#
# print sqrt(36)  # try sending -36
