# print(travel_log["France"[1]])
#
# print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris","Lille","Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin","Hamburg","Stuttgart"],
        "total_visits": 5
    },
}

print(travel_log["Germany"]["cities_visited"][2])