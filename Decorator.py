# __Author__ __Lencof__
# Decorator.py

# create def decorator(func):
def decorator(func):
    def wrapper():
        print('Lencof') # your text
        func()
    return wrapper

# create def basic():
def basic():
    print('Lencof') # your text

wrapped = decorator(basic)
print('Lencof') # your text
basic() # close
wrapped() # close
print('Bye!') # your text
