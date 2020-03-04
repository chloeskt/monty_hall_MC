from random import shuffle, choice

def monty_hall_game():
    # Create the doors with random allocation of the car i.e 1
    doors = [0, 1, 0]
    shuffle(doors)

    # Choose a door among the three
    door_selected = choice([0, 1, 2])

    # Open the door that does not have the car
    non_car_doors = list()
    for i,d in enumerate(doors):
        if d == 0 and i != door_selected: non_car_doors.append(i)

    door_opened = choice(non_car_doors)

    # Success if the player does not switch
    non_switch_success =  True if doors[door_selected] == 1 else False

    # Success if the player switches
    remaining_door = set([0,1,2]).difference([door_selected, door_opened])
    remaining_door = remaining_door.pop()
    switch_success =  True if doors[remaining_door] == 1 else False

    return non_switch_success, switch_success


def monte_carlo_estimate(nb_simulation):
    non_switch_success_count = 0
    switch_success_count = 0
    for i in range(nb_simulation):
        non_switch_success, switch_success = monty_hall_game()
        non_switch_success_count += non_switch_success
        switch_success_count += switch_success

    print(f"Number of plays: {nb_simulation}")
    print(f"Number of success on switch: {switch_success_count}  {(switch_success_count/nb_simulation)*100}%")
    print(f"Number of success on non-switch: {non_switch_success_count}  {(non_switch_success_count/nb_simulation)*100}%")


monte_carlo_estimate(1000)
