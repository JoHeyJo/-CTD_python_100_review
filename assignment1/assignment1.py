# Task 1: Hello
def hello():
    return "Hello!"

# Task 2: Greet with a Formatted String


def greet(name):
    return f"Hello, {name}!"


# Task 3: Calculator
def calc(a, b, c="multiply"):
    try:
        if c == "add":
            return a + b
        elif c == "subtract":
            return a - b
        elif c == "multiply":
            return a * b
        elif c == "divide":
            return a / b
        elif c == "modulo":
            return a % b
        elif c == "int_divide":
            return a // b
        elif c == "power":
            return a ** b
    except ZeroDivisionError:
        return ("You can't divide by 0!")
    except TypeError:
        return ("You can't multiply those values!")


# Task 4: Data Type Conversion
def data_type_conversion(value, type):
    try:
        match type:
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "int":
                return int(value)
    except ValueError:
        return (f"You can't convert {str(value)} into a {str(type)}.")


# Task 5: Grading System, Using * args
def grade(*args):
    try:
        total = sum(args)
        percentage = total / len(args)
        if percentage >= 90:
            return "A"
        elif percentage > 79 and percentage < 90:
            return "B"
        elif percentage > 69 and percentage < 80:
            return "C"
        elif percentage > 59 and percentage < 70:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."


# Task 6: Use a For Loop with a Range
def repeat(string, count):
    result = ""
    loops = range(count)
    for loop in loops:
        result += string
    return result


# Task 7: Student Scores, Using ** kwargs
def student_scores(position, **kwargs):
    total = 0
    max = 0
    maxScore = ''
    for key, value in kwargs.items():
        if max < value:
            max = value
            maxScore = key
        total += value
    if position == "mean":
        return total / len(kwargs)
    if position == "best":
        return maxScore


# Task 8: Titleize, with String and List Operations
def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split(" ")
    capitalized_words = []
    for i, word in enumerate(words):
        if word not in little_words or i == 0 or i == len(words) - 1:
            capitalized_words.append(word.capitalize())
        else:
            capitalized_words.append(word)
    capitalized_string = " ".join(capitalized_words)
    return capitalized_string


# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    guessed = ""
    for letter in secret:
        if letter in guess:
            guessed += letter
        else:
            guessed += "_"
    return guessed


# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(string):
    vowels = "aeiou"
    phrase = string.split(" ")
    converted_words = []
    for word in phrase:
        if word[0] in vowels:
            converted_words.append(word + "ay")
        elif word[0] == "q" and word[1] == "u":
            converted_words.append(word[:2] + word[2:] + "ay")
        else:
            converted_words.append(convert_word(word))
    return " ".join(converted_words)

def convert_word(string):
    vowels = "aeiou"
    converted_string = ''
    for i, char in enumerate(string):
        if char not in vowels:
            print(i)
            converted_string = string[i+1:] + string[:i+1] + "ay"
        return converted_string


# pytest -v -x assignment1-test.py
# can use just -x, adding -v lists the passing tests
