import concurrent.futures
import random as rd
import time
import threading


# creating trapezoid class
class Trapezoid:

    def __init__(self, trap=[0, 0, 0]):
        self.a = min(trap)
        self.b = max(trap)
        self.h = sum(trap) - self.a - self.b

    def __str__(self):
        return 'ტოლფერდა ტრაპეციის დიდი ფუძეა -> {}, პატარა ფუძეა -> {}, ხოლო სიმაღლეა ->{}'.format(self.b, self.a,
                                                                                                    self.h)

    def area(self):
        return (self.a + self.b) / 2 * self.h

    def __lt__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() < other.area()
        return False

    def __eq__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() == other.area()

        return False

    def __ge__(self, other):
        if isinstance(other, Trapezoid):
            return not self.__lt__(other)
        return False

    def __add__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() + other.area()
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() - other.area()
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, Trapezoid):
            if other.area() != 0:
                return self.area() // other.area()
            else:
                raise ValueError("Exception -> Division by zero!")
        return NotImplemented


# creating rectangle class which is child of trapezoid
class Rectangle(Trapezoid):
    def __init__(self, re=None):
        if re is None:
            re = [0, 0]
        super().__init__([re[0], re[1], 0])

    def area(self):
        return self.a * self.b

    def __str__(self):
        return "მართკუთხედის სიმაღლეა -> {}, ხოლო სიგანე -> {}".format(self.a, self.h)

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.area() + other.area()
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            return self.area() - other.area()
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, Rectangle):
            if other.area() != 0:
                return self.area() // other.area()
            else:
                raise ValueError("Exception -> Division by zero!")
        return NotImplemented


# creating square class which is child of rectangle
class Square(Rectangle):
    def __init__(self, c):
        super().__init__([c[0], 0, 0])

    def area(self):
        return pow(self.a, 2)

    def __str__(self):
        return "კვადრატის გვერდია -> {}".format(self.a)

    def __add__(self, other):
        if isinstance(other, Square):
            return self.area() + other.area()
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Square):
            return self.area() - other.area()
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, Square):
            if other.area() != 0:
                return self.area() // other.area()
            else:
                raise ValueError("Exception -> Division by zero!")
        return NotImplemented


# functions to calculate generate areas
def trapezoid_area(arr):  # arr = [[10, 200, 15], [1000, 40, 15], [100, 60, 15]]
    for i in arr:  # i = [10, 20, 15]
        T = Trapezoid(i)
        T.area()
        # you can print here parameters if you want
        # print(T, "ფართობით", T.area())


def rectangle_area(arr):
    for i in arr:
        R = Rectangle(i)
        R.area()
        # you can print here parameters if you want
        # print(R,"ფართობით",  R.area())


def square_area(arr):
    for i in arr:
        S = Square(i)
        S.area()
        # you can print here parameters if you want
        # print(S, "ფართობით", S.area())


def with_threads(arr):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(trapezoid_area, arr)
        executor.map(rectangle_area, arr)
        executor.map(square_area, arr)


def with_processes(arr):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(trapezoid_area, arr)
        executor.map(rectangle_area, arr)
        executor.map(square_area, arr)


def with_mixed(arr):
    num_processes = 5

    start = time.perf_counter()
    for _ in range(num_processes):
        with concurrent.futures.ThreadPoolExecutor() as thread_executor:
            thread_executor.map(trapezoid_area, arr)
            thread_executor.map(rectangle_area, arr)
            thread_executor.map(square_area, arr)

    end = time.perf_counter()
    print("Time with mixed:", round((end - start), 2), "second(s).")


if __name__ == "__main__":
    # Generating parameters for 10000 trapezoid: big base, small base and height
    trapezoids = [[rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200)] for _ in range(10000)]

    # Generating parameters for 10000 rectangles: width and height
    rectangles = [[rd.randint(1, 200), rd.randint(1, 200)] for _ in range(10000)]

    # Generating parameters for 10000 squares
    squares = [rd.randint(1, 200) for _ in range(10000)]

    start = time.perf_counter()
    with_threads(trapezoids + rectangles + squares)
    end = time.perf_counter()
    print("Time with threads:", round(end - start, 4), 'second(s).')

    start = time.perf_counter()
    with_processes(trapezoids + rectangles + squares)
    end = time.perf_counter()
    print("Time with processes:", round((end - start), 4), "second(s)")

    with_mixed(trapezoids + rectangles + squares)
