from collections import deque


def isPalidrome(data: str) -> bool:
    deqata = deque(data.lower().replace(" ", ""))
    for i in range(len(deqata) // 2):
        if deqata[i] != deqata[-(i + 1)]:
            return False
    return True


def main():
    data = "abobA "
    print(isPalidrome(data))


main()
