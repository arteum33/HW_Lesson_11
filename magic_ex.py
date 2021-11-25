#

class Numbers():
    def __init__(self, value):
        self.value = value

    def __eq__(self, other): # ==
        return self.value == other.value

    def __ne__(self, other): # !=
        return self.value != other.value

    def __lt__(self, other): # <
        return self.value < other.value

    def __gt__(self, other): # >
        return self.value > other.value

    def __le__(self, other): # <=
        return self.value <= other.value

    def __ge__(self, other): # >=
        return self.value >= other.value
    def __add__(self, other): # +
        return self.value + other.value
    def __float__(self): #Numbers => Float
        return self.value**0.5

    def __len__(self):
        return (self.value)


    # метод класса
    @classmethod
    def class_method_ex(cls):
        number_list = []
        for i in range(5):
            number_list.append((cls(i)))
        return number_list

if __name__ == '__main__':
    a = Numbers(2)
    b = Numbers(3)
    str_ex = 'photo'
    print('1. Сравнение чисел А и В: ', a == b)
    print('2. Неравенство чисел А и В: ', a != b)
    print('3. Число А < В: ', a < b)
    print('4. Число А > В: ', a > b)
    print('6 Число А <= В: ', a <= b)
    print('7. Число А >= В: ', a >= b)
    print('8. Cумма А и В: ', a + b)
    print('9. Вывод дробного числа: ', float(a))
    print('10. Длина строки: ', len(str_ex))
    num_list = Numbers.class_method_ex()
    print('11. ', num_list)

