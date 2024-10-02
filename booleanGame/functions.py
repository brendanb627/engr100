def check_score(problem_answer_list):
    print(f"You got {score(problem_answer_list)} out of {len(problem_answer_list)}")

def score(problem_answer_list):
    score = 0
    for i in problem_answer_list:
        if i[0] == i[1]:
            score += 1

    return score