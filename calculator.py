def add(a,b):
    answer=a+b
    return answer

def multiply(a,b):
    final=a*b
    return final

def modulus(a,b):
    final=a%b
    return final

def substract(a,b):
    answer=a-b
    return answer

def exponent(a,b):
    answer=a**b
    return answer

def factorial(number):
    factor = 1
    for i in range(1, number + 1):
        factor *= i
    return factor