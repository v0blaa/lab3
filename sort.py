def sort(list):
    return sorted(list, reverse=True, key=abs)


data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = sort(data)
    print(result)

    result_with_lambda = sorted(data, key=lambda x: abs(x)*-1)
    print(result_with_lambda)