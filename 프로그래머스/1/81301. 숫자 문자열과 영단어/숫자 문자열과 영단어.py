def solution(s):
    numberList = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for word, num in numberList.items():
        s = s.replace(word, num)
    answer = int(s)
    return answer