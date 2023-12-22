"""
Author: Halaevalu Patterson, patte194@purdue.edu
Assignment: 12.1 - Battleship
Date: 10/30/2023

Description:
    This program will create a space themed single player variation of battleship
Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
import random

"""Write new functions below this line (starting with unit 4)."""


# make_grid function
def print_grid(grid_list):
    print("\n   A  B  C  D  E  F  G  H  I  J  K  L")
    for column in range(len(grid_list)):
        list_element = grid_list[column]
        print(column, end='  ')
        for row in range(len(list_element)):
            if row == 11:
                print(list_element[row])
            else:
                print(list_element[row], end='  ')

def empty_grid():
    my_grid = []  # 10x12
    for column in range(10):
        temp_list = []
        for row in range(12):
            temp_list.append('~')  # ~ represents empty space
        my_grid.append(temp_list)
    return my_grid

def make_grid():
    my_grid = empty_grid()

    # 'M', 'B', 'D', 'S', 'P' -> mothership(5), battleship(4), destroyer(3), stealth ship(3), patrol ship(2)
    my_ships = {
        'mothership': 'x',
        'battleship': 'sq',
        'destroyer': 'c',
        'stealth ship': 'hz',
        'patrol ship': 'hz'
    }

    for key, value in my_ships.items():
        if key == 'mothership':
            placed = False
            while not placed: # Loop until placed
                row = random.randint(0, 9)
                column = random.randint(0, 12)
                mothership = [
                    ['M', '~', 'M'],
                    ['~', 'M', '~'],
                    ['M', '~', 'M']
                ]
                if check_ship_placement(my_grid, mothership, row, column):
                    place_ship(my_grid, mothership, row, column) # Place ship if valid
                    placed = True
        elif key == 'battleship':
            placed = False
            while not placed:
                row = random.randint(0, 9)
                column = random.randint(0, 12)
                battleship = [
                    ['B', 'B'],
                    ['B', 'B']
                ]
                if check_ship_placement(my_grid, battleship, row, column):
                    place_ship(my_grid, battleship, row, column)
                    placed = True
        elif key == 'destroyer':
            placed = False
            while not placed:
                row = random.randint(0, 9)
                column = random.randint(0, 12)
                destroyer = [
                    ['D', '~'],
                    ['~', 'D'],
                    ['D', '~']
                ]
                if check_ship_placement(my_grid, destroyer, row, column):
                    place_ship(my_grid, destroyer, row, column)
                    placed = True
        elif key == 'stealth ship':
            placed = False
            while not placed:
                row = random.randint(0, 9)
                column = random.randint(0, 12)
                stealth_ship = [
                    ['S', 'S', 'S']
                ]
                if check_ship_placement(my_grid, stealth_ship, row, column):
                    place_ship(my_grid, stealth_ship, row, column)
                    placed = True
        elif key == 'patrol ship':
            placed = False
            while not placed:
                row = random.randint(0, 9)
                column = random.randint(0, 12)
                patrol_ship = [
                    ['P', 'P']
                ]
                if check_ship_placement(my_grid, patrol_ship, row, column):
                    place_ship(my_grid, patrol_ship, row, column)
                    placed = True
        
    return my_grid

def check_ship_placement(grid, ship, start_row, start_col):
    # Iterate horizontal length of ship
    for i in range(len(ship)):
        # Iterate through vertical of ship
        for j in range(len(ship[i])):
            row = start_row + i # Get row of Grid
            col = start_col + j # Get column of grid
            # Check if position is within the grid bounds and is empty
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == '~'):
                return False
    return True

def place_ship(grid, ship, start_row, start_col):
    for i in range(len(ship)):
        for j in range(len(ship[i])):
            row = start_row + i
            col = start_col + j
            grid[row][col] = ship[i][j]

def print_menu():
    print("\nMenu:")
    print("  1 : Instructions")
    print("  2 : View Example Map")
    print("  3 : New Game")
    print("  4 : Hall of Fame")
    print("  5 : Quit")

def print_instructions():
    print("\nInstructions:\n")
    print("Ships are positioned at fixed locations in a 10-by-12 grid. The")
    print("rows of the grid are labeled 0 through 9, and the columns are")
    print("labeled A through L. Use menu option \"2\" to see an example.")
    print("Target the ships by entering the row and column of the location")
    print("you wish to shoot. A ship is destroyed when all of the spaces")
    print("it fills have been hit. Try to destroy the fleet with as few")
    print("shots as possible. The fleet consists of the following 5 ships:\n")
    print("Size : Type")
    print("   5 : Mothership")
    print("   4 : Battleship")
    print("   3 : Destroyer")
    print("   3 : Stealth Ship")
    print("   2 : Patrol Ship")

class map_logic():
    def __init__(self, game_map, location_key_columns, shots_taken, shots_missed, shots_hit):
        self.game_map = game_map
        self.location_key_columns = location_key_columns
        self.shots_taken = shots_taken
        self.shots_missed = shots_missed
        self.shots_hit = shots_hit
        self.mothership_bool = False
        self.battleship_bool = False
        self.destroyer_bool = False
        self.stealthship_bool = False
        self.patrolship_bool = False

    def update_map(self, target):
        temp_column = self.location_key_columns[target[1:]]
        self.game_map[int(target[0])][temp_column] = '~'
    
    def check_hit(self, target):
        temp_column = self.location_key_columns[target[1:]]
        if self.game_map[int(target[0])][temp_column] != '~':
            self.game_map[int(target[0])][temp_column] = '~'
            return True
        else:
            return False
    
    def update_shots_taken(self):
        self.shots_taken += 1

    def update_shots_missed(self):
        self.shots_missed += 1
        
    def update_shots_hit(self):
        self.shots_hit += 1
    
    def calculate_accuracy(self):
        return (float(self.shots_hit / self.shots_taken)*100.0)
    
    def create_temp_list(self):
        temp_list = []
        for i in range(len(self.game_map)):
            for j in range(len(self.game_map[i])):
                temp_list.append(self.game_map[i][j])
        return temp_list
    
    # Check all ships destroyed yet
    def check_mothership(self):
        temp_list = self.create_temp_list()
        if (self.mothership_bool == False) and ('M' not in temp_list):
            print("The enemy's Mothership has been destroyed.")
            self.mothership_bool = True
    def check_battleship(self):
        temp_list = self.create_temp_list()
        if (self.battleship_bool == False) and ('B' not in temp_list):
            print("The enemy's Battleship has been destroyed.")
            self.battleship_bool = True
    def check_destroyer(self):
        temp_list = self.create_temp_list()
        if (self.destroyer_bool == False) and ('D' not in temp_list):
            print("The enemy's Destroyer has been destroyed.")
            self.destroyer_bool = True
    def check_stealthship(self):
        temp_list = self.create_temp_list()
        if (self.stealthship_bool == False) and ('S' not in temp_list):
            print("The enemy's Stealth Ship has been destroyed.")
            self.stealthship_bool = True
    def check_patrolship(self):
        temp_list = self.create_temp_list()
        if (self.patrolship_bool == False) and ('P' not in temp_list):
            print("The enemy's Patrol Ship has been destroyed.")
            self.patrolship_bool = True

    def check_status(self):
        if self.mothership_bool == True and self.battleship_bool == True and self.destroyer_bool == True and self.stealthship_bool == True and self.patrolship_bool == True:
            return True
        else: 
            return False
    

def game():
    game_over = False
    game_map = make_grid()
    current_map = empty_grid()
    location_key_columns = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11}
    location_key_rows = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    spots_picked = []
    user_map = map_logic(game_map, location_key_columns, 0, 0, 0)
    print_grid(current_map)

    while(game_over == False):
        target = input("\nWhere should we target next (q to quit)? ")
        if target == 'q' or target == 'Q':
            game_over = True
        elif len(target) < 2:
            print("Please enter exactly two characters.")
        elif len(target) > 2:
            print("Please enter exactly two characters.")
        elif target[0].isascii() and not target[0].isdigit():
            print("Please enter a location in the form \"6G\".")
        elif (((target[1:]) in location_key_columns) and (target[0] in location_key_rows)):
            if (target[0]) in location_key_rows:
                if target in spots_picked:
                    print("\nYou've already targeted that location")
                    user_map.update_shots_taken()
                else:
                    user_map.update_shots_taken()
                    spots_picked.append(target)
                    # Check if there's a hit
                    result = user_map.check_hit(target)
                    # If a hit, display x
                    if result == True:
                        user_map.update_shots_hit()
                        print("\nIT'S A HIT!")
                        current_map[int(target[0])][location_key_columns[target[1:]]] = 'x'
                        user_map.check_mothership()
                        user_map.check_battleship()
                        user_map.check_destroyer()
                        user_map.check_patrolship()
                        user_map.check_stealthship()
                        if user_map.check_status() == False:
                            print_grid(current_map)
                    # If a miss, display o
                    elif result == False:
                        user_map.update_shots_missed()
                        print("\nmiss")
                        current_map[int(target[0])][location_key_columns[target[1:]]] = 'o'
                        print_grid(current_map)
            else:
                print("Please enter a location in the form \"6G\".")
        else:
            print("Please enter a location in the form \"6G\".")
        # Game over when won
        if user_map.check_status() == True:
            print("\nYou've destroyed the enemy fleet!")
            print("Humanity has been saved from the threat of AI.")
            print("\nFor now ...")

            if hall_of_fame.check_hof(user_map.shots_missed) == True:
                print("\nCongratulations, you have achieved a targeting accuracy of")
                print(f"{user_map.calculate_accuracy():.2f}% and earned a spot in the Hall of Fame.")
                hof_name = input("Enter your name: ")
                hall_of_fame.update_scores(user_map.shots_missed, hof_name)
                hall_of_fame.print_hof()
            else:
                print(f"\nYour targeting accuracy was {user_map.calculate_accuracy():.2f}%.")
            game_over = True

class hof():
    def __init__(self, file):
        self.file = file
    
    def print_hof(self):
        print("\nHall of Fame:")
        print("+------+-------------+----------+")
        print("| Rank | Player Name | Accuracy |")
        print("+------+-------------+----------+")
        file_list = self.file_list()
        for i in range(len(file_list)):
            if i == 0:
                continue
            else:
                accuracy = (float(17.0 / (float(file_list[i][0])+17.0)))*100
                print(f"| {i:^5}|{file_list[i][1]:^13}|{accuracy:8.2f}% |")
        print("+------+-------------+----------+")

    def initialize_hof(self):
        with open(self.file, "w") as myfile:
            myfile.write("misses,name\n")
    
    def file_list(self):
        file_list = []

        with open(self.file, "r") as myfile:
            for i in myfile:
                file_list.append(i.strip().split(','))
        return file_list

    def update_scores(self, missed, name):
        with open(self.file, "r") as myfile:
            lines = myfile.readlines()[1:]
        lines.append(f"{missed},{name}\n")
        sorted_lines = sorted(lines, key=lambda x: (int(x.split(',')[0]), lines.index(x)))
        top_10 = sorted_lines[:10]
        # bruh add column name back i hate my life
        with open(self.file, "w") as myfile:
            myfile.write("misses,name\n")
            myfile.writelines(top_10)

    def check_hof(self, missed):
        my_file = self.file_list()
        my_file.remove(my_file[0])
        if len(my_file) < 10:
            return True
        else:
            missed_list = []
            for i in range(len(my_file)):
                missed_list.append(int(my_file[i][0]))
            if missed <= max(missed_list): 
                return True
            else: 
                return False

def get_valid_choice():
    user_input = input("What would you like to do? ")
    valid_choices = ['1', '2', '3', '4', '5']
    while user_input not in valid_choices:
        print("\nInvalid selection.  Please choose a number from the menu.")
        print_menu()
        user_input = input("What would you like to do? ")
    return int(user_input)

hall_of_fame = hof("battleship_hof.txt")
hall_of_fame.initialize_hof()

def main():
    # Intro
    print("\n                   ~ Welcome to Battleship! ~                   \n")
    print("ChatGPT has gone rogue and commandeered a space strike fleet.")
    print("It's on a mission to take over the world.  We've located the")
    print("stolen ships, but we need your superior intelligence to help")
    print("destroy them before it's too late.")

    # Print the main menu
    print_menu()
    user_input = get_valid_choice()
    while (user_input != 5):
        if user_input == 1:
            # Choose instructions - display, return to main menu
            print_instructions()
        if user_input == 2:
            print_grid(make_grid())
        if user_input == 3:
            game()
        if user_input == 4:
            hall_of_fame.print_hof()
            
        print_menu()
        user_input = get_valid_choice()
    print("\nGoodbye")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
