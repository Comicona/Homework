def password_required(func):
    def wrapper():
        pas = input('Enter your password: ')
        if pas=='8':
            return func()
        else:
            return 'Access denied'
    return wrapper

def Koba():
    return'Knowing you’re different is only the beginning. \
If you accept these differences you’ll be able to get \
past them and grow even closer.'

def Eilish():
    return'If teardrops could be bottled there\'d be swimming pools filled by models'

@password_required
def Tolstoy():
    return 'All happy families are alike; \
each unhappy family is unhappy in its own way.'

switcher = {
    '1': Koba,
    '2': Eilish,
    '3': Tolstoy
}

def get_func(n):
    func = switcher.get(n, lambda:'Invalid number')
    print (func())

check = True

while check:

    print('Menu: '+ '\n\t1) Koba (doesn\'t require autorisation)'
     + '\n\t2) Eilish (doesn\'t require autorisation)'
     + '\n\t3) Tolstoy (require autorisation)')
    
    n = input('Which function to call? ')
    
    get_func(n)
    
    choise = input('Want to try again? ')
    if choise=='Yes':
        check = True
    else:
        check = False
