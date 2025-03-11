t = int(input())
for tc in range(t):
    n = int(input())
    trees = list(map(int, input().split()))

    m_height = max(trees)

    diff = [0 for _ in range(n)]
    mod1 = [0 for _ in range(n)]
    mod2 = [0 for _ in range(n)]
    for i in range(n):
        diff[i] = m_height - trees[i]
        mod1[i] = diff[i] // 3
        mod2[i] = diff[i] % 3

    days = 0
    days += sum(mod1)*2


    day1 = 0
    day2 = 0
    for i in mod2:
        if i == 1:
            day1 += 1
        elif i == 2:
            day2 += 1

    flag = False
    if day1 > day2:
        while True:
            if (day1-day2) < 3:
                break
            else:
                for i in diff:
                    if i%3 == 1 and i >= 4:
                        flag = True
                        diff[i] -= 4
                        break
                if flag:
                    days -= 2
                    day1 -= 1
                    day2 += 2
                    flag = False
    
    if day1 > day2:    
        days += day2 * 2
        day1 -= day2
        day2 = 0
        days += day1 * 2 - 1

    elif day1 < day2:
        days += day1 * 2
        day2 -= day1
        day1 = 0
        days += (day2+1+day2//3)
    else:
        days += day1 * 2

    print(f'#{tc+1}',days)