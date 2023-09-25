poem = '''
나 보기가 역겨워 가실 때에는 말없이 고이 보내 드리오리다
영변에 약산 진달래꽃 아름 따다 가실 길에 뿌리오리다
가시는 걸음 걸음 놓인 그 꽃을 사뿐히 즈려 밟고 가시옵소서
나 보기가 역겨워 가실 때에는 죽어도 아니 눈을 흘리오리다
'''

countWord = {}
for word in poem:
    if word.isalpha():
        if word in countWord:
            countWord[word] += 1
        else:
            countWord[word] = 1
print("원문 ", poem)
print("--------------------------------------------------------")
print("문자 빈도수 (4회 이상)")
print("--------------------------------------------------------")
for key in countWord:
    if countWord[key] >= 4:
        print(key, '--->', countWord[key])
print("countWord 전문")
print(countWord)