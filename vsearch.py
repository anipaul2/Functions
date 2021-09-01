def searchforvowels(phrase:str) -> set:
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))
print(searchforvowels('sky'))
def search4letters(phrase:str, letters:str = 'aeiou') -> set:
    """Return a set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
print(search4letters('galaxy', 'xyz'))
