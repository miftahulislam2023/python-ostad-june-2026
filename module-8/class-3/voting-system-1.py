voter1 = {
    "id": 1,
    "name": "Miftah",
    "age": 18,
    "has_voted": False,
    "zone": "Rajshahi-02"
}

voter2 = {
    "id": 2,
    "name": "Nishat",
    "age": 25,
    "has_voted": False,
    "zone": "Dhaka-05"
}

voter3 = {
    "id": 3,
    "name": "Alia",
    "age": 17,
    "has_voted": False,
    "zone": "Chittagong-03"
}

voter4 = {
    "id": 4,
    "name": "Aron",
    "age": 32,
    "has_voted": True,
    "zone": "Sylhet-01"
}

candidate1 = {
    "id": 1,
    "name": "Abu Jafor",
    "age": 40,
    "vote_count": 0,
    "zone": "Rajshahi-02",
    "symbol": "Light-bulb"
}

candidate2 = {
    "id": 2,
    "name": "Nishat",
    "age": 35,
    "vote_count": 0,
    "zone": "Rajshahi-02",
    "symbol": "Bus"
}

candidate3 = {
    "id": 3,
    "name": "Aron",
    "age": 30,
    "vote_count": 0,
    "zone": "Sylhet-01",
    "symbol": "Tree"
}

candidate4 = {
    "id": 4,
    "name": "Alia",
    "age": 28,
    "vote_count": 0,
    "zone": "Chittagong-03",
    "symbol": "Fan"
}

voters = [
    voter1, voter2, voter3, voter4
]

candidates = [
    candidate1, candidate2, candidate3, candidate4
]

for voter in voters:
    candidate_id = int(input(f"Enter candidate id for voter: {voter["name"]} - ID: {voter["id"]} - "))
    for candidate in candidates:
        if candidate["id"] == candidate_id and candidate["zone"] == voter["zone"]:
            candidate["vote_count"] += 1
            voter["has_voted"] = True
            print("You have successfully voted.")
            break

for candidate in candidates:
    print(candidate)
