def checkio(words: str) -> bool:

    words = words.split()

    for index in range(len(words) - 2):
        three_words = words[index:index+3]
        if all_words_are_text(three_words):
            return True
    return False


def all_words_are_text(words: list) -> bool:
    for word in words:
        if not word.isalpha():
            return False
    return True
