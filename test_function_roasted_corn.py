
from function_class_roasted_corn import 
from unittest import TestCase


# Tests for Question 1
class TestCalculateStringLength(TestCase):
    def test_that_semicolon_length_is_9(self):
        length = calculate_string_length('semicolon')
        self.assertEqual(length, 9)
    
    def test_that_empty_string_length_is_0(self):
        length = calculate_string_length('')
        self.assertEqual(length, 0)
    
    def test_that_hello_world_length_is_11(self):
        length = calculate_string_length('hello world')
        self.assertEqual(length, 11)


# Tests for Question 2
class TestFirstAndLastTwo(TestCase):
    def test_that_semicolon_returns_seon(self):
        result = first_and_last_two('semicolon')
        self.assertEqual(result, 'seon')
    
    def test_that_on_returns_onon(self):
        result = first_and_last_two('on')
        self.assertEqual(result, 'onon')
    
    def test_that_single_character_returns_empty(self):
        result = first_and_last_two('o')
        self.assertEqual(result, '')
    
    def test_that_programming_returns_prng(self):
        result = first_and_last_two('programming')
        self.assertEqual(result, 'prng')


# Tests for Question 3
class TestAddIngOrLy(TestCase):
    def test_that_abc_becomes_abcing(self):
        result = add_ing_or_ly('abc')
        self.assertEqual(result, 'abcing')
    
    def test_that_string_becomes_stringly(self):
        result = add_ing_or_ly('string')
        self.assertEqual(result, 'stringly')
    
    def test_that_on_remains_on(self):
        result = add_ing_or_ly('on')
        self.assertEqual(result, 'on')
    
    def test_that_running_becomes_runningly(self):
        result = add_ing_or_ly('running')
        self.assertEqual(result, 'runningly')


# Tests for Question 4
class TestFindLongestWord(TestCase):
    def test_that_breakfast_is_longest(self):
        words = ['welcome', 'out', 'weather', 'mobile', 'breakfast', 'journey']
        longest, length = find_longest_word(words)
        self.assertEqual(longest, 'breakfast')
        self.assertEqual(length, 9)
    
    def test_that_single_word_returns_itself(self):
        words = ['hello']
        longest, length = find_longest_word(words)
        self.assertEqual(longest, 'hello')
        self.assertEqual(length, 5)
    
    def test_that_programming_is_longest(self):
        words = ['programming', 'hi', 'bye']
        longest, length = find_longest_word(words)
        self.assertEqual(longest, 'programming')
        self.assertEqual(length, 11)


# Tests for Question 5
class TestRemoveOddIndices(TestCase):
    def test_that_semicolon_returns_eioo(self):
        result = remove_odd_indices('semicolon')
        self.assertEqual(result, 'eioo')
    
    def test_that_python_returns_yhn(self):
        result = remove_odd_indices('python')
        self.assertEqual(result, 'yhn')
    
    def test_that_single_character_returns_empty(self):
        result = remove_odd_indices('a')
        self.assertEqual(result, '')
    
    def test_that_numbers_returns_correct_result(self):
        result = remove_odd_indices('0123456789')
        self.assertEqual(result, '13579')


# Tests for Question 6
class TestFindMinimum(TestCase):
    def test_that_minimum_is_2(self):
        minimum = find_minimum([8, 4, 9, 2, 5, 7, 3])
        self.assertEqual(minimum, 2)
    
    def test_that_minimum_at_beginning_works(self):
        minimum = find_minimum([1, 5, 9, 3, 7])
        self.assertEqual(minimum, 1)
    
    def test_that_negative_numbers_work(self):
        minimum = find_minimum([-5, -2, -10, -1])
        self.assertEqual(minimum, -10)
    
    def test_that_single_number_returns_itself(self):
        minimum = find_minimum([42])
        self.assertEqual(minimum, 42)


# Tests for Question 7
class TestFindMaximum(TestCase):
    def test_that_maximum_is_9(self):
        maximum = find_maximum([8, 4, 9, 2, 5, 7, 3])
        self.assertEqual(maximum, 9)
    
    def test_that_maximum_at_end_works(self):
        maximum = find_maximum([2, 4, 6, 8, 10])
        self.assertEqual(maximum, 10)
    
    def test_that_negative_numbers_work(self):
        maximum = find_maximum([-5, -2, -10, -1])
        self.assertEqual(maximum, -1)
    
    def test_that_single_number_returns_itself(self):
        maximum = find_maximum([42])
        self.assertEqual(maximum, 42)


# Tests for Question 8
class TestRepeatString(TestCase):
    def test_that_hello_repeats_3_times(self):
        result = repeat_string('hello', 3)
        self.assertEqual(result, 'hellohellohello')
    
    def test_that_float_returns_original_string(self):
        result = repeat_string('hi', 4.5)
        self.assertEqual(result, 'hi')
    
    def test_that_repeat_once_works(self):
        result = repeat_string('test', 1)
        self.assertEqual(result, 'test')
    
    def test_that_repeat_zero_returns_empty(self):
        result = repeat_string('test', 0)
        self.assertEqual(result, '')


# Tests for Question 9
class TestSquareListElements(TestCase):
    def test_that_list_squares_correctly(self):
        result = square_list_elements([2, 3, 4, 5, 7])
        self.assertEqual(result, [4, 9, 16, 25, 49])
    
    def test_that_single_element_squares(self):
        result = square_list_elements([5])
        self.assertEqual(result, [25])
    
    def test_that_negative_numbers_square(self):
        result = square_list_elements([-2, -3, -4])
        self.assertEqual(result, [4, 9, 16])
    
    def test_that_zero_squares_to_zero(self):
        result = square_list_elements([0, 1, 2])
        self.assertEqual(result, [0, 1, 4])


# Tests for Question 10
class TestSumOfSquares(TestCase):
    def test_that_sum_of_squares_is_103(self):
        result = sum_of_squares([2, 3, 4, 5, 7])
        self.assertEqual(result, 103)
    
    def test_that_single_element_works(self):
        result = sum_of_squares([5])
        self.assertEqual(result, 25)
    
    def test_that_negative_numbers_work(self):
        result = sum_of_squares([-2, -3])
        self.assertEqual(result, 13)
    
    def test_that_empty_list_returns_zero(self):
        result = sum_of_squares([])
        self.assertEqual(result, 0)
