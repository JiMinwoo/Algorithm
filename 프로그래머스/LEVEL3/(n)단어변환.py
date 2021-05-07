def solution(begin, target, words):
    
    answer = 0
    ch_word = [begin] # 현재 상태에서 변환될수있는 단어리스트
    visited = [False] * len(words)

    if target not in words:
        return 0

    while ch_word:

        if target in ch_word:
            return answer

        now = ch_word.pop()

        for i in range(len(words)):
            cnt = 0

            if not visited[i]:
                for j in range(len(begin)):
                    if now[j] == words[i][j]:
                        cnt += 1   
            
            if cnt == 2:
                    ch_word.append(words[i])
                    visited[i] = True

        answer += 1

    if False not in visited[i]:
        return 0

    return answer

print(solution("hit","cog",["cog","hot","hig"]))