
def backward_string_by_word(text: str) -> str:

    words = text.split(" ")

    res = []
    for word in words:
        word = reverse(word)
        res.append(word)

    return " ".join(res)


def reverse(text: str) -> str:
    return text[::-1]


def backward_string_by_word_gen(text: str) -> str:
    return " ".join(reverse(word) for word in text.split(" "))


def backward_string_by_word_map(text: str) -> str:
    return " ".join(map(reverse, text.split(" ")))
