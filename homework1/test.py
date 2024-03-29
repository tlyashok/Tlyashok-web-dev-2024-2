import subprocess

import pytest

INTERPRETER = 'python'


def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()


test_data = {
    'python_if_else': [
        ('1', 'Weird'),
        ('4', 'Not Weird'),
        ('3', 'Weird'),
        ('6', 'Weird'),
        ('22', 'Not Weird')
    ],
    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10', '5'], ['15', '5', '50'])
    ],
    'division': [
        (['6', '3'], ['2', '2.0']),
        (['7', '2'], ['3', '3.5']),
        (['10', '0'], ['Деление на ноль невозможно.'])
    ],
    'loops': [
        (['3'], ['0', '1', '4']),
        (['0'], ['']),
        (['-5'], [''])
    ],
    'print_function': [
        (['5'], ['12345']),
        (['1'], ['1']),
        (['0'], [''])
    ],
    'second_score': [
        (['5', '2 3 6 6 5'], ['5']),
        (['6', '2 3 6 6 5 5'], ['5']),
        (['1', '10'], ['']),
        (['4', '-2 -3 -6 -5'], ['-3'])
    ],
    'nested_list': [
        (['1', 'John', '50'], ['']),
        (['5', 
          'Harry', '37.21', 
          'Berry', '37.21', 
          'Tina', '37.2', 
          'Akriti', '41', 
          'Harsh', '39'], ['Berry', 'Harry']),
        (['3', 'John', '50', 'Jane', '60', 'Alex', '60'], ['Alex', 'Jane'])
    ],
    'lists': [
        (['2', 'insert 0 1', 'print'], ['[1]']),
        (['4', 'insert 0 1', 'insert 1 2', 'remove 1', 'print'], ['[2]']),
        (['2', 'append 1', 'print'], ['[1]']),
        (['5', 'append 3', 'append 1', 'append 2', 'sort', 'print'], ['[1, 2, 3]']),
        (['6', 'append 1', 'append 2', 'append 3', 'pop', 'reverse', 'print'], ['[2, 1]'])
    ],
    'swap_case': [
        (['Www.MosPolytech.ru'], ['wWW.mOSpOLYTECH.RU']),
        (['Pythonist 2'], ['pYTHONIST 2']),
    ],
    'split_and_join': [
        (['hello world'], ['hello-world']),
        (['this is a string'], ['this-is-a-string']),
        (['this is a word'], ['this-is-a-word']),
    ],
    'max_word': [
        ([''], ['сосредоточенности']),
    ],
    'price_sum': [
        ([''], ['6842.84 5891.06 6810.90'])
    ],

    'anagram': [
        (['привет', 'привте'], ['YES']),
        (['а', 'a'], ['NO']),
        (['hello', 'helo'], ['NO']),
        (['hi', 'ih'], ['YES']),
    ],
    'metro': [
        ((['3', '10 20', '15 30', '25 40', '20']), ['2'])
    ]
}


def test_hello_world():
    assert run_script('hello_world.py') == 'Hello, world!'


@pytest.mark.parametrize('input_data, expected', test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data]) == expected


@pytest.mark.parametrize('input_data, expected',
                         test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected


@pytest.mark.parametrize('input_data, expected',
                         test_data['division'])
def test_division(input_data, expected):
    assert run_script('division.py', input_data).split('\n') == expected


@pytest.mark.parametrize('input_data, expected',
                         test_data['loops'])
def test_loops(input_data, expected):
    assert run_script('loops.py', input_data).split('\n') == expected


@pytest.mark.parametrize('input_data, expected',
                         test_data['print_function'])
def test_print_function(input_data, expected):
    assert run_script('print_function.py', input_data).split('\n') == expected


@pytest.mark.parametrize('input_data, expected',
                         test_data['second_score'])
def test_second_score(input_data, expected):
    assert run_script('second_score.py', input_data).split('\n') == expected


@pytest.mark.parametrize('input_data, expected',
                         test_data['nested_list'])
def test_nested_list(input_data, expected):
    assert run_script('nested_list.py', input_data).split('\n') == expected


@pytest.mark.parametrize('input_data, expected',
                         test_data['lists'])
def test_lists(input_data, expected):
    assert run_script('lists.py', input_data).split('\n') == expected


@pytest.mark.parametrize('input_data, expected',
                         test_data['swap_case'])
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', input_data).split('\n') == expected


@pytest.mark.parametrize('input_data, expected',
                         test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', input_data).split('\n') == expected


@pytest.mark.parametrize('input_data, expected',
                         test_data['max_word'])
def test_max_word(input_data, expected):
    assert run_script('max_word.py', input_data).split('\n') == expected


@pytest.mark.parametrize('input_data, expected',
                         test_data['price_sum'])
def test_price_sum(input_data, expected):
    assert run_script('price_sum.py', input_data).split('\n') == expected


@pytest.mark.parametrize('input_data, expected',
                         test_data['anagram'])
def test_anagram(input_data, expected):
    assert run_script('anagram.py', input_data).split('\n') == expected


@pytest.mark.parametrize('input_data, expected',
                         test_data['metro'])
def test_metro(input_data, expected):
    assert run_script('metro.py', input_data).split('\n') == expected