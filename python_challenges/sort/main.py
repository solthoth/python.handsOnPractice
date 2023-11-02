def word_sort(value: str):
    words = value.split(" ")
    wordDict = {}
    for word in words:
        key = word.lower()
        wordDict[key] = word
    sortedWords = dict(sorted(wordDict.items()))
    return " ".join(sortedWords.values())

def word_sort2(value: str):
    return " ".join(sorted(value.split(), key=str.casefold))

def test(value: str, answer: str):
    sorted = word_sort(value)
    print(sorted)
    assert sorted == answer

def test2(value: str, answer: str):
    sorted = word_sort2(value)
    print(sorted)
    assert sorted == answer

def main():
    test("Test data", "data Test")
    test("banana ORANGE apple", "apple banana ORANGE")
    test2("banana ORANGE apple", "apple banana ORANGE")

if __name__ == "__main__":
    main()