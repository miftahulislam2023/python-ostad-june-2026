a_team_scores = []
b_team_scores = []

print("Press q to exit")
winner = input("Enter the winner team (a or b): ")

while True:
    if winner.lower() == 'q':
        break
    elif winner.lower() == 'a':
        a_team_scores.append(1)
        b_team_scores.append(0)
    elif winner.lower() == 'b':
        a_team_scores.append(0)
        b_team_scores.append(1)
    else:
        print("Invalid input. Please try again")
    
    winner = input("Enter the winner team (a or b): ")

# score count and compare

total_score_a = 0
total_score_b = 0

for score in a_team_scores:
    total_score_a += score

for score in b_team_scores:
    total_score_b += score

if total_score_a > total_score_b:
    print(f"A got {total_score_a} points and B got {total_score_b} points.\nThus is A the winner.")
elif total_score_b > total_score_a:
    print(f"A got {total_score_a} points and B got {total_score_b} points.\nThus is B the winner.")
else:
    print(f"A got {total_score_a} points and B got {total_score_b} points.\nNo team won. It's a draw.")
