# calculator.py

def sum(m, n):
    result = m
    if n < 0:
        for i in range(abs(n)):
            result -= 1
    else:
        for i in range(n):
            result += 1

    return result

def divide(m, n):
    result = 0

    negResult = m < 0 and n > 0 or \
                m > 0 and n < 0

    if n == 0:
        raise ZeroDivisionError("You cannot divide by 0!")
    
    m = abs(m)
    n = abs(n)

    while (m - n >= 0):
        m -= n
        result += 1

    if negResult:
        result = - result

    return result

def subtract(m, n):
    result = m

    if n < 0:
        for i in range(abs(n)):
            result += 1
    else:
        for i in range(n):
            result -= 1
    
    return result

def multiply(m, n):
    result = 0

    negResult = m < 0 and n > 0 or \
                m > 0 and n < 0
    
    m = abs(m)
    n = abs(n)

    for i in range(n):
        result += m

    if negResult:
        result = -result

    return result

def gcd(m, n):
    if m < 0 or n < 0:
        raise ValueError("The gcd input must be positive integer!")

    if n == 0:
        return m

    r = n

    while r != 0:
        r = m % n
        
        if r != 0:
            m = n
            n = r
    
    return n

def percentage(m, n):
    if m < 0 or n < 0:
        raise ValueError("The gcd input must be positive integer!")

    result = 0

    return (m * n)/100