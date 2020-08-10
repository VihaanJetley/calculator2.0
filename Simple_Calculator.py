import time
#Problem 1
nl = [1, 2, 3, 4, 5, 6, 7, 8]
def square_nums(numslist):
  for i in numslist:
      newlist = [i**2 for i in numslist]
  return newlist

# Problem 2
def display_square_nums(numslist):
  for i in numslist:
      newlist = [i**2 for i in numslist]
  print(newlist)

# Problem 3
wd = ['Monday', 'Tuesday', 'Wednesday,', 'Thursday', 'Friday']
def is_weekend(day_of_week):
  if day_of_week.title() == 'Saturday':
    return True
  elif day_of_week.title() == 'Sunday':
    return True
  elif day_of_week.title() in wd:
    return False
  else:
    return 'Invalid day of week'


# Problem 4
def is_isosceles(a, b, c):
  if a == b or b == c or a == c:
      if a + b + c == 180:
        return True
  else:
      return False


# Problem 5
# Implement trigonometric function
from math import sin, cos, tan, radians
def calc_sin(angle):
    a = float(angle)
    try:
        return sin(radians(a))
    except:
        return 'Error'


def calc_cos(angle):
    a = float(angle)
    try:
        return cos(radians(a))
    except:
        return 'Error'


def calc_tan(angle):
    a = float(angle)
    try:
        return tan(radians(a))
    except:
        return 'Error'


from math import log, sqrt

m = 'Bad input argument'
# Question 1
# Specify code to import so sqrt and log functions can work
# Fill in the blanks and uncomment  code below
input_prompt = """Select operation by letter:
                        Addition       : A
                        Subtraction    : S
                        Multiplication : M
                        Division       : D
                        Square         : X
                        Square Root    : Y
                        Logarithm      : L
                        Exponential    : E 
                        Quit           : Q
                        Cosine         : C
                        Tangent        : T
                        Sine           : B
                      """
from math import sqrt, log

asmd = ['A', 'S', 'M', 'D']
xy = ['X', 'Y']
el = ['E', 'L']
ctb = ['C', 'T', 'B']

# Question 2
def check_input(s):
    try:
        float(s)
        return True
    except:
        return False


# Question 3
def do_basic_arithmetic(func):
    i1 = input('First Number: ')
    i2 = input('Second Number: ')
    if func.title() == 'A':
        if check_input(i1) == True and check_input(i2) == True:
            return float(i1) + float(i2)
        else:
            return m
    if func.title() == 'S':
        if check_input(i1) == True and check_input(i2) == True:
            return float(i1) - float(i2)
        else:
            return m
    if func.title() == 'M':
        if check_input(i1) == True and check_input(i2) == True:
            return float(i1) * float(i2)
        else:
            return m
    if func.title() == 'D':
        if check_input(i1) == True and check_input(i2) == True:
            try:
                return float(i1)/float(i2)
            except:
                return 'Undefined'
        else:
            return m


# Question 4
def do_square_or_sqrt(func):
    num = input('Enter number: ')
    if func.title() == 'X':
        if check_input(num) == True:
            return float(num) ** 2
        else:
            return m
    if func.title() == 'Y':
        try:
            return sqrt(float(num))
        except:
            return m


# Question 5
def do_exp_or_log(func):
    if func.title() == 'L':
        num1 = input('Enter number: ')
        num2 = input('Enter another number: ')
        try:
            return log(float(num1), float(num2))
        except:
            return m
    if func.title() == 'E':
        num1 = input('Enter number: ')
        num2 = input('Enter another number: ')
        if check_input(num1) == True and check_input(num2) == True:
            return pow(float(num1), float(num2))
        else:
            return m
def trig(func):
    angle = input('Enter Angle Value: ')
    if check_input(angle) == True:
        if func.title() == 'B':
            return calc_sin(angle)
        elif func.title() == 'C':
            return calc_cos(angle)
        elif func.title() == 'T':
            return calc_tan(angle)


# Question 6


def get_input_and_calculate():
    func = input(input_prompt)
    if func.title() in asmd:
        return do_basic_arithmetic(func)
    elif func.title() in xy:
        return do_square_or_sqrt(func)
    elif func.title() in el:
        return do_exp_or_log(func)
    elif func.title() in ctb:
        return trig(func)
    elif func.title() == 'Q':
        print('bye')
        time.sleep(2)
        exit()
    else:
        return m


def main():
    while True:
        res = get_input_and_calculate()
        print(res)
        time.sleep(3)
if __name__ == '__main__':
    main()




