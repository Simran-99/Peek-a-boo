import os
import sys
import time
from grid import MemoryGame




#Creating a function to play the game
def playgame(size):
    #object created for a player to track the scores,guesses and the cells that have been guessed correctly
    gamer = MemoryGame(size)
    choice = -1
    #as per the assignment, the grid, the title and the menu should be displayed at all times. The gamer.user_interface() will make sure of that
    gamer.user_interface()
    total_guesses = size*size//2
    guess = 0
    while True:
        if gamer.validate==True:
            print("You could either select option 4 to start a new game or option 5 to quit\n")
            gamer.user_interface()
            choice=input("Select")
            choice=int(choice)

            if choice==1:
                print("Invalid choice, you can either play again or end the game\n")
                time.sleep(1)
                os.system("cls")

            elif choice==2:
                print("Invalid choice, you can either play again or end the game\n")
                time.sleep(1)
                os.system("cls")
            elif choice==3:
                print("Invalid choice, you can either play again or end the game")
                time.sleep(1)
                os.system("cls")
            elif choice==4:
                new_gamer_size = gamer.new_game()
                playgame(new_gamer_size)
            elif choice==5:
                gamer.exit_sys()


        else:
            try:

                choice = input("Select ")
                choice = int(choice)

            except Exception as e:
                print("Please Enter a valid choice")

            #choice = int(choice)


            if choice == 1:
                f_check=False
                s_check=False
                guess = guess + 1
                #User input taken in the format a0 or A0.
                while f_check==False:

                    first_cell_coordinate = input("Enter first cell coordinates(e.g.,:a0): ")

                    f_row = int(first_cell_coordinate[1])
                    f_column = ord(first_cell_coordinate[0].upper()) - ord('A')
                    #Conditions to check if the raw number input is less than the number of rows we have
                    if f_row>=size or len(first_cell_coordinate)>2:
                        print("Input Error: Row Entry is out of range. Please try again")
                    #Condition to check if column number is less than the number of columns we have
                    elif f_column>=size or len(first_cell_coordinate)>2:
                        print("Input Error: Column Entry is out of range")
                    #If both the conditions are not true then we validate the coordinate
                    else:
                        f_check=True
                while s_check==False:



                    #User input for second cell taken in the format a0 , A0.
                    second_cell_coordinate = input("Enter second cell coordinates(e.g.,:a0): ")
                    s_row = int(second_cell_coordinate[1])
                    s_column = ord(second_cell_coordinate[0].upper()) - ord('A')
                    # Conditions to check if the raw number input is less than the number of rows we have
                    if s_row!=f_row or s_column!=f_column:
                        if s_row>=size or len(second_cell_coordinate)>2:
                            print("Input Error: Row Entry is out of range. Please try again\n")
                        # Condition to check if column number is less than the number of columns we have
                        elif s_column>=size or len(second_cell_coordinate)>2:
                            print("Input Error: Column Entry is out of range\n")
                        # If both the conditions are not true then we validate the coordinate
                        else:
                            s_check=True
                        #If the first and second coordinate are validated the function will be called for choice 1(revealing the pairs)
                    else:
                        print("Invalid input. First and second coordinate cannot be the same. Please try again\n")


                if f_check==True and s_check==True:

                    gamer.revealing_two_elements(first_cell_coordinate,second_cell_coordinate)
                else:
                    time.sleep(2)
                    os.system("cls")
                    gamer.user_interface()
                # print("I was returned back")
            elif choice == 2:
                #on manually turning over the cell the number of guesses counter are 2
                guess = guess + 2
                #taking the input in the format a0
                e_check = False

                while e_check==False:

                    element_coordinate = input("Enter cell coordinates(e.g,.:a0) ")




                    e_row = int(element_coordinate[1])
                    e_column = ord(element_coordinate[0].upper()) - ord('A')
                    # Conditions to check if the raw number input is less than the number of rows we have
                    if e_row >= size or len(element_coordinate)>2:
                        print("Input Error: Row Entry is out of range. Please try again\n")
                    # Condition to check if column number is less than the number of columns we have
                    elif e_column >= size or len(element_coordinate)>2:
                        print("Input Error: Column Entry is out of range.Please try again\n")
                    #if the rows and column are in the specified range then 2_check would be set to True
                    else:
                        e_check = True
                    #function would be called to show single element
                if e_check:
                    gamer.show_one(element_coordinate)
            elif choice == 3:
                guess = 0
                gamer.reveal_all()
            elif choice == 4:
                guess = 0


                new_gamer_size=gamer.new_game()


                playgame(new_gamer_size)

                #playgame(size)

            elif choice == 5:
                #score = (total_guesses / guess) * 100
                #print("Score is", score)

                gamer.exit_sys()

            elif isinstance(choice,int) and (choice<1 or choice>5):

                print("INVALID INPUT! Please enter a valid choice(1-5)\n")




if __name__ == "__main__":

    size = int(sys.argv[1])
    #Error checking if the matrix size is 2, 4, 6 then the program will run otherwise it will display an eeror message and stop
    if size==4 or size==2 or size==6:
        playgame(size)
    else:
        print("Please enter a valid input(2,4 or 6)")