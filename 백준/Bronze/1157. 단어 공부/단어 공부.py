import sys
input = sys.stdin.readline

# 가장 많이 사용된 알파벳을 대문자로 출력
# 가장 많이 사용된 알파벳이 여러 개 존재하는 경우는 ?를 출력

word = input().strip().upper()
word_list = list(word)
cnt = {}

for w in word_list:
    if w in cnt:
        cnt[w] += 1
    else:
        cnt[w] = 1

maxV = max(cnt.values())
max_cnt = []

for k, v in cnt.items():
    if v == maxV:
        max_cnt.append(k)

if len(max_cnt) > 1:
    print("?")
else:
    print(max_cnt[0])
# sort_word = sorted(cnt.items(),key=lambda x:x[1])
# print(sort_word)