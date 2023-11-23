# a = 1
# b = 2
# print(a)
# print(B)

# run this file using this and that will give error
# pylint pylint-test.py
# pylint-test.py:4:6: E0602: Undefined variable 'B' (undefined-variable)

# ************* Module pylint-test
# pylint-test.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# pylint-test.py:1:0: C0103: Module name "pylint-test" doesn't conform to snake_case naming style (invalid-name)
# pylint-test.py:1:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
# pylint-test.py:2:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
# pylint-test.py:4:6: E0602: Undefined variable 'B' (undefined-variable)

# ------------------------------------------------------------------
# Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)


def myfunc():
    a = 1
    b = 2
    print(a)
    print(b)

myfunc()
