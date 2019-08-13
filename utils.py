from time import sleep
import words
CHAR = 0.3
TIRE_MULTIPLIER = 3
DEBUG=True
SYMBOLS=True


def dot(on_start_func=None, *args, **kwargs):
    if SYMBOLS: print("<\t.\t")
    if on_start_func:
        on_start_func(*args)
    else:
        print(dot.__name__)
    sleep(CHAR)
    if kwargs.get('on_end_func', None):
        kwargs['on_end_func'](*args)

def tire(on_start_func=None, *args, **kwargs):
    if SYMBOLS: print("<\t-\t")
    if on_start_func:
        on_start_func(*args)
    else:
        print(tire.__name__)
    sleep(CHAR * TIRE_MULTIPLIER)
    if kwargs.get('on_end_func', None):
        kwargs['on_end_func'](*args)

def element_wait(*args,**kwargs):
    sleep(CHAR)
    if DEBUG:print("> element wait")

def char_wait(*args,**kwargs):
    sleep(CHAR*3)
    if DEBUG: print(">> char wait")

def word_wait(*args,**kwargs):
    sleep(CHAR*7)
    if DEBUG: print(">>> word wait")



