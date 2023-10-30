"""
Recursion - Factorials
"""


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


def _main():
    print(factorial(6))

if __name__ == "__main__":
    _main()
