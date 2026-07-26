def play_tictactoe():

    board = [[1,2,3],[4,5,6],[7,8,9]]
    
    def draw_board():
        print("\n")
        for i in range(3):
            print("\t| ",end ="")
            for j in range(3):
                print(f"{board[i][j]}",end=" | ")
            print("\n")

    def checkWin():
        for i in range(3):
            if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                return True
            if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                return True
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return True
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return True
        return False

    player = 1
    moves = 0

    while True:

        draw_board()
        mark = 'X' if player == 1 else 'O'

        try:
            choice = int(input(f"Player {player} ({mark}), enter a number 1-9: "))
        except ValueError:
            print("\n Invalid input! Please enter a valid number.")
            continue

        if choice >= 1 and choice <= 9 :
            row = (choice - 1) // 3
            col = (choice - 1) % 3

            if board[row][col] != 'X' and board[row][col] != 'O':
                board[row][col] = mark
                if checkWin() :
                    draw_board()
                    print(f"\n(✿◠‿◠) CONGRATULATIONS! Player { player } wins!\n")
                    break

                moves += 1

                if moves == 9 :
                    draw_board()
                    print("\nGAME OVER! It's a Draw.\n")
                    break

                player = 2 if player == 1 else 1

            else:
                print("\nCell already occupied! Try again.")

        else:
            print("\nOut of bounds! Please enter a number between 1 and 9.")

if __name__ == "__main__":
    play_tictactoe()