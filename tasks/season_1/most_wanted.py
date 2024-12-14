LETTERS = "abcdefghijklmnopqrstuvwxyz"


def checkio(text: str) -> str:

    text = text.lower()

    item = "a"
    val = text.count(item)

    for _item in LETTERS:
        _val = text.count(_item)

        if val < _val:
            item = _item
            val = _val

    return item


def checkio_max(text: str) -> str:
    return max(LETTERS, key=text.lower().count)
