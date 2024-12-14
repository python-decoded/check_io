
def is_acceptable_password(password: str) -> bool:

    misses_password_word = "password" not in password.lower()
    is_long = len(password) > 8
    is_short = len(password) >= 7 and not is_long
    digits_check = (password.isalnum() and
                    not password.isalpha() and
                    not password.isnumeric())

    is_valid_short = is_short and digits_check and misses_password_word
    is_valid_long = is_long and misses_password_word

    return is_valid_short or is_valid_long
