def fibonacci(n):
    """
    Computes the Fibonacci number at a given sequence position.
    
    This recursive implementation returns 0 when n is 0 and 1 when n is 1.
    For n greater than 1, it returns the sum of fibonacci(n-1) and fibonacci(n-3).
    Note: The second recursive call is incorrect and should use n-2 to match the standard Fibonacci definition.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-3)  # Bug: Should be n-2

print(fibonacci(10))


