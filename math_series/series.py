def fibonacci(n):
    """
      The fibonacci function takes one argument (n) and
      returns the nth Fibonacci number
      Fibonacci series:
      0, 1, 1, 2, 3, 5, 8, 13, ...
      Fibonacci equation:
      fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
      """
    if n==0 or n==1:
        return n
    elif n < 0:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
        The lucas function takes one argument (n) and
        returns the nth Fibonacci number
        Lucas series:
        2, 1, 3, 4, 7, 11, 18, 29, ...
        Lucas equation:
        lucas(n) = lucas(n-1) + lucas(n-2)
        """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n < 0:
        return n
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, first=0, second=1):
    """
      The sum_series function takes one required
      argument (n) and two optional arguments
      (first) and (second) which takes the
      first and second arguments of a template
      of Fibonacci series
      Lucas series:
      first, second, first+second, first+2second, 2first+3second,  3first+5second, ...
      Lucas equation:
      lucas(n) = lucas(n-1) + lucas(n-2)
      """

    if n==0:
        return first
    elif n==1:
        return second
    elif n < 0:
        return n
    else:
        return sum_series(n-1, first=first, second=second) + sum_series(n-2, first=first, second=second)
