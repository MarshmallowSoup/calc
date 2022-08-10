
import operator
digits = ('0123456789')
def Numbers(var):
    return var in digits

def Test4Num(varstr):
    n = 0
    var = ''
    try: 
        while Numbers(varstr[n]):
            var += varstr[n]
            n += 1
    except: pass
    return (int(var), n)

OPERATIONS = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '^' : operator.pow,
    '|' : operator.xor
}


def operation(string, num1, num2): #perform_
    op = OPERATIONS.get(string, None)
    if op is not None:
        return op(num1, num2)
    else:
        return None

'''def operation(string, num1, num2):
    if string == '+':
        return num1 + num2
    if string == '-':
        return num1-num2
    if string == '*':
        return num1*num2
    if string == '/':
        return num1/num2
    if string == '^':
        return num1 ** num2
    if string == '|':
        return num1 | num2'''


def operator(operato):
    return operato == '+' or operato == '-' or operato == '*' or operato == '/' or operato == '^'



def eval_math_expr(expr):
    negate = False
    while True:
        try: 
            if expr[0] == '-': #for negative numbers
                negate = True #because here the numbers are string format
                expr = expr[1:]
            number1 = Test4Num(expr)[0]
            if negate == True:
                number1 = -number1
                negate = False
            end_number1 = Test4Num(expr)[1]
            expr = expr[end_number1:]
            if expr == '':
                return number1
            op = expr[0]
            expr = expr[1:]
            number2 = Test4Num(expr)[0]
            end_number2 = Test4Num(expr)[1]
            result = operation(op, number1, number2)
            number1 = result
            expr = str(number1) + expr[end_number2:]
        except Exception as e:
            print(e)
            break
    return number1


expr = input('Enter your expression:')
print(expr + '=')
print(eval_math_expr(expr))