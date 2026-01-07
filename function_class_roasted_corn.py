
# Question 1
def calculate_string_length(string):
    length = len(string)
    return length


# Question 2
def first_and_last_two(string):
    if len(string) < 2:
        return ''
    
    first_two = string[0] + string[1]
    last_two = string[-2] + string[-1]
    
    result = first_two + last_two
    return result


# Question 3
def add_ing_or_ly(string):
    if len(string) < 3:
        return string
    
    if string[-3:] == 'ing':
        return string + 'ly'
    else:
        return string + 'ing'


# Question 4 
def find_longest_word(words):
    longest = words[0]
    
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    length = len(longest)
    
    return longest, length


# Question 5 
def remove_odd_indices(string):
    result = ''
    
    for i in range(len(string)):
        if i % 2 == 1:
            result = result + string[i]
    
    return result


# Question 6
def find_minimum(numbers):
    minimum = numbers[0]
    
    for num in numbers:
        if num < minimum:
            minimum = num
    
    return minimum


# Question 7 
def find_maximum(numbers):
    maximum = numbers[0]
    
    for num in numbers:
        if num > maximum:
            maximum = num
    
    return maximum


# Question 8 
def repeat_string(string, number):
    if type(number) == float:
        if number != int(number):
            return string
    
    result = ''
    for i in range(int(number)):
        result = result + string
    
    return result


# Question 9 
def square_list_elements(numbers):
    squared = []
    
    for num in numbers:
        square = num * num
        squared.append(square)
    
    return squared


# Question 10
def sum_of_squares(numbers):
    total = 0
    
    for num in numbers:
        square = num * num
        total = total + square
    
    return total
