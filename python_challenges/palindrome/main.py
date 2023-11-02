import re
import string
from collections import deque

def is_palindrome(value: str) -> bool:
    value = value.lower().translate(str.maketrans('','',string.punctuation+" "))
    data = deque(value)
    while len(data)>1:
        if data.pop() != data.popleft():
            return False
    return True

def is_palindrome_regex(value: str) -> bool:
    forwards = ''.join(re.findall(r'[a-z]+', value.lower()))
    backwards = forwards[::-1]
    return forwards == backwards

def main():
    value = is_palindrome("taco cat")
    assert value
    value = is_palindrome("hello world")
    assert not value
    value = is_palindrome("Go hang a salami - I'm a lasagna hog.")
    assert value

    value = is_palindrome_regex("taco cat")
    assert value
    value = is_palindrome_regex("hello world")
    assert not value
    value = is_palindrome_regex("Go hang a salami - I'm a lasagna hog.")
    assert value

if __name__ == "__main__":
    main()