'''
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the
missing second character of the final pair with an underscore ('_').
'''

from icecream import ic


def solution(s):
    lst = []
    s = s if len(s) % 2 == 0 else s + "_"
    for i in range(0, len(s), 2):
        lst.append(s[i] + s[i + 1])
    return lst


def main():
    solution("abcdefg")
    pass


if __name__ == "__main__":
    main()
