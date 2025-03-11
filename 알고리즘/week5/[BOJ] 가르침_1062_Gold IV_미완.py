import time
a = time.time()
n, k = map(int, input().split())

'''
a c e h l o r t
a c r 
rc
hello
car
a n t i c 'r'
모든 알파벳에 대하여 counting을 해주기
'''

alphabets = {}
for i in range(26):
    alphabets[chr(i+97)] = 1    # 제시된 단어의 알파벳 종류보다 k가 더 큰 경우를 제외하기 위해 0이 아닌 1 입력

languages = []                  # 입력받을 모든 단어
for _ in range(n):              # 각각의 단어 입력받기
    language = input().strip()
    languages.append(language)

if k < 5:                       # a, n, t, i, c 를 배울 수 없어서 배울 수 있는 단어가 없음
    print(0)

else:                           # 각각의 단어의 알파벳 개수 counting
    for language in languages:  # 입력받은 모든 단어에 대해서 단어 한 개씩 봄
        dup = ''                # 중복 제거를 위한 변수
        for i in language[4:-4]:    # 앞, 뒤 anta, tica제외 가운데 알파벳 확인
            if i not in dup:        # 처음 나온 알파벳이라면
                alphabets[i] += 1   # dict에 counting 1 추가
                dup += i            # dup에 해당 알파벳 넣기

    teach = ['a','n','t','i','c']   # 가르쳐야하는 단어 + anta/tica
    while True:
        if len(teach) == k:         # k개를 모두 뽑은 경우
            break

        max_word = max(alphabets, key=alphabets.get)    # alphabet 중에서 가장 많은 단어
        if max_word not in teach:                       # teach 변수에 없다면 추가
            teach.append(max_word)
        alphabets[max_word] = 0                         # 해당 알파벳의 dict 값은 0으로 리셋
        
    ans = 0                         # 최종 결과
    for i in range(n):  
        cnt = 0                     # 각각의 단어를 읽을 수 있는지 확인하기 위한 변수
        for lang in languages[i]:   # lang: 각 단어의 알파벳
            # print(lang)
            if lang in teach:       # 배웠던 단어면 cnt + 1
                cnt += 1
        if cnt == len(languages[i]):# 해당 단어의 길이와 cnt가 일치하면 읽을 수 있는 단어임 -> ans + 1
            ans += 1

    print(ans)
b = time.time()
print(b-a)