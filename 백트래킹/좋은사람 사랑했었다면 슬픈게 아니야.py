'''
좋은 수열
https://www.acmicpc.net/problem/2661

이거 뭐임?
어캐 품?

후보
백트래킹
    - 가장 작은 수를 찾아야 하니깐 1 -> 2 -> 3씩 수열에 붙이고 판단
    - 나쁜 수열이 확인되면 넘어간다.
    - 나쁜 수열을 판단하는 기준이 마음에 안 들어 -> 그냥 다 돌아다니면서 판단해도 괜찮다.
'''


def is_bad(s):
    added = s[-1]

    pre_end = len(s)-1
    while True:
        idx = s.rfind(added, 0, pre_end)
        if idx == -1:
            return False

        diff = len(s)-1 - idx
        if diff <= idx+1:
            kind = False
            for i in range(1, diff):
                if s[len(s)-i-1] != s[idx-i]:
                    kind = True
                    break
            if not kind:
                return True
            pre_end = idx
        else:
            return False


def bt():
    global s, result

    if len(s) == N:
        result = s
    else:
        for number in ["1", "2", "3"]:
            tmp = s+number
            if not is_bad(tmp):
                s = tmp
                bt()
                if not result:
                    s = s[:-1]


N = int(input())

s = ""
result = None
bt()
print(result)
