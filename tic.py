from random import randint
ar=[[-1,],[2,4,5],[1,3,5],[2,5,6],[7,5,1],[1,2,3,4,6,7,8,9],[9,5,3],[4,8,5],[7,5,9],[8,5,6]]
   
def display(b):
 print('*'*8)
 print(' ||'*2)
 print(''+b[7]+'||'+b[8]+'||'+b[9])
 print(' ||'*2)
 print('*'*8)
 print(' ||'*2)
 print(''+b[4]+'||'+b[5]+'||'+b[6])
 print(' ||'*2)
 print('*'*8)
 print(' ||'*2)
 print(''+b[1]+'||'+b[2]+'||'+b[3])
 print(' ||'*2)
 print('*'*8)
board=['.','.','.','.','.','.','.','.','.','.']
y=['0','1','2','3','4','5','6','7','8','9']
def mark_selection():
 while (5):
 
  a=input('player1:enter the symbol you want ').upper()
  if a=='X':
     return('X','O')
     
  elif a=='O':
     return('O','X')
  else:
      continue 


def assigning (board,position,marker):
 board[position]=marker 
def win_check(board,m):
 return (board[7]==board[8]==board[9]==m or board[4]==board[5]==board[6]==m or board[1]==board[2]==board[3]==m or board[1]==board[4]==board[7]==m or 
   board[2]==board[5]==board[8]==m or board[3]==board[6]==board[9]==m or board[3]==board[5]==board[7]==m or board[1]==board[5]==board[9]==m)

def player_1():
   while(5):
    p=input(' Player 1, Enter the position you want to place   ')
    p=int(p)  
    if p<10 and p>0 and board[p]=='.':
      break
    else:
       print('INVALID PLACEMENT')
       continue
   assigning(board,p,player_1mark)
   a=win_check(board,player_1mark)
   if a==True:
      print('PLAYER 1 WON THE GAME')
      return True
   else:
      pass
   display(board)
def player_11(): 
   while(5):
    q=input('player 1,Enter the position of piece you want to move from ')
    q=int(q)
    p=input(' Player 1, Enter the position you want to move to ')
    p=int(p)
    if p<10 and p>0 and q<10 and q>0 and board[p]=='.' and board[q]==player_1mark and p in ar[q]:
      break
    else:
       print('INVALID MOVE,PLEASE CHECK YOUR MOVE')
       continue
   assigning(board,q,'.')
   assigning(board,p,player_1mark)
   a=win_check(board,player_1mark)
   if a==True:
      print('PLAYER 1 WON THE GAME')
      return 0
   else:
      pass
   display(board)
   player_22()
  
def player_2():
   while(5):
    p=input('player 2,Enter the position you want to place  ')
    p=int(p)
    if p>0 and p<10 and board[p]=='.':
      break
    else:
       print('INVALID PLACEMENT')
       continue
   assigning(board,p,player_2mark)
   a=win_check(board,player_2mark)
   if a==True:
      print('PLAYER 2 WON THE GAME')
      return True
   else:
      pass
   display(board)
def player_22():
   while(5):
    q=input('player 2,Enter the position of piece you want to move from ')
    q=int(q)
    p=input(' Player 2, Enter the position you want to move to ')
    p=int(p)
    if p<10 and p>0 and q<10 and q>0 and board[p]=='.' and board[q]==player_2mark and p in ar[q]:
      break
    else:
       print('INVALID MOVE,PLEASE CHECK YOUR MOVE')
       continue
   assigning(board,q,'.')
   assigning(board,p,player_2mark)
   a=win_check(board,player_2mark)
   if a==True:
      print('PLAYER 2 WON THE GAME')
      return 0
   else:
      pass
   display(board)
   player_11()
  
def display_rules ():
   print(' QUICKLY GO THROUGH THE FOLLOWING INSTRUCTIONS')
   print(' 1)BOTH THE PLAYERS WILL CHOOSE THEIR SYMBOLS (CHOOSE X or O) ')
   print(' 2)COMPUTER WILL RANDOMLY SELECT ONE PLAYER TO START THE GAME')
   print(' 3)PLAYERS WILL GET ALTERNATIVE TURNS ONE AFTER THE OTHER')
   print(' 4)EACH PLAYER WILL CHOOSE THE POSITION WHERE THEY WANT TO PLACE THEIR PIECE AND MOVE THEM LATER')
   print('THE POSITIONING IN THE BOARD IS AS FOLLOWS')
   display(y)
z=1
flag=1
while(z):
  board=['.','.','.','.','.','.','.','.','.','.']
  b='.'*10
  if(flag):
   print('WELCOME TO TIC-TAC-TOE')
   q=input('Do you want to continue Y/N   ').upper()
   if q=='Y':
      pass
   else:
      print('THANK YOU ')
      exit() 
   display_rules()
   print("OK LET'S START")
   flag=0
  m=mark_selection()
  player_1mark=m[0]
  player_2mark=m[1]
  a=randint(1,2)
  if a==1:
     print('PLAYER 1 WILL GO FIRST')
     player_1()
     player_2()
     player_1()
     player_2()
     if(player_1()):
        d=input('Do you want to play again?  ').upper()
        if d=='Y':
            continue
        else:
            print('THANK YOU ')
            exit()
     if(player_2()):
        d=input('Do you want to play again?  ').upper()
        if d=='Y':
            continue
        else:
            print('THANK YOU ')
            exit()
     player_11()
     d=input('Do you want to play again?  ').upper()
     if d=='Y':
        pass
     else:
            print('THANK YOU ')
            exit()
  else:
     print('PLAYER 2 WILL GO FIRST')
     player_2()
     player_1()
     player_2()
     player_1()
     if(player_2()):
        d=input('Do you want to play again?  ').upper()
        if d=='Y':
            continue
        else:
            print('THANK YOU ')
            exit()
     if(player_1()):
        d=input('Do you want to play again?  ').upper()
        if d=='Y':
            continue
        else:
            print('THANK YOU ')
            exit() 
     player_22()
     d=input('Do you want to play again?  ').upper()
     if d=='Y':
        pass
     else:
        print('THANK YOU ')
        exit()
