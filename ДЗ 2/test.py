import os
import sys
import pytest
import math
import time
import tempfile

from fact import *
from show_employee import *
from sum_and_sub import *
from process_list import *
from my_sum import *
from my_sum_argv import *
from files_sort import *
from file_search import *
from email_validation import *
from fibonacci import *
from average_scores import compute_average_scores
from plane_angle import *
from phone_number import *
from people_sort import *
from complex_numbers import *
from circle_square_mk import *
from log_decorator import *

@pytest.mark.parametrize(
        "n, res", 
        [
            (1, 1),
            (2, 2),
            (3, 6),
            (4, 24),
            (5, 120),
        ])
def test_fact(n, res):
    assert fact_rec(n) == res
    assert fact_it(n) == res

@pytest.mark.parametrize(
        "name, salary, expected_result", 
[
    ("Иванов Иван Иванович", 30000, "Иванов Иван Иванович: 30000 ₽"),
    ("Петров Петр Петрович", 50000, "Петров Петр Петрович: 50000 ₽"),
    ("Сидоров Сидор Сидорович", 100000, "Сидоров Сидор Сидорович: 100000 ₽"),
])
def test_show_employee(name, salary, expected_result):
    assert show_employee(name, salary) == expected_result

@pytest.mark.parametrize("a, b, expected_sum, expected_sub", [
    (5, 3, 8, 2),
    (10, 7, 17, 3),
    (-3, 8, 5, -11),
])
def test_sum_and_sub(a, b, expected_sum, expected_sub):
    result_sum, result_sub = sum_and_sub(a, b)
    assert result_sum == expected_sum
    assert result_sub == expected_sub

@pytest.mark.parametrize("arr, expected_result", [
    ([1, 2, 3, 4, 5], [1, 4, 27, 16, 125]),
    ([2, 3, 4, 5, 6], [4, 27, 16, 125, 36]),
    ([], []),
])
def test_process_list(arr, expected_result):
    assert process_list(arr) == expected_result

@pytest.mark.parametrize("arr, expected_result", [
    ([1, 2, 3, 4, 5], [1, 4, 27, 16, 125]),
    ([2, 3, 4, 5, 6], [4, 27, 16, 125, 36]),
    ([], []),
])
def test_process_list_gen(arr, expected_result):
    assert list(process_list_gen(arr)) == expected_result

@pytest.mark.parametrize("inputs, expected_output", [
    ((1, 2, 3), 6),
    ((-1, -2, -3), -6),
    ((1, -2, 3), 2),
    ((0, 0, 0), 0),
    ((10, 20, 30, 40), 100),
])
def test_my_sum(inputs, expected_output):
    res = my_sum(*inputs)
    assert res == expected_output

@pytest.mark.parametrize("input_args, expected_output", [
    (["1", "2", "3", "4", "5"], "15.0\n"),
    (["-1", "2", "-3", "4", "-5"], "-3.0\n"),
])
def test_my_sum_argv(input_args, expected_output, monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ["my_sum_argv.py"] + input_args)
    my_sum_argv()
    captured = capsys.readouterr()
    assert captured.out == expected_output

@pytest.mark.parametrize(
        "test_input, expected_output", 
[
    (["a.py", "b.py", "c.py", "a.txt", "b.txt", "c.txt"], 
"""a.py
b.py
c.py
a.txt
b.txt
c.txt
"""),
    (["c.py", "b.py", "a.py", "c.txt", "b.txt", "a.txt"], 
"""a.py
b.py
c.py
a.txt
b.txt
c.txt
"""),
    (["b.py", "a.txt", "c.txt", "a.py", "b.txt", "c.py"], 
"""a.py
b.py
c.py
a.txt
b.txt
c.txt
"""),
])
def test_list_files(tmpdir, test_input, expected_output, capsys):
    test_dir = tmpdir.mkdir("test_directory")
    for filename in test_input:
        open(os.path.join(test_dir, filename), 'a').close()
    list_files(test_dir)
    captured = capsys.readouterr()
    output = captured.out
    assert output == expected_output
    test_dir.remove()

def test_search_file(capsys):
    test_content = ["Line 1\n", "Line 2\n", "Line 3\n", "Line 4\n", "Line 5\n"]
    with open('test.txt', 'w') as file:
        file.writelines(test_content)
    
    search_file('test.txt')
    
    captured = capsys.readouterr()
    output = captured.out
    
    assert output == ''.join(test_content)

