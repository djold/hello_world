class Fraction:
    def __init__(self, namber, demon):
        self.namber = namber
        self.demon = demon

    def __str__(self):
        return f"{self.namber} / {self.demon}"

fast = Fraction(65, 23)


print(fast)







































