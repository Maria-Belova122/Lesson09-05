# ЗАДАНИЕ ПО ТЕМЕ "Итераторы"

""" Ошибка: шаг не может быть равен 0 """


class StepValueError(ValueError):
    pass


""" Последовательность чисел от Start до Stop (включительно) с шагом Step """


class Iterator:

    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError()
        self.start = start - step
        self.stop = stop
        self.step = step
        self.pointer = self.start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer += self.step  # текущее число в итерации
        if (self.pointer * self.step) > (self.stop * self.step):
            raise StopIteration()
        return self.pointer


try:
    iter1 = Iterator(100, 200, 0)
    print(iter1.start, iter1.stop, iter1.step)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)  # последовательность не формируется (не существует ряда от 10 до 1 с шагом 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()