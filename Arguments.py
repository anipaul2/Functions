def double(arg):
    print('Before: ', arg)
    arg = arg*2
    print('After: ', arg)
print(double('hello'))
def change(arg):
    print('Before: ', arg)
    arg.append('More Data')
    print('After: ', arg)
print(change([42,256,16]))