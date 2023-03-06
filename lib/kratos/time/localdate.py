from dataclasses import dataclass, field
from typing import TypeVar

from datetime import date

TLocalDate = TypeVar("TLocalDate", bound="LocalDate")


@dataclass
class LocalDate:
    year: int
    month: int
    day: int
    inner_date: date = field(init=False, repr=False)

    def __post_init__(self):
        self.inner_date = date(self.year, self.month, self.day)

    @classmethod
    def today(cls) -> TLocalDate:
        today = date.today()
        return LocalDate(today.year, today.month, today.day)

    @classmethod
    def of(cls, one_date: date) -> TLocalDate:
        return LocalDate(one_date.year, one_date.month, one_date.day)

