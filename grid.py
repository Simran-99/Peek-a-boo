import random
import os
import sys
import time

class MemoryGame:
    def __init__(self, size):
        #Size if to get the matrix size
        self.size = size
        #initalizing the grid with X
        self.grid = [["X"] * size for _ in range(size)]
        #generating random pairs
        self.pairs = self.random_generate_pairs(int(size))
        #initial number of guess=0
        self.guesses=0
        #total minimym nymber of guesses
        self.total_guesses=(size*size)//2
        #validate=False when all the numbers have not been uncovered
        self.validate=False
        #lst to store the elements that have been uncovered by guesses or manually uncovered so that they are not set to X again
        self.lst=[]
        #variable to store manually uncovered elements
        self.manually_uncover=0










    #The following function is to generate the random pairs and keep them in grd

    def random_generate_pairs(self, size):
        if not hasattr(self, 'generated_pairs'):
            self.generated_pairs = []
            grid = []
            # If size of the matrix is 4*4, 16 elements would be there in total 8 pairs should be generated
            total_num_pairs = (size * size) /2
            total_num_pairs = int(total_num_pairs)
            # generating numbers
            for i in range(total_num_pairs):
                for j in range(2):
                    self.generated_pairs.append(i)
            #shuffling the numbers generated
            random.shuffle(self.generated_pairs)
            numeric_grid = [[None] * (size) for i in range(size)]
        #Keeping the numbers that were generated in the numberic_grid
        for i in range(size):
            for j in range(size):
                numeric_grid[i][j] = self.generated_pairs.pop()
        # grid=grids(matrix_size)

        return numeric_grid

    def initial_grid(self):
        for i in range(len(self.grid)):
            print([i], end=" ")
            for j in range(len(self.grid)):
                print(self.grid[i][j], end=" ")
                print("   ", end=" ")
            print("\n")




    #the user_interface function displays the title, it represents the columns with alphabetically arranged letters
    #the rows are represented with numbers

    def user_interface(self):

        int_val_letter = ord('A')
        print("-------------------------")
        print("|      PEEK-A-BOO       |")
        print("-------------------------\n\n")

        print(" ", end=" ")
        for i in range(len(self.grid)):
            print([chr(int_val_letter + i)], end=" ")
        print("\n")
        #the following function is to display the initial grid which is initialized with X at the time when a new game started

        self.initial_grid()

        print("1.Let me select two elements")
        print("2.Uncover one element for me")
        print("3.I give up - reveal the grid")
        print("4.New game")
        print("5.Exit")
        print("\n")

    # def exit_menu(self):
    #     int_val_letter = ord('A')
    #     print("-------------------------")
    #     print("|      PEEK-A-BOO       |")
    #     print("-------------------------\n\n")
    #
    #     print(" ", end=" ")
    #     for i in range(len(self.grid)):
    #         print([chr(int_val_letter + i)], end=" ")
    #     print("\n")
    #
    #     self.initial_grid()
    #
    #
    #     print("1.New game")
    #     print("2.Exit")
    #     print("\n")






    def revealing_two_elements(self,first_cell_coordinate,second_cell_coordinate):



        self.guesses=self.guesses+1
        #first_cell_coordinate = input("Enter cell coordinates(e.g.,:a0): ")
        f_row = int(first_cell_coordinate[1])
        f_column = ord(first_cell_coordinate[0].upper()) - ord('A')

        #second_cell_coordinate = input("Enter cell coordinates(e.g.,:a0): ")
        s_row = int(second_cell_coordinate[1])
        s_column = ord(second_cell_coordinate[0].upper()) - ord('A')
        os.system("cls")
        grid_val = self.pairs
        #print(grid_val)

        #assigning the values from grid val to the grid which was initialised as X

        self.grid[f_row][f_column] = grid_val[f_row][f_column]
        self.grid[s_row][s_column] = grid_val[s_row][s_column]
        count=0

        #grid_val = self.pairs
        pairs_to_guess=len(grid_val)
        #if both the values at the tow coordinates are equal then store it in the list and again display the interface with two values visible
        if grid_val[f_row][f_column]==grid_val[s_row][s_column]:
            self.lst.append(first_cell_coordinate.upper())
            self.lst.append(second_cell_coordinate.upper()  )
            self.user_interface()
        #incase the values at the coordinates are not equal then they would apperar for two secons using sleep fn
        #after which they would be assigned X again
        #interface would be available again
        else:
            self.user_interface()
            time.sleep(2)
            os.system("cls")
            if first_cell_coordinate.upper() not in self.lst:
                self.grid[f_row][f_column] = "X"
            if second_cell_coordinate.upper() not in self.lst:
                self.grid[s_row][s_column] = "X"
            # if not self.lst:
            #     self.grid[f_row][f_column] = "X"
            #     self.grid[s_row][s_column] = "X"
            #     self.user_interface()
            #
            # else:
            #     for i in self.lst:
            #         if i.upper()!=first_cell_coordinate.upper():
            #             self.grid[f_row][f_column] = "X"
            #         elif i.upper()!=second_cell_coordinate.upper():
            #
            #             self.grid[s_row][s_column] = "X"
            self.user_interface()



       #if the entire grid is revealed then display the score
        for i in range(len(grid_val)):
            for j in range(len(grid_val)):
                if self.grid[i][j]=='X':
                    count=count+1

        if count==0:
            print("Oh! Happy Day. You've won! your score is {} ".format((self.total_guesses/self.guesses)*100))
            self.validate=True
        #time.sleep(2)
        #os.system("cls")



    def show_one(self,element_coordinate):
        #when one element is revealed the guesses are counted as 2
        self.guesses=self.guesses+2
        self.manually_uncover=self.manually_uncover+1

        #assigning the randomly generated pairs in grid_val

        grid_val=self.pairs

        ele_row=int(element_coordinate[1])
        ele_column=int(ord(element_coordinate[0].upper())-ord('A'))

        #uncovering the grid element for specified coordinate specified
        self.grid[ele_row][ele_column]=grid_val[ele_row][ele_column]
        #keeping note of the element uncovered
        self.lst.append(element_coordinate.upper())
        print(self.lst)
        os.system("cls")
        self.user_interface()
        count=0
        #finding if all the elements are revealed
        for i in range(len(grid_val)):
            for j in range(len(grid_val)):
                if self.grid[i][j]=='X':
                    count=count+1
        #if alll the elements have been manually uncovered then the score is 0
        if self.manually_uncover==self.size*self.size:
            print("You cheated - Loser !. You're score is 0!")


        elif count==0:
            # if self.guesses==0:
            #     print("You cheated - Loser !. You're score is 0!")
            # else:


            print("Oh! Happy Day. You've won! your score is {} ".format((self.total_guesses/self.guesses)*100))
            self.validate=True



    def reveal_all(self):
        grid_val=self.pairs
        #assigning all the values in grid_val to grid at specific cpoorrdinates and revealing the values
        for i in range(len(grid_val)):
            for j in range(len(grid_val)):
                self.grid[i][j]=grid_val[i][j]
        os.system("cls")
        self.user_interface()
        count=0
        self.validate = True
        print("You cheated - Loser !. You're score is 0!")

        # for i in range(len(grid_val)):
        #     for j in range(len(grid_val)):
        #         if self.grid[i][j]=='X':
        #             count=count+1
        #
        # if count==0:
        #     if self.guesses==0:
        #         print("You cheated - Loser !. You're score is 0!")
        #         self.validate=True
        #     else:
        #
        #         print("Oh! Happy Day. You've won! your score is {} ".format((self.total_guesses/self.guesses)*100))
        #         self.validate=True

    def new_game(self):
        #Deleting the earlier created object
        #asking for the user to enter the size of the game
        #returning the size


        del self
        while True:

            size=input("Enter the Size ")
            if int(size)==2 or int(size)==4 or int(size)==6:
                os.system("cls")
                return int(size)
            else:
                print("Size should be 2, 4 or 6")


        #new_user.reveal_all()

    # def exiting(self):
    #     os.system("cls")
    #     self.exit_menu()
    #     #self.user_interface()
    #     print("Exiting the game")

    def exit_sys(self):
        print("Exiting the game...")


        sys.exit()








# user_1 = MemoryGame(2)
# user_1.exiting()
# print(user_1.random_generate_pairs(4))
#user_1.revealing_two_elements()
#user_1.show_one()
#user_1.reveal_all()

