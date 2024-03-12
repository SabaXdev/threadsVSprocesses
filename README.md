Trapezoid, Rectangle, and Square Area Calculator

This Python script provides classes to calculate the areas of trapezoids, rectangles, and squares. It includes methods for sequential computation, multithreading, multiprocessing, and a mixed approach using both threads and processes.
How to Use

    Install Python: Ensure you have Python installed on your system. You can download it from the official Python website.

    Clone the Repository: Clone this repository to your local machine using the following command:

    bash

git clone https://github.com/your-username/your-repository.git

Navigate to the Directory: Move to the directory containing the cloned repository:

bash

cd your-repository

Run the Script: Execute the Python script to perform area calculations:

bash

    python area_calculator.py

Classes and Methods

    Trapezoid: Represents a trapezoid shape with methods to calculate its area.
    Rectangle: Represents a rectangle shape, which is a subclass of Trapezoid.
    Square: Represents a square shape, which is a subclass of Rectangle.

Functions

    trapezoid_area(arr): Calculates the area of each trapezoid in the provided array.
    rectangle_area(arr): Calculates the area of each rectangle in the provided array.
    square_area(arr): Calculates the area of each square in the provided array.
    with_threads(arr): Computes areas using multithreading.
    with_processes(arr): Computes areas using multiprocessing.
    with_mixed(arr): Computes areas using a mixed approach of threads and processes.

Sample Usage

python

# Generating parameters for 10000 trapezoids
trapezoids = [[rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200)] for _ in range(10000)]

# Generating parameters for 10000 rectangles
rectangles = [[rd.randint(1, 200), rd.randint(1, 200)] for _ in range(10000)]

# Generating parameters for 10000 squares
squares = [rd.randint(1, 200) for _ in range(10000)]

# Sequential computation
with_regular(trapezoids + rectangles + squares)

# Multithreading
with_threads(trapezoids + rectangles + squares)

# Multiprocessing
with_processes(trapezoids + rectangles + squares)

# Mixed approach
with_mixed(trapezoids + rectangles + squares)

Dependencies

    Python 3.x
    concurrent.futures

License

This project is licensed under the MIT License - see the LICENSE file for details.
