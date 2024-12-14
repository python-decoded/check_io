from collections import defaultdict, Counter


def popular_words(text: str, words: list) -> dict:

    res = {}

    text = text.lower().split()

    for word in words:
        res[word] = text.count(word)

    return res


def popular_words_list(text: str, words: list) -> dict:

    text = text.lower().split()
    return dict([word, text.count(word)] for word in words)


def popular_words_comp(text: str, words: list) -> dict:

    text = text.lower().split()
    return {word: text.count(word) for word in words}


def popular_words_perf(text: str, words: list) -> dict:

    words = set(words)

    res = dict.fromkeys(words, 0)
    for word in text.lower().split():
        if word in words:
            res[word] = res[word] + 1

    return res


def popular_words_all(text: str, words: list) -> dict:

    res = {}
    for word in text.lower().split():
        res[word] = res.get(word, 0) + 1

    return {word: res.get(word, 0) for word in words}


def popular_words_defaultdict(text: str, words: list) -> dict:

    res = defaultdict(int)
    for word in text.lower().split():
        res[word] += 1

    return {word: res[word] for word in words}


def popular_words_counter(text: str, words: list) -> dict:
    res = Counter(text.lower().split())
    return {word: res[word] for word in words}
