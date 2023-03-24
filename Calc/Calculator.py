class Calculator:
    a = 1
    b = 1
    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b
    def __str__(self):
        return \
            f'a: {self.a}\n' \
            f'b: {self.b}\n' \
            f'Summa: {Calculator.sum(self)}\n' \
            f'Razniza {Calculator.raz(self)}\n' \
            f'Ymnozhenie: {Calculator.mno(self)}\n' \
            f'Delenie: {Calculator.div(self)}\n'
    def sum(self):
        return self.a + self.b
    def raz(self):
        return self.a - self.b
    def mno(self):
        return self.a * self.b
    def div(self):
        if self.b == 0:
            raise ZeroDivisionError
        else:
            return self.a / self.b




    class Multicalculator:
        a = 1
        b = 1
        c = 1
        d = 1
        e = 1
    def __init__(self, a=1, b=1, c=1, d=1, e=1):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
    def __str__(self):
        return \
            f'a: {self.a}\n' \
            f'b: {self.b}\n' \
            f'Summa: {Multicalculator.sum(self)}\n' \
            f'Razniza {Multicalculator.raz(self)}\n' \
            f'Ymnozhenie: {Multicalculator.mno(self)}\n' \
            f'Delenie: {Multicalculator.div(self)}\n'
    def sum(self):
        return self.a + self.b + self.c + self.d + self.e
    def raz(self):
        return self.a - self.b - self.c - self.d - self.e
    def mno(self):
        return self.a * self.b * self.c * self.d * self.e

    def div(self):
        if self.b == 0:
            raise ZeroDivisionError
        elif self.c==0:
            raise ZeroDivisionError
        elif self.d==0:
            raise ZeroDivisionError
        elif self.e==0:
            raise ZeroDivisionError
        else:
             return self.a / self.b / self.c / self.d / self.e