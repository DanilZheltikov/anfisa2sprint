def func():
    try:
        print('test1')
    finally:
        return 'test2'

print(func())