N = int(input())

def afs(s):
    return int(s[:2]) * 60 + int(s[3:])

for tc in range(N):
    T = int(input())
    Na, Nb = list(map(int, input().split()))
    a_schedule = [list(map(afs, input().split())) + [1] for _ in range(Na)]
    b_schedule = [list(map(afs, input().split())) + [2] for _ in range(Nb)]
    schedule = sorted(a_schedule + b_schedule)
    A = []
    B = []

    answer_a = 0
    answer_b = 0

    for i in range(len(schedule)):
        if schedule[i][2] == 1:
            for j in range(len(A)):
                if A[j] <= schedule[i][0]:
                    A.pop(j)
                    break
                else:
                    pass
            else:
                answer_a += 1
            B.append(schedule[i][1] + T)
        else:
            A.append(schedule[i][1] + T)
            for j in range(len(B)):
                if B[j] <= schedule[i][0]:
                    B.pop(j)
                    break
                else:
                    pass
            else:
                answer_b += 1
    print('Case #%d: %d %d' %(tc + 1, answer_a, answer_b))




