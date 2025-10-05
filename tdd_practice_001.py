def increment_string(string):
    """
       Description: Increment the numeric suffix of a string.

    If the string ends with a number, increment that number by 1.
    If the string does not end with a number, append 1.
    Examples:

    "foo" -> "foo1"
    "foobar23" -> "foobar24"
    "foo0042" -> "foo0043"
    "foo9" -> "foo10"
    """

    num = ""
    if len(string) == 0 or not string[-1].isdigit():
        return string + str(1)
    for i in range(len(string)):
        if string[len(string) - 1 - i].isalpha():
            break
        idx = len(string) - 1 - i
        num += string[len(string) - 1 - i]
    return f"{string[:idx]}{int(num[::-1]) + 1:0{len(num)}d}"


def count_letters(string):
    """
       Description: Count the occurrences of each letter in a string.

    Example::

    "aba" -> {"a": 2, "b": 1}
    """

    occurance = {}
    for char in string:
        char = char.lower()
        occurance[char] = string.lower().count(char)
    return occurance


def sum_consecutives(s):
    """
    Description: Return a list of sums of each consecutive pair in a list.

    Example:

    [1, 2, 3] -> [3, 5]  # 1+2=3, 2+3=5
    """
    sum = []
    for idx, num in enumerate(s):
        if idx + 1 < len(s) and not (is_number(num) and is_number(s[idx + 1])):
            raise ValueError("The list must be numerical list.")
        if idx + 1 < len(s):
            sum.append(num + s[idx + 1])
    return sum


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def count_unique(text):
    '''
    Description: Count the number of unique words in a string.

    Should raise a ValueError if the input is not a string.

    Example:

    "no example ;)"'''

    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    words = text.lower().split()
    # unique_words = set(words)
    unique_words = []
    for word in words:
        if len(word) > 1 and word not in unique_words and word.isalpha():
            unique_words.append(word)
    return len(unique_words)
