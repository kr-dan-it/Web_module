import unittest
import utils as utils
import pytest

# class TestAddition(unittest.TestCase):
#
#     def test_addition(self):
#         self.assertEqual(add(4, 5), 9) # what we pass in / what we expect
#         self.assertEqual(add(10, -7), 3)
#         self.assertEqual(add(-1, 1), 0)
#         self.assertEqual(add(8, 4), 12)
#
# class TestSubtraction(unittest.TestCase):
#
#     def test_subtraction(self):
#         self.assertEqual(subtract(10, 5), 5)
#         self.assertEqual(subtract(6, -3), 9)
#
# if __name__=="__main__":
#     unittest.main()

# def test_addition():
#     assert add(10, 5) == 15
#     assert add(7, -3) == 4
#     assert add(6, -7) == -1
#
# def test_mult():
#     assert multiply(3, 4) == 13
#     assert multiply(0, 18) == 1

# def test_add_positive_numbers():
#     assert add(2, 7) == 9
#
# def test_add_negative_numbers():
#     assert add(-3, -6) == -9
#
# def test_add_zero():
#     assert add(0, 8) == 8
#     assert add(-4, 0) == -4
#
# def test_add_floats():
#     assert add(2.5, 3.5) == 6.0
#     assert add(4, 4.4) == 8.4
#     assert add(0.1, 0.3) == pytest.approx(0.4)
#
# def test_polindrome():
#     assert utils.is_polindrome("madam") == True
#     assert utils.is_polindrome("Race car") == True
#     assert utils.is_polindrome("The big brown fox jumps over the lazy dog") == False
#     assert utils.is_polindrome("BreAD") == False

# @pytest.mark.parametrize("a, b, expected",
#                          [
#                              (2, 3, 6),
#                              (-1, 5, -5),
#                              (-3, -7, 21),
#                              (0, 10, 0),
#                              (2.5, 2.5, 6.25)
#                          ])
#
# def test_mult_with_params(a, b, expected):
#     assert multiply(a, b) == expected
#
# @pytest.fixture
# def tmp_file(tmp_path):
#     file_path = tmp_path / "test_data.txt"
#     file_path.write_text("It's test data")
#     print(f"Created Fixture for temp file ({file_path})")
#     yield file_path
#     print(f"End Fixture, deleted file ({file_path})")
#
# def test_read_temp_file(tmp_file):
#     print(f"Read from file {tmp_file}")
#     content = tmp_file.read_text()
#     assert "test" in content
#     assert len(content) > 0
#
# def test_write_to_tmp_file(tmp_file):
#     print(f"Write to file {tmp_file}")
#     tmp_file.write_text("New data from test_write")
#     content = tmp_file.read_text()
#     assert "New data from test_write" in content

# - Тест для коректної знижки (наприклад, 100, 10 -> 90.0)
# - Тест для 0% знижки
# - Тест для 100% знижки
# - Тест, що перевіряє виняток `ValueError` при некоректному відсотку знижки (наприклад, -5% або 105%)

# def test_normal_discount():
#     assert utils.calculate_discount(100, 10) == 90.0
#
# def test_discount_zero():
#     assert utils.calculate_discount(100, 0) == 100.0
#
# def test_discount_hundred():
#     assert utils.calculate_discount(100, 100) == 0.0
#
# def test_discount_value_error():
#     with pytest.raises(ValueError):
#         assert utils.calculate_discount(100, -5)
#         assert utils.calculate_discount(100, 105)
#
# def test_negative_price():
#     with pytest.raises(ValueError):
#         assert utils.calculate_discount(-10, 5)

# @pytest.mark.parametrize("first_name, last_name, expected",
#                          [
#                              ("John", "Foo", "Foo, John"),
#                              ("Alice", "Bar", "Bar, Alice")
#                          ])
# def test_full_name(first_name, last_name, expected):
#     assert utils.format_user_name(first_name, last_name) == expected
#
# @pytest.mark.parametrize("first_name, last_name, expected",
#                          [
#                              ("John  ", "Foo ", "Foo, John"),
#                              ("Alice ", "Bar  ", "Bar, Alice")
#                          ])
# def test_name_with_spaces(first_name, last_name, expected):
#     assert utils.format_user_name(first_name, last_name) == expected
#
# @pytest.mark.parametrize("first_name, last_name, expected",
#                          [
#                              ("", "Foo", "Foo"),
#                              ("Alice", "", "Alice")
#                          ])
# def test_name_with_spaces(first_name, last_name, expected):
#     assert utils.format_user_name(first_name, last_name) == expected
#
# def test_nameless_name():
#     with pytest.raises(ValueError):
#         assert utils.format_user_name("", "")

