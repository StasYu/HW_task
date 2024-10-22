# task 1 github test process

import random
from typing import List
from src.task_1 import is_prime
from src.task_1 import primes
from src.task_1 import checksum
from src.task_1 import pipeline



def test_functions():
    assert is_prime(13) == True
    assert primes(3) == [2, 3, 5]
    assert checksum([1, 2, 6, 24]) == 6012369
    assert pipeline() == 7785816

if __name__ == '__main__':
    test_functions()
