import random
scores = [random.randint(1, 100) for _ in range(8)]
print("Исходные баллы: " + str(scores))

min_score = min(scores)
max_score = max(scores)
print("Удаляем минимум (" + str(min_score) + ") и максимум (" + str(max_score) + ").")

scores.remove(min_score)
scores.remove(max_score)

average = sum(scores) / len(scores)
print("Оставшиеся баллы:", scores)
print("Средний рейтинг:", average)