from time import ctime,sleep

def tsfunc(func):
    def warppedFunc():
        print '[%s] %s() called' %(ctime(),func.__name__)
        return func()
    return warppedFunc
def test(func):
    print 'test!'
    return func
@test
@tsfunc
def foo():
    pass
foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()

