from time import clock

def timer(f):
    def _f(*args):
        t0 = clock()
        f(*args)
        return clock() - t0
    return _f
