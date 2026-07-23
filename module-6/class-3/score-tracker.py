a_team_scores = [1, 0, 1, 1, 0, 1]
b_team_scores = [0, 1, 0, 0, 1, 0]

total_score_a = 0
total_score_b = 0

for score in a_team_scores:
    total_score_a += score

for score in b_team_scores:
    total_score_b += score

if total_score_a > total_score_b:
    print("A is the winner")
elif total_score_b > total_score_a:
    print("B is the winner")
else:
    print("No team won. It's a draw")
