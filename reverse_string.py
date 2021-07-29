def rev_string(s):
    # itertive
    n = len(s)-1
    rev_s = ''
    while n >= 0:
        rev_s = rev_s + s[n]
        n -= 1
    print(f"iterative way: {rev_s}")


def rev_string_recursive(s):
    if s == "":
        return ""
    else:
        return rev_string_recursive(s[1:]) + s[0]


def rev_string_pythonic(s):
    # python way
    print(f"python way: {s[::-1]}")


if __name__ == "__main__":
    test_s = 'Hey'
    rev_string(test_s)
    print(f"recursive method: {rev_string_recursive(test_s)}")

