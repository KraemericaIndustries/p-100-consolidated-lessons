def calculate_love_score(name1, name2):

    name1 = name1.lower()
    name2 = name2.lower()

    names = [name1, name2]

    true_score = 0
    love_score = 0

    for name in names:
        for char in name:
            if char == "t": true_score += 1
            if char == "r": true_score += 1
            if char == "u": true_score += 1
            if char == "e": true_score += 1

    for name in names:
        for char in name:
            if char == "l": love_score += 1
            if char == "o": love_score += 1
            if char == "v": love_score += 1
            if char == "e": love_score += 1

    print(true_score)
    print(love_score)

    cast1 = str(true_score)
    cast2 = str(love_score)
    concat = cast1 + cast2
    print(int(concat))
calculate_love_score("Kanye West", "Kim Kardashian")