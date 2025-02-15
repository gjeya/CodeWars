# This function takes two numbers as parameters, the first number being the coefficient, and the second number being the exponent. Take the Derivative
# Your function should multiply the two numbers, and then subtract 1 from the exponent. Then, it has to return an expression (like 28x^7). "^1" should not be truncated when exponent = 2.

def derive(coefficient, exponent): 
    
    mul = coefficient * exponent
    # print(mul)
    exp = exponent - 1
    # print (exp)
    output = f"{mul}x^{exp}"
#     print(output)
    return output

print (derive (5, 7))
print (derive (3,5))