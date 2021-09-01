def searchforvowels(phrase:str) -> set:
    """Return any vowels found in a supplied word."""
    return set('aeiou').intersection(set(phrase))
print(searchforvowels('sky'))
help(searchforvowels)
def search4letters(phrase:str, letters:str = 'aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'. """
    return set(letters).intersection(set(phrase))
print(search4letters('galaxy', 'xyz'))
help(search4letters)
