def isSymetric(s: str) -> bool:
    stack = []
    brackets = {"]": "[", "}": "{", ")": "("}

    for char in s:
        if char in "[{(":
            stack.append(char)
        elif char in "]})":
            if not stack or stack.pop() != brackets[char]:
                return False

    return len(stack) == 0


def main():
    data = "[{[]}]"
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
