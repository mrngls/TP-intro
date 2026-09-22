def is_palindrome(s: str) -> bool:
    """Renvoie True si s est un palindrome (insensible à la casse et aux espaces)."""
    cleaned = s.lower()  # bug volontaire : les espaces ne sont pas retirés
    return cleaned == cleaned[::-1]


def word_frequency(text: str) -> dict:
    """À implémenter : renvoie {mot: nombre d'occurrences}, insensible à la casse et à la ponctuation."""
    raise NotImplementedError


def celsius_to_fahrenheit(celsius: float) -> float:
    """À implémenter : convertit une température de Celsius en Fahrenheit."""
    raise NotImplementedError
