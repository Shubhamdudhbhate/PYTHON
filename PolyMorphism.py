class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show(self):
        print(f"{self.real} + {self.img}i")

    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.img - other.img)

    def __mul__(self, other):
        r = self.real * other.real - self.img * other.img
        i = self.real * other.img + self.img * other.real
        return Complex(r, i)

    def __truediv__(self, other):
        denom = other.real**2 + other.img**2
        r = (self.real * other.real + self.img * other.img) / denom
        i = (self.img * other.real - self.real * other.img) / denom
        return Complex(round(r, 2), round(i, 2))

    def __floordiv__(self, other):
        div = self.__truediv__(other)
        return Complex(int(div.real), int(div.img))

    def __mod__(self, other):
        return Complex(self.real % other.real, self.img % other.img)

    def __pow__(self, power):
        result = Complex(1, 0)
        for _ in range(power):
            result = result * self
        return result

    def __eq__(self, other):
        return self.real == other.real and self.img == other.img

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __ge__(self, other):
        return abs(self) >= abs(other)

    def __abs__(self):
        return (self.real**2 + self.img**2)**0.5

    def __neg__(self):
        return Complex(-self.real, -self.img)

    def __str__(self):
        return f"{self.real} + {self.img}i"

    def __repr__(self):
        return f"Complex({self.real}, {self.img})"

    def __bool__(self):
        return self.real != 0 or self.img != 0

    def __del__(self):
        print(f"Deleted Complex({self.real}, {self.img})")


# === Testing All Dunder Functions ===

a = Complex(4, 5)
b = Complex(1, 2)
a.show()
b.show()
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("True Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power (a^2):", a ** 2)

print("Equal:", a == b)
print("Not Equal:", a != b)
print("Less Than:", a < b)
print("Greater Than:", a > b)
print("Less Than or Equal:", a <= b)
print("Greater Than or Equal:", a >= b)

print("Absolute Value of a:", abs(a))
print("Negation of a:", -a)
print("String:", str(a))
print("Representation:", repr(a))
print("Is non-zero?", bool(a))

# Object deletion (will call __del__)
del a
del b
