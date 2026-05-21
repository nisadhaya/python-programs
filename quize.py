scoreboard = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

print("--- QUIZ SCOREBOARD ---")
sorted_scores = sorted(scoreboard.items(), key=lambda x: x[1], reverse=True)

for rank, (player, score) in enumerate(sorted_scores, 1):
    print(f"{rank}. {player}: {score} points")
