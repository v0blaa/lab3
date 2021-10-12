import random

def genRandom(num, begin, end):
    for i in range(num):
        yield(random.randint(begin, end))



"""def main():
    num, begin, end = (int(i) for i in input().split())
    gen = genRandom(num, begin, end)
    for i in range(num):
        print(next(gen), end=' ')"""

if __name__ == "__main__":
    main()