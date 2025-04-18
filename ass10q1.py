rows, cols = 8, 8
board = []
for k in range(rows):
    board.append([0] * cols)
for i in board:
    print(i)
a,b,c,d=1,1,1,1
for i in range(0,8):
    a,b,c,d=1,1,1,1
    row1=int(input("Enter the row"))
    col1=int(input("Enter the col"))
    for i in range(len(board)):
        if board[i][col1]==1:
            a=0
    for i in range(len(board[row1])):
        if board[row1][i]==1:
            b=0
        
    if a==b==1:
        board[row1][col1]=1
for i in board:
    print(i)