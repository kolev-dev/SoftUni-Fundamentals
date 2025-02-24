class Number:
    def __init__(self, num):
        self.num = num

    def __mul__(self, other):
        return Number(self.num * other.num)

first_number = Number(200)
second_number = Number(2)

multiplied = first_number * second_number
print(multiplied.num)
