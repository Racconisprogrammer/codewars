def stringCamel(s: str)->str:
    return "".join(' '+i if i.isupper() else i for i in s)
