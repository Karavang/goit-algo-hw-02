def isSymetric(s: str) -> bool:
    s = s.lower().replace(" ", "")
    if not s:
        return True
    if len(s) == 1:
        return True
    if len(s) == 2:
        return s[0] == s[1]
    if len(s) % 2 == 1:
        return s[: len(s) // 2] == s[-(len(s) // 2 + 1) :][::-1]
    else:
        return s[: len(s) // 2] == s[-(len(s) // 2) :][::-1]


def main():
    data = "abobA "
    print(isSymetric(data))
    data = "abobA"
    print(isSymetric(data))
    data = "a"
    print(isSymetric(data))
    data = ""
    print(isSymetric(data))
    data = "ab"
    print(isSymetric(data))
    data = "abc"
    print(isSymetric(data))
    data = "abcd"
    print(isSymetric(data))


main()
