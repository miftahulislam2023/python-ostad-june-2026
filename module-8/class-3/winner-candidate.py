candidate1 = {
    "id": 1,
    "name": "Abu Jafor",
    "age": 40,
    "vote_count": 340,
    "zone": "Rajshahi-02",
    "symbol": "Light-bulb"
}

candidate2 = {
    "id": 2,
    "name": "Nishat",
    "age": 35,
    "vote_count": 24,
    "zone": "Rajshahi-02",
    "symbol": "Bus"
}

candidate3 = {
    "id": 3,
    "name": "Aron",
    "age": 30,
    "vote_count": 45,
    "zone": "Sylhet-01",
    "symbol": "Tree"
}

candidate4 = {
    "id": 4,
    "name": "Alia",
    "age": 28,
    "vote_count": 1800,
    "zone": "Chittagong-03",
    "symbol": "Fan"
}

candidates = [
    candidate1, candidate2, candidate3, candidate4
]

winner_index = 0

for candidate in candidates:
    if candidate["vote_count"] > candidates[winner_index]["vote_count"]:
        winner_index = candidate["id"] - 1

print(candidates[winner_index])