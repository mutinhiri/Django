def announce(f):
    def wrapper():
        print('About to run the function')
        f()
        print('Done withb  the function')

    return wrapper

@announce
def hello():
    print('Retuen hello ')


hello()