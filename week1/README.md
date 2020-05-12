## Структурное программирование

### Стиль кода в языке Python

**Внешний вид кода:**
* Юникод, формат UTF-8
* Переменные, функции, комментарии и т.д в ascii
* Не смешивать табуляцию и пробелы (желательно пробелы)

**Пробелы**

Окружать операторы одним пробелом с каждой стороны:
* присваивание (=, +=, -= и т.п)
* сравнения (==, <, >, !=, in, not in, is, is not)
* логические операторы (and, or, not)


### Соглашение об именах

* mymodule - модуль или пакет
* UserClassName - класс
* ExceptionsAreAlsoClasses - исключение
* function_name - функция или метод
* variable_name - переменная или открытый атрибут класса
* GLOBAL_CONSTANT - константа уровня модуля

### Структурное программирование

Методолгоия, облегчающая проектирование больших программ
**Принципы:**
* Отказаться от использования goto
* Строить программу из вложенных конструкций: последовательность, ветвление, цикл
* Оформлять повторяющиеся фрагменты программы в виде функций
* Разработка программы ведется пошшагово, методом "сверху-вниз"

## Тестирование
**Тестирование(Quality Control)** - это:
* проверка соответствия между реальным поведением программы и ее ожидаемым поведением
* на конеччном наборе тестов, выбранных определенным образом

**Классификация тестирования по масштабу:**
* модульное тестирование (юнит-тестирование):
  - тестирование отдельных операций, методов, функций

* интеграционное тестирование: 
  - проверка, ччто модули взаимодействуют друг с другом корректно
  
* системное тестирование: 
  - тестирование на уровне пользовательского интерфейса
  
### Программирование по контракту

Библиотека PyContracts используетя для проектирования по контракту. 
Описание обязательств через параметры декоратора: 
```python
from contracts import contract


@contract(a='int,>0',
          b='list[N],N>0',
          returns='list[N]')
def my_func(a, b):
    pass


my_func(a=-1, b=[-1, 0])
```

### Бибилотека doctest

Данная библиотека используется для добавления запускающихся тестов в документ строку
```python
class MyClass:

    def __init__(self, x):
        self.x = x

    def custom_is_digit(self) -> bool:
        """
        :param self:
        :return: True if self.x is digit else False
        >>> MyClass("123").custom_is_digit()
        True
        >>> MyClass("abc").custom_is_digit()
        False
        """
        return not self.x.isdigit()


if __name__ == "__main__":
    import doctest
    doctest.testmod()

```

### Библиотека unittest

**Инструментарий библиотеки:**
1) Test case — тестовый случай, базовая единица тестирования.
2) Test fixture — среда исполнения теста. Включает подготовку к тестированию и последующее обнуление данных, используемых в тестовом случае.
3) Test suite — набор тестовых случаев.
4) Test runner — группа запуска тестов. Это множество классов, связанных с запуском и представлением тестов.

**Тестовый случай (test case)**
```python
import unittest

class MyTest(unittest.TestCase):
    def test_usage(self):
        self.assertEqual(2+2, 4)
```

Правила для написания тестовых классов: 
1) класс тестового случая — потомок unittest.TestCase;
2) тестирующий метод начинается со слова «test»;
3) для проверки утверждения используется метод self.assertEqual().

**Выделение подслучая**
Для выделения конкретной ситуации, в рамках которой произошла ошибка, удобно использовать метод self.subTest():
```python
import unittest


def sort_algorithm(A: list):
    pass  # FIXME


def is_not_in_descending_order(a):
    """
    Check if the list a is not descending (means "rather ascending")
    """
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True

class TestSort(unittest.TestCase):
    def test_simple_cases(self):
        cases = ([1], [], [1, 2], [1, 2, 3, 4, 5], 
                 [4, 2, 5, 1, 3], [5, 4, 4, 5, 5],
                 list(range(1, 10)), list(range(9, 0, -1)))
        for b in cases:
            with self.subTest(case=b):
                a = list(b)
                sort_algorithm(a)
                self.assertCountEqual(a, b)  # контейнеры равны с точностью до порядка элементов
                self.assertTrue(is_not_in_descending_order(a))
```

**Тестирование возбуждения исключений**

Для проверки корректного выброса исключений используется метод assertRaises
```python
import unittest


def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)


class ExceptionTest(unittest.TestCase):
    def test_raises(self):
        self.assertRaises(ValueError, fib, -1)


if __name__=='__main__':
    unittest.main()
```

