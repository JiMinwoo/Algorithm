def solution(progresses, speeds):

    answer = []

    while progresses:

        cnt = 0

        for i in range(0,len(progresses)):
            progresses[i] += speeds[i]

        if progresses[0] >= 100:
            for pg in progresses:
                if pg >= 100:
                    cnt += 1
                else:
                    break
            for i in range(cnt):
                progresses.pop(0)
                speeds.pop(0)

            answer.append(cnt)

    return answer