@pytest.mark.parametrize("email, expected", [
    ("example@example.com", True),  # Корректный адрес
    ("example123@example.com", True),  # Корректный адрес
    ("example-123@example.com", True),  # Корректный адрес
    ("example_123@example.com", True),  # Корректный адрес
    ("example@example", False),  # Некорректный адрес (нет расширения)
    ("example@.com", False),  # Некорректный адрес (нет имени сайта)
    ("example.com", False),  # Некорректный адрес (нет символа @)
    ("example@website", False),  # Некорректный адрес (нет расширения)
    ("@website.com", False),  # Некорректный адрес (нет имени пользователя)
    ("example@website.longextension", False),  # Некорректный адрес (длинное расширение)
])
def test_fun(email, expected):
    assert fun(email) == expected

@pytest.mark.parametrize("n, expected", [
    (1, [0]),
    (2, [0, 1]),
    (5, [0, 1, 1, 8, 27]),
    (10, [0, 1, 1, 8, 27, 125, 512, 2197, 9261, 39304]),
])
def test_fibonacci(n, expected):
    assert list(map(cube, fibonacci(n))) == expected

@pytest.mark.parametrize("scores, expected", [
    ([(89, 90, 78, 93, 80), (90, 91, 85, 88, 86), (91, 92, 83, 89, 90.5)], (90.0, 91.0, 82.0, 90.0, 85.5)),
    ([(70, 80, 90), (60, 70, 80), (50, 60, 70), (40, 50, 60)], (55.0, 65.0, 75.0)),
    ([(100, 100, 100), (0, 0, 0), (50, 50, 50)], (50.0, 50.0, 50.0)),
])
def test_compute_average_scores(scores, expected):
    assert compute_average_scores(scores) == expected

@pytest.fixture
def point_a():
    return Point(0, 0, 0)

@pytest.fixture
def point_b():
    return Point(1, 1, 1)

@pytest.fixture
def point_c():
    return Point(1, 0, 0)

@pytest.fixture
def point_d():
    return Point(0, 1, 0)

def test_point_subtraction(point_a, point_b):
    result = point_b - point_a
    assert result.x == 1
    assert result.y == 1
    assert result.z == 1

def test_point_dot(point_a, point_b):
    result = point_a.dot(point_b)
    assert result == 0

def test_point_cross(point_a, point_b):
    result = point_a.cross(point_b)
    assert result.x == 0
    assert result.y == 0
    assert result.z == 0

def test_point_absolute(point_a):
    result = point_a.absolute()
    assert result == 0.0

@pytest.mark.parametrize("input_numbers, expected_output", [
    (['07895462130', '89875641230', '9195969878'], 
     ['+7 (789) 546-21-30', '+7 (919) 596-98-78', '+7 (987) 564-12-30']),
    (['81234567890', '89123456789'], 
     ['+7 (123) 456-78-90', '+7 (912) 345-67-89']),
    (['71234567890'], 
     ['+7 (123) 456-78-90'])
])
def test_sort_phone(input_numbers, expected_output):
    result = sort_phone(input_numbers)
    assert result == expected_output

import pytest

@pytest.mark.parametrize("input_data, expected_output", [
    (
        [
            ["Mike", "Thomson", "20", "M"],
            ["Robert", "Bustle", "32", "M"],
            ["Andria", "Bustle", "30", "F"]
        ],
        [
            "Mr. Mike Thomson",
            "Ms. Andria Bustle",
            "Mr. Robert Bustle"
        ]
    )
])
def test_name_format(input_data, expected_output):
    result = name_format(input_data)
    assert list(result) == expected_output

@pytest.mark.parametrize("input_complex1, input_complex2, expected_output", [
    ((2, 1), (5, 6), [
        "7.00+7.00i",
        "-3.00-5.00i",
        "4.00+17.00i",
        "0.26-0.11i",
        "2.24+0.00i",
        "7.81+0.00i"
    ]),

])
def test_complex_operations(input_complex1, input_complex2, expected_output):
    c = Complex(*input_complex1)
    d = Complex(*input_complex2)
    result = [str(x) for x in [c + d, c - d, c * d, c / d, c.mod(), d.mod()]]
    assert result == expected_output

@pytest.mark.parametrize("radius, num_experiments, tolerance", [
    (1, 1000, 0.2),  # Пример с малым числом экспериментов
    (1, 10000, 0.3),  # Пример с умеренным числом экспериментов
    (1, 100000, 0.2),  # Пример с большим числом экспериментов
])
def test_circle_square_mk(radius, num_experiments, tolerance):
    monte_carlo_square = circle_square_mk(radius, num_experiments)
    true_square = 3.141592653589793 * radius**2
    assert abs(monte_carlo_square - true_square) < tolerance