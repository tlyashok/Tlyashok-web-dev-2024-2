n = int(input())


scores = list(map(int, input().split()))


unique_scores = sorted(set(scores), reverse=True)


second_place_score = unique_scores[1]

print(second_place_score)