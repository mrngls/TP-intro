def is_palindrome(s: str) -> bool:
    """Renvoie True si s est un palindrome (insensible à la casse et aux espaces)."""
    cleaned = "".join(s.lower().split())
    return cleaned == cleaned[::-1]


def word_frequency(text: str) -> dict:
    """Renvoie {mot: nombre d'occurrences}, insensible à la casse et à la ponctuation."""
    text = text.lower()
    cleaned = ""
    for char in text:
        if char.isalnum() or char == " ":
            cleaned += char
        else:
            cleaned += " "
    words = cleaned.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def celsius_to_fahrenheit(celsius: float) -> float:
    """À implémenter : convertit une température de Celsius en Fahrenheit."""
    raise NotImplementedError
