msg_ = ["Enter an equation",
        "Do you even know what numbers are? Stay focused!",
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "Yeah... division by zero. Smart move...",
        "Do you want to store the result? (y / n):",
        "Do you want to continue calculations? (y / n):",
        " ... lazy",
        " ... very lazy",
        " ... very, very lazy",
        "You are",
        "Are you sure? It is only one digit! (y / n)",
        "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)"]


class Calculator:
    def __init__(self, x, op, y):
        self.x = x
        self.op = op
        self.y = y
        self.result = False

    def calculate(self):
        match self.op:
            case '+':
                self.result = self.x + self.y
            case '-':
                self.result = self.x - self.y
            case '*':
                self.result = self.x * self.y
            case '/':
                try:
                    self.result = self.x / self.y
                except ZeroDivisionError:
                    self.result = True  # change result so it is known there is an exception

    @staticmethod
    def make_number(x):
        if x.isnumeric():
            return int(x)
        else:
            try:
                return float(x)
            except ValueError:
                return False

    @staticmethod
    def check_op(op):
        if op == '+' or op == '-' or op == '*' or op == '/':
            return True
        return False

    @staticmethod
    def check(v1, v2, v3):
        msg = ''

        if Calculator.is_one_digit(v1) and Calculator.is_one_digit(v2):
            msg += msg_[6]

        if (v1 == 1 or v2 == 1) and v3 == '*':
            msg += msg_[7]

        if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
            msg += msg_[8]

        if msg != '':
            msg = msg_[9] + msg
            print(msg)

    @staticmethod
    def is_one_digit(v):
        return -10 < v < 10 and (float.is_integer(float(v)))


def main():
    memory = 0

    while True:
        inp = input(f'{msg_[0]}\n').split()
        calc = Calculator(Calculator.make_number(inp[0]), inp[1], Calculator.make_number(inp[2]))

        if inp[0] == 'M':
            calc.x = memory
        if inp[2] == 'M':
            calc.y = memory
        if (type(calc.x) is bool) or (type(calc.y) is bool):
            print(msg_[1])
            continue

        if not Calculator.check_op(calc.op):
            print(msg_[2])
            continue

        Calculator.check(calc.x, calc.y, calc.op)

        calc.calculate()
        if calc.result is True:  # ZeroDivisionError
            print(msg_[3])
            continue

        print(float(calc.result))

        while True:
            answer = input(f'{msg_[4]}\n')
            if answer == 'y':
                if Calculator.is_one_digit(calc.result):
                    msg_index = 10
                    while True:
                        answer = input(f'{msg_[msg_index]}\n') 
                        if answer == 'y':
                            if msg_index < 12:
                                msg_index += 1
                                continue
                            else:
                                memory = calc.result
                                answer = 'n'
                                break
                        else:
                            if answer == 'n':
                                break
                            else:
                                continue
                    if answer == 'n':
                        break
                else:
                    memory = calc.result
                    break
            else:
                if answer == 'n':
                    break
                else:
                    continue
        while True:
            answer = input(f'{msg_[5]}\n')  # print msg_5
            if answer == 'y':
                break
            else:
                if answer == 'n':
                    break
                else:
                    continue
        if answer == 'y':
            continue
        break  # end


main()
