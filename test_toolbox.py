from toolbox import is_palindrome, word_frequency

# Palindrome


def test_is_palindrome_simple():
    assert is_palindrome("radar") is True


def test_is_palindrome_with_spaces():
    assert is_palindrome("un roc si biscornu") is True  # échoue à cause du bug


def test_is_palindrome_false():
    assert is_palindrome("python") is False


# Word frequency


def test_word_frequency_happy_path():
    result = word_frequency("the cat and the dog")
    assert result == {"the": 2, "cat": 1, "and": 1, "dog": 1}


def test_word_frequency_case_insensitive():
    result = word_frequency("The the THE")
    assert result == {"the": 3}


def test_word_frequency_with_punctuation():
    result = word_frequency("hello, world! hello...")
    assert result == {"hello": 2, "world": 1}


def test_word_frequency_empty_string():
    result = word_frequency("")
    assert result == {}


def test_word_frequency_only_punctuation():
    result = word_frequency("!!! ... ,,,")
    assert result == {}


def test_word_frequency_single_word():
    result = word_frequency("python")
    assert result == {"python": 1}
