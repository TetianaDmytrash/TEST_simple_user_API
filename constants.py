"""
    all constants that need to correct system work
"""
import string


LOCALHOST = "http://127.0.0.1"
PORT = "5000"

USERS_LINK = "/users"
USER_LINK = "/user"

ascii_letters = string.ascii_letters
digits = string.digits
special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"

ALL_CHARS = ascii_letters + digits + special_chars
LETTER_CHARS = ascii_letters
DIGITS_CHARS = digits
DIGITS_LETTERS_CHARS = ascii_letters + digits
LETTERS_SPECIAL_CHARS = ascii_letters + special_chars

GET_ALL_USERS_LINK = LOCALHOST + ":" + PORT + USERS_LINK
GET_USER_LINK = LOCALHOST + ":" + PORT + USER_LINK
POST_USER_LINK = LOCALHOST + ":" + PORT + USER_LINK
PUT_USER_LINK = LOCALHOST + ":" + PORT + USER_LINK
DELETE_USER_LINK = LOCALHOST + ":" + PORT + USER_LINK
