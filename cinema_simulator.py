films = {
    "Finding Nemo": [3, 5],
    "Tarzan": [15, 2],
    "Vikram Betaal": [12, 5],
    "Darr": [18, 5]
}

while True:
    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("how old are you?: ").strip())
        if age >= films[choice][0]:
            # check enough seats

            if films[choice][1] > 0:
                print("enjoy the movie")
                films[choice][1] = films[choice][1] - 1
            else:
                print("We are sold out")
        else:
            print("You're not old enough to watch the movie")
    else:
        print("we do not have that movie")
