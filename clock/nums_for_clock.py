a = '\u2B1C'
b = '  '
ps = '\n'

zero = [(a*4), (a + b + b + a), (a + b + b + a), (a + b + b + a), (a*4)]
one = [(b + b + a + b), (b + a + a + b), (b + b + a + b), (b + b + a + b), (a*4)]
two = [(a*4), (b + b + b + a), (a*4), (a + b + b + b), (a*4)]
three = [(a*4), (b + b + b + a), (a*4), (b + b + b + a), (a*4)]
four = [(a + b + b + a), (a + b + b + a), (a*4), (b + b + b + a), (b + b + b + a)]
five = [(a*4), (a + b + b + b), (a*4), (b + b + b + a), (a*4)]
six = [(a*4), (a + b + b + b), (a*4), (a + b + b + a), (a*4)]
seven = [(a*4), (b + b + b + a), (b + b + b + a), (b + b + b + a), (b + b + b + a)]
eight = [(a*4), (a + b + b + a), (a*4), (a + b + b + a), (a*4)]
nine = [(a*4), (a + b + b + a), (a*4), (b + b + b + a), (a*4)]
dots = [(b*4),(b + a + b + b), (b*4), (b + a + b + b), (b*4)]

nums = {'0' : zero, '1' : one, '2' : two, '3' : three, '4' : four, '5' : five, '6' : six, '7' : seven, '8' : eight, '9' : nine, ':': dots}

def get_num(n):
    return nums.get(n)

def print_num(num):
    return(num[0] + ps + num[1] + ps + num[2] + ps + num[3] + ps + num[4])

def print_time(time):
    print(print_num(time[0]) + print_num(time[1]) + print_num(time[2]) + print_num(time[3])
        + print_num(time[4]) + print_num(time[5]) + print_num(time[6]) + print_num(time[7]))