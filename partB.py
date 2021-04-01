import random


class Point:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def get_distance(self, other_point):
        diff_x = (self.get_x() - other_point.get_x()) ** 2
        diff_y = (self.get_y() - other_point.get_y()) ** 2
        return (diff_x + diff_y) ** 0.5

    def get_vertices(self):
        list1 = []
        list1.append(self.get_x())
        list1.append(self.get_y())
        return list1

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def __str__(self):
        return "Point[" + str(self.get_x()) + "," + str(self.get_y()) + "]"


class Rectangle:

    def __init__(self, list: list):
        self._width = list[0]
        self._height = list[1]
        self._point = list[2]

    def get_area(self):
        return self.get_width() * self.get_height()

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_point(self):
        return self._point

    def get_diag_length(self):
        """
        sqrt(a^2 + b^2)
        """
        diag = (self.get_height() ** 2 + self.get_width() ** 2) ** 0.5
        return diag

    def add_value_height(self, height_to_add: float):
        self._height += height_to_add

    def add_value_width(self, width_to_add: float):
        self._width += width_to_add

    def __str__(self):
        return "Rectangle: " + str(self.get_point()) + " Width: " + str(self.get_width()) + " Height: " + str(self.get_height()) + " Area: " + str(self.get_area())

    def get_border_points(self):
        border_points = []

        x1 = self.get_point().get_x()
        y1 = self.get_point().get_y()

        x2 = x1 + self.get_width()
        y2 = y1

        x3 = x1 + self.get_width()
        y3 = y1 + self.get_height()

        x4 = x1
        y4 = y1 + self.get_height()

        border_points.append(Point(x1, y1))
        border_points.append(Point(x2, y2))
        border_points.append(Point(x3, y3))
        border_points.append(Point(x4, y4))

        return border_points

    def __gt__(self, other):
        return self.get_area() > other.get_area()


# Constants for triangle vertex
A = 0
B = 1
C = 2


class Triangle:

    def __init__(self, point_a: Point, point_b: Point, point_c: Point):
        self._vertices = []
        self._vertices.append(point_a)
        self._vertices.append(point_b)
        self._vertices.append(point_c)

    def get_vertices(self):
        return self._vertices

    def get_area(self):
        """
        Area By Heron Formula
        """
        semiperimeter = self._get_semiperimeter()
        diff_a = (semiperimeter - self._get_edge(A))
        diff_b = (semiperimeter - self._get_edge(B))
        diff_c = (semiperimeter - self._get_edge(C))
        area = (semiperimeter * diff_a * diff_b * diff_c) ** 0.5

        return area

    def get_circumence(self):
        distance_ab = self._vertices[A].get_distance(self._vertices[B])
        distance_bc = self._vertices[B].get_distance(self._vertices[C])
        distance_ca = self._vertices[C].get_distance(self._vertices[A])
        return distance_ab + distance_bc + distance_ca

    def __str__(self):
        return "Triangle: (A)" + str(self._vertices[A]) + " (B)" + str(self._vertices[B]) + " (C)" + str(
            self._vertices[C]) + " Circumference: " + str(self.get_circumence()) + " Area: " + str(self.get_area())

    def _get_triangle_base(self):
        base_bc = self._get_edge(A)
        return base_bc

    def _get_edge(self, edge):
        return self._vertices[(edge+1) % 3].get_distance(self._vertices[(edge+2) % 3])

    def _get_semiperimeter(self):
        return self.get_circumence() / 2

    def __gt__(self, other):
        return self.get_area() > other.get_area()


def selection_sort(shapes: list):
    n = len(shapes)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if shapes[min_index] > shapes[j]:
                min_index = j

        swap(shapes, min_index, i)


def bubble_sort(shapes: list):
    n = len(shapes)
    for i in range(n):
        for j in range(n - 1 - i):
            if shapes[j].get_area() > shapes[j+1].get_area():
                swap(shapes, j, j+1)


def swap(arr: list, a: int, b: int):
    arr[a], arr[b] = arr[b], arr[a]


def create_random_triangle_list(num_of_objects, min, max):
    triangles = []
    for i in range(num_of_objects):
        point_a = create_random_point(min, max)
        point_b = create_random_point(min, max)
        point_c = create_random_point(min, max)
        triangle = Triangle(point_a, point_b, point_c)
        triangles.append(triangle)

    return triangles


def create_random_point(min, max):
    x = random.randint(min, max)
    y = random.randint(min, max)

    return Point(x, y)


def create_random_rectangle_list(num_of_objects, min, max):
    rectangles = []
    for i in range(num_of_objects):
        width = random.randint(min, max)
        height = random.randint(min, max)
        point = create_random_point(min, max)
        rectangle = Rectangle([width, height, point])
        rectangles.append(rectangle)

    return rectangles


def print_list(list: list):
    for item in list:
        print(str(item))


def add_to_sorted(sorted_list, to_add):
    high = len(sorted_list)
    low = 0
    _insert_to_sorted(sorted_list, to_add, low, high)


def _insert_to_sorted(sorted_list, to_add, low, high):
    while low < high:
        mid = (low + high) // 2
        if sorted_list[mid] > to_add:
            high = mid
        else:
            low = mid+1

    sorted_list.insert(low, to_add)


def add_rectangle(sorted_list, rectangle_params):
    rectangle = Rectangle(rectangle_params)
    add_to_sorted(sorted_list, rectangle)


# Constans for createing random shapes
NUM_OF_SHAPES = 5
MIN_POINT_VAL = 1
MAX_POINT_VAL = 100


def run():
    rectangles = create_random_rectangle_list(NUM_OF_SHAPES, MIN_POINT_VAL, MAX_POINT_VAL)
    triangles = create_random_triangle_list(NUM_OF_SHAPES, MIN_POINT_VAL, MAX_POINT_VAL)

    print('\nBefore sorting rectangles:')
    print_list(rectangles)
    selection_sort(rectangles)
    print('\nAfter sorting rectangles: ')
    print_list(rectangles)

    print('\nBefore sorting triangles:')
    print_list(triangles)
    bubble_sort(triangles)
    print('\nAfter sorting triangles: ')
    print_list(triangles)

    to_add = create_random_rectangle_list(1, MIN_POINT_VAL, MAX_POINT_VAL)
    print('\nCreated rectangle: ')
    print(str(to_add[0]))
    new_rectangle_params = [to_add[0].get_width(), to_add[0].get_height(), to_add[0].get_point()]
    print('\nAdding to sorted list...')
    add_rectangle(rectangles, new_rectangle_params)
    print('\nPrinting new rectangle list: ')
    print_list(rectangles)


run()
