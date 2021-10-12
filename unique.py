from genRandom import genRandom

class Unique(object):
    index = 0
    mas = []
    def __init__(self, items, **kwargs):
        ignore_case = kwargs.get('ignore_case')
        cur = list(items)
        for i in cur:
            if ignore_case and type(i) == str:
                if not(i.lower() in [x.lower() for x in self.mas]):
                    self.mas.append(i)
            else:
                if not(i in self.mas):
                    self.mas.append(i)
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        pass


    def __next__(self):
        array_length = len(self.mas)
        prev_index = self.index

        if self.index < array_length:
            self.index += 1

        if prev_index <= array_length and prev_index < array_length:
            return self.mas[prev_index]
        else:
            self.index = 0
            raise StopIteration

    def __iter__(self):
        return self

def main():
    data = ['A', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    data1 = Unique(data, ignore_case=True)

    for i in data1:
        print(i)

if __name__ == "__main__":
    main()