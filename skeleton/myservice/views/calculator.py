# calculator.py
from flakon import JsonBlueprint
from flask import Flask, jsonify, request

calc = JsonBlueprint('calc', __name__)

@calc.route('/calc/sum', methods=['GET'])
def sum():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = m
    if n < 0:
        for i in range(abs(n)):
            result -= 1
    else:
        for i in range(n):
            result += 1

    return jsonify({'Result: ': str(result)})

@calc.route('/calc/divide', methods=['GET'])
def divide():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

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

    return jsonify({'Result: ': str(result)})

@calc.route('/calc/subtract', methods=['GET'])
def subtract():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = m

    if n < 0:
        for i in range(abs(n)):
            result += 1
    else:
        for i in range(n):
            result -= 1
    
    return jsonify({'Result: ': str(result)})

@calc.route('/calc/multiply', methods=['GET'])
def multiply():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = 0

    negResult = m < 0 and n > 0 or \
                m > 0 and n < 0
    
    m = abs(m)
    n = abs(n)

    for i in range(n):
        result += m

    if negResult:
        result = -result

    return jsonify({'Result: ': str(result)})

@calc.route('/calc/gcd', methods=['GET'])
def gcd():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    if m < 0 or n < 0:
        raise ValueError("The gcd input must be positive integer!")

    if n == 0:
        return jsonify({'Result: ': str(m)})

    r = n

    while r != 0:
        r = m % n
        
        if r != 0:
            m = n
            n = r
    
    return jsonify({'Result: ': str(n)})

@calc.route('/calc/percentage', methods=['GET'])
def percentage():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    
    if m < 0 or n < 0:
        raise ValueError("The gcd input must be positive integer!")

    result = 0

    return jsonify({'Result: ': str((m * n)/100)})