
def is_pangram(s: str):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    st = s.lower().replace(',', '').replace('!', '').replace(' ', '')
    st_set = set(st)

    return alphabet.issubset(st_set)
  
print(is_pangram("The quick, brown foxx jumps over the lazy dog!"))
