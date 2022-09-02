import random
from typing import Optional, List


class ListRandom:
    _inner_list: Optional[list[int]] = []

    def __init__(self, *, start: Optional[int] = 0, end: Optional[int] = 10, count: Optional[int] = 10):
        for i in range(count):
            self._inner_list.append(random.randint(start, end))


    @property
    def all_digit_is_odd(self) -> bool:
        is_odd = True

        for digit in self._inner_list:
            is_odd = is_odd and not (digit % 2)

            if not is_odd:
                break

        return is_odd

    def digits_more(self, digit: int) -> List[int]:
        _temp_list = []
        for i in self._inner_list:
            if i > digit:
                _temp_list.append(i)
        return _temp_list

    def print_list(self) -> None:
        print(self._inner_list)

    def all_digit_is_max(self) -> bool:
        print(max(self._inner_list))

    def all_digit_is_min(self) -> bool:
        print(min(self._inner_list))

    def all_digit_is_sred(self) -> bool:
        print(sum(self._inner_list)/10)