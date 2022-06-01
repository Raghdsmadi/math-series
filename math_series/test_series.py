from math_series.series import fibonacci,lucas,sum_series
# fibonacci tests
def test_fibonacci_at_0():
    assert fibonacci(0) == 0

def test_fibonacci_at_2():
    assert fibonacci(2) == 1

def test_fibonacci_at_5():
    assert fibonacci(5) == 5

def test_fibonacci_at_7():
    assert fibonacci(7) == 13

def test_fibonacci_at_20():
    assert fibonacci(20) == 6765

# lucas tests
def test_lucas_at_0():
    assert lucas(0) == 2
def test_lucas_at_0():
    assert lucas(1)==1
    
def test_lucas_at_2():
    assert lucas(2) == 3

def test_lucas_at_5():
    assert lucas(5) == 11

def test_lucas_at_7():
    assert lucas(7) == 29

def test_lucas_at_20():
    assert lucas(20) == 15127

# sum_series tests
def test_sum_series_at_20_as_fibo():
    assert sum_series(20) == 6765

def test_sum_series_at_20_as_lucas():
    assert sum_series(20, first=2, second=1) == 15127

def test_sum_series_at_20_for_other_series():
    assert sum_series(20, first=5, second=3) == 41200