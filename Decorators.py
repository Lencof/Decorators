# __Author__ __Lencof__
# Decorators.py

# create def document_it(func):
def document_it(func):
  def new_function(*args, **kwargs): # your name text
    print('Running function:', func.__name__) # your text
    print('Positional arguments:', args) # your text
    print('Keyword arguments:', kwargs) # your text
    result = func(*args, **kwargs)
    print('Result:', result) # your text
    return result # use function return
  return new_function # use return
