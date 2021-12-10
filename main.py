def list_comprehension_exercise_1():
    return [num for num in range(11)]

def list_comprehension_exercise_2():
    return [num for num in range(22) if num % 2 == 0 or num % 3 == 0]

def list_comprehension_exercise_3():
    return [num for num in range(-5, 32) if num % 2 != 0 and num % 5 != 0]

def list_comprehension_exercise_4():
    return [num**2 for num in range(11)]

def list_comprehension_exercise_5(sentence):
    return [letter for letter in sentence if letter.isupper()]

def list_comprehension_exercise_6(sentence):
    return [word for word in sentence.split(' ') if word[0] in 'r' and len(word) > 3 ]
