# Здесь должна быть реализация декоратора
def print_result(func):
    def wrapper(*kwargs):
        print(func.__name__)
        result = func(*kwargs)
        if type(result) is list:
            for i in result:
                print(i)
        elif type(result) is dict:
            for key in result:
                print('{} = {}'.format(key, result[key]))
        else:
            print(result)
        return result
    return wrapper

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()

