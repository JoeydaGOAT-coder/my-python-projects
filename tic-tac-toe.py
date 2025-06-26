import random
def main():
    win = False
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    a1 = "-"
    a2 = "-"
    a3 = "-"
    b1 = "-"
    b2 = "-"
    b3 = "-"
    c1 = "-"
    c2 = "-"
    c3 = "-"
    com = input("enter ''y'' to play against computer: ")
    print(" abc")
    print("1---")
    print("2---")
    print("3---")
    if (com == "y"):
        while not win:
            x_select()
            print(" abc")
            print("1" + a1 + b1 + c1)
            print("2" + a2 + b2 + c2)
            print("3" + a3 + b3 + c3)
            if (a1 == "X" and a2 == "X" and a3 == "X" or
                b1 == "X" and b2 == "X" and b3 == "X" or
                c1 == "X" and c2 == "X" and c3 == "X" or
                a1 == "X" and b1 == "X" and c1 == "X" or
                a2 == "X" and b2 == "X" and c2 == "X" or
                a3 == "X" and b3 == "X" and c3 == "X" or
                a1 == "X" and b2 == "X" and c3 == "X" or
                a3 == "X" and b2 == "X" and c1 == "X"):
                win = True
                print("X wins")
            else:
                computer_select()
                print(" abc")
                print("1" + a1 + b1 + c1)
                print("2" + a2 + b2 + c2)
                print("3" + a3 + b3 + c3)
                if (a1 == "O" and a2 == "O" and a3 == "O" or
                    b1 == "O" and b2 == "O" and b3 == "O" or
                    c1 == "O" and c2 == "O" and c3 == "O" or
                    a1 == "O" and b1 == "O" and c1 == "O" or
                    a2 == "O" and b2 == "O" and c2 == "O" or
                    a3 == "O" and b3 == "O" and c3 == "O" or
                    a1 == "O" and b2 == "O" and c3 == "O" or
                    a3 == "O" and b2 == "O" and c1 == "O"):
                    win = True
                    print("O wins")
    else:
        while not win:
            x_select()
            print(" abc")
            print("1" + a1 + b1 + c1)
            print("2" + a2 + b2 + c2)
            print("3" + a3 + b3 + c3)
            if (a1 == "X" and a2 == "X" and a3 == "X" or
                b1 == "X" and b2 == "X" and b3 == "X" or
                c1 == "X" and c2 == "X" and c3 == "X" or
                a1 == "X" and b1 == "X" and c1 == "X" or
                a2 == "X" and b2 == "X" and c2 == "X" or
                a3 == "X" and b3 == "X" and c3 == "X" or
                a1 == "X" and b2 == "X" and c3 == "X" or
                a3 == "X" and b2 == "X" and c1 == "X"):
                win = True
                print("X wins")
            else:
                o_select()
                print(" abc")
                print("1" + a1 + b1 + c1)
                print("2" + a2 + b2 + c2)
                print("3" + a3 + b3 + c3)
                if (a1 == "O" and a2 == "O" and a3 == "O" or
                    b1 == "O" and b2 == "O" and b3 == "O" or
                    c1 == "O" and c2 == "O" and c3 == "O" or
                    a1 == "O" and b1 == "O" and c1 == "O" or
                    a2 == "O" and b2 == "O" and c2 == "O" or
                    a3 == "O" and b3 == "O" and c3 == "O" or
                    a1 == "O" and b2 == "O" and c3 == "O" or
                    a3 == "O" and b2 == "O" and c1 == "O"):
                    win = True
                    print("O wins")
    again = input("enter 'y' to play again: ")
    if again == "y":
        main()
def x_select():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    x_move = input("enter coordinates of move for X ex. 'b3': ")
    if x_move == "a1":
        if a1 == "-":
            a1 = "X"
        else:
            print("space has already been claimed")
            x_select()
    elif x_move == "a2":
        if a2 == "-":
            a2 = "X"
        else:
            print("space has already been claimed")
            x_select()
    elif x_move == "a3":
        if a3 == "-":
            a3 = "X"
        else:
            print("space has already been claimed")
            x_select()
    elif x_move == "b1":
        if b1 == "-":
            b1 = "X"
        else:
            print("space has already been claimed")
            x_select()
    elif x_move == "b2":
        if b2 == "-":
            b2 = "X"
        else:
            print("space has already been claimed")
            x_select()
    elif x_move == "b3":
        if b3 == "-":
            b3 = "X"
        else:
            print("space has already been claimed")
            x_select()
    elif x_move == "c1":
        if c1 == "-":
            c1 = "X"
        else:
            print("space has already been claimed")
            x_select()
    elif x_move == "c2":
        if c2 == "-":
            c2 = "X"
        else:
            print("space has already been claimed")
            x_select()
    elif x_move == "c3":
        if c3 == "-":
            c3 = "X"
        else:
            print("space has already been claimed")
            x_select()
    else:
        print("you did not enter valid coordinates, please try again")
        x_select()

def o_select():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    o_move = input("enter coordinates of move for O ex. 'b3': ")
    if o_move == "a1":
        if a1 == "-":
            a1 = "O"
        else:
            print("space has already been claimed")
            o_select()
    elif o_move == "a2":
        if a2 == "-":
            a2 = "O"
        else:
            print("space has already been claimed")
            o_select()
    elif o_move == "a3":
        if a3 == "-":
            a3 = "O"
        else:
            print("space has already been claimed")
            o_select()
    elif o_move == "b1":
        if b1 == "-":
            b1 = "O"
        else:
            print("space has already been claimed")
            o_select()
    elif o_move == "b2":
        if b2 == "-":
            b2 = "O"
        else:
            print("space has already been claimed")
            o_select()
    elif o_move == "b3":
        if b3 == "-":
            b3 = "O"
        else:
            print("space has already been claimed")
            o_select()
    elif o_move == "c1":
        if c1 == "-":
            c1 = "O"
        else:
            print("space has already been claimed")
            o_select()
    elif o_move == "c2":
        if c2 == "-":
            c2 = "O"
        else:
            print("space has already been claimed")
            o_select()
    elif o_move == "c3":
        if c3 == "-":
            c3 = "O"
        else:
            print("space has already been claimed")
            o_select()
    else:
        print("you did not enter valid coordinates, please try again")
        o_select()
def computer_select():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    o_move = random.randrange(1, 10)
    if o_move == 3:
        if a1 == "-":
            a1 = "O"
        else:
            computer_select()
    elif o_move == 1:
        if a2 == "-":
            a2 = "O"
        else:
            computer_select()
    elif o_move == 2:
        if a3 == "-":
            a3 = "O"
        else:
            computer_select()
    elif o_move == 4:
        if b1 == "-":
            b1 = "O"
        else:
            computer_select()
    elif o_move == 5:
        if b2 == "-":
            b2 = "O"
        else:
            computer_select()
    elif o_move == 6:
        if b3 == "-":
            b3 = "O"
        else:
            computer_select()
    elif o_move == 7:
        if c1 == "-":
            c1 = "O"
        else:
            computer_select()
    elif o_move == 8:
        if c2 == "-":
            c2 = "O"
        else:
            computer_select()
    elif o_move == 9:
        if c3 == "-":
            c3 = "O"
        else:
            computer_select()

