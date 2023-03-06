import unittest

from datetime import date
from lib.kratos.time.localdate import LocalDate


class TestLocalDate(unittest.TestCase):
    def test_today(self):
        today = LocalDate.today()
        self.assertEqual(today.inner_date, date.today())

    def test_of_instance(self):
        single_date = date(2023, 3, 6)
        instance = LocalDate.of(single_date)

        self.assertEqual(instance, LocalDate(2023, 3, 6))

