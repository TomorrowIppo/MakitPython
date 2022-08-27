scores = []
sum_scores = 0
aver = 0
test_num = 4

for i in range(test_num):
    score = int(input('시험 점수 : '))
    scores.append(score)

for score in scores:
    sum_scores += score

aver = int(sum_scores/test_num)
print('평균 :', aver)