def compute_average_scores(scores):
    averages = []
    for student_scores in zip(*scores):
        avg_score = sum(student_scores) / len(student_scores)
        averages.append(round(avg_score, 1))
    return tuple(averages)