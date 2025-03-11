T = int(input())
for tc in range(T):
    n, l = map(int, input().split())    # 재료의 수, 제한 칼로리
    tk_lst = [[0,0]]
    for _ in range(n):
        tk_lst.append(list(map(int, input().split())))

    dp = [[0 for _ in range(l+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,l+1):
            taste = tk_lst[i][0]
            kcal = tk_lst[i][1]

            if j < kcal:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-kcal] + taste)

    print(f'#{tc + 1}', dp[n][l])

    # for i in range(1, l+1):
    #     if i in k:
    #         dp[i][0] = max(dp[i-1][0] + dp[1][0], t[k.index(i)]) + dp[i-1][0]
    #         dp[i] = dp[i-1] + dp[i]
    #     else:
    #         dp[i] = dp[i] + dp[i-1]
    #
    # for i in range(0,l,100):
    #    print(dp[i])
    # print(f'#{tc+1}', dp[-1])


    '''
    1. 더했을 때 제한 칼로리를 넘지 않아야함
    2. 맛의 점수를 누적해서 dp에 저장
    '''