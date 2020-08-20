def pres(stack, input1):
    top1 = stack[-1]
    precedence = {'^': 3, '/': 2, '*': 2, '+': 1, '-': 1}
    try:
        if(precedence[top1] >= precedence[input1]):
            return True
        else:
            return False
    except KeyError:
        return False


def func1(arr, capacity):
    stack = []
    output = []
    operators = ['+', '-', '*', '/', '^']
    top = -1
    for ch in arr:
        if(ch.isalpha()) == True:
            output.append(ch)

        elif(ch == '('):
            stack.append(ch)
            top += 1
        elif(ch == ')'):
            while((stack) and stack[-1] != '('):
                if(stack):
                    a = stack.pop()
                    top -= 1
                    output.append(a)
                else:
                    output.append('$')
                if((stack) and stack[-1] != '('):
                    return -1
                    stack.pop()
        else:
            while((top != -1) and pres(stack, ch)):
                if(stack):
                    a = stack.pop()
                    top -= 1
                    output.append(a)
                else:
                    output.append('$')
            top += 1
            stack.append(ch)
    while stack:
        if(stack):
            a = stack.pop()
            top -= 1
            output.append(a)
        else:
            output.append('$')
    print(*output, sep='')

    #array=input('Enter infix expression')
# arr='a+b*(c^d-e)^(f+g*h)-i'
arr = 'a+b-i+g-h*j'
func1(arr, len(arr))


class Conversion:

    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False

    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]

    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)

    # A utility function to check is the given character
    # is operand
    def isOperand(self, ch):
        return ch.isalpha()

    # Check if the precedence of operator is strictly
    # less than top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    # The main function that converts given infix expression
    # to postfix expression
    def infixToPostfix(self, exp):

        # Iterate over the expression for conversion
        for i in exp:
            # If the character is an operand,
            # add it to output
            if self.isOperand(i):
                self.output.append(i)

            # If the character is an '(', push it to stack
            elif i == '(':
                self.push(i)

            # If the scanned character is an ')', pop and
            # output from the stack until and '(' is found
            elif i == ')':
                while((not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()

            # An operator is encountered
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)

        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())

        print("".join(self.output))


# Driver program to test above function
exp = "a+b-i+g-h*j"
obj = Conversion(len(exp))
obj.infixToPostfix(exp)
