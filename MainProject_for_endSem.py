# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:15:14 2020

@author: patan
"""
import time, os, PyPDF2
from Crypto.Cipher import AES
from tkinter import Tk,Button,Label 
from tkinter import Canvas 
from random import randint 
import pygame
import random
root = Tk() 
canvas = Canvas(root, width=600, height=600) 
canvas.pack() 
class Ball: 
	
	# for creation of ball on the canvas 
	def __init__(self, canvas, x1, y1, x2, y2): 
		self.x1 = x1 
		self.y1 = y1 
		self.x2 = x2 
		self.y2 = y2 
		self.canvas = canvas 
		
		# for creation of ball object 
		self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, 
												fill = "red",tags = 'dot1') 
	
	# for moving the ball 
	def move_ball(self): 
		
		# defining offset 
		offset = 10
		global limit 
		
		# checking if ball lands ground or bar 
		if limit >= 510: 
			global dist,score,next
			
			# checking that ball falls on the bar 
			if(dist - offset <= self.x1 and
			dist + 40 + offset >= self.x2): 
					
				# incrementing the score 
				score += 10
				
				# dissappear the ball 
				canvas.delete('dot1') 
				
				# calling the function for again 
				# creation of ball object 
				ball_set() 
				
			else: 
				# dissappear the ball 
				canvas.delete('dot1') 
				bar.delete_bar(self) 
				
				# display the score 
				score_board() 
			return
			
		# incrementing the vertical distance 
		# travelled by ball by deltay 
		limit += 1
		
		# moving the ball in vertical direction 
		# by taking x=0 and y=deltay 
		self.canvas.move(self.ball,0,1) 
		
		# for continuous moving of ball again call move_ball 
		self.canvas.after(10,self.move_ball) 
		
# class for creating and moving bar		 
class bar: 
	
	# method for creating bar 
	def __init__(self,canvas,x1,y1,x2,y2): 
		self.x1 = x1 
		self.y1 = y1 
		self.x2 = x2 
		self.y2 = y2 
		self.canvas = canvas 
		
		# for creating bar using create_rectangle 
		self.rod=canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, 
												fill="yellow",tags='dot2') 
	
	# method for moving the bar 
	def move_bar(self,num): 
		global dist 
		
		# checking the forward or backward button 
		if(num == 1): 
			
			# moving the bar in forward direction by 
			# taking x-axis positive distance and 
			# taking vertical distance y=0 
			self.canvas.move(self.rod,20,0) 
			
			# incrementing the distance of bar from x-axis 
			dist += 20
		else: 
			
			# moving the bar in backward direction by taking x-axis 
			# negative distance and taking vertical distance y=0 
			self.canvas.move(self.rod,-20,0) 
			
			# decrementing the distance of bar from x-axis 
			dist-=20
	
	def delete_bar(self): 
		canvas.delete('dot2') 
		

# Function to define the dimensions of the ball 
def ball_set(): 
	global limit 
	limit=0
	
	# for random x-axis distance from 
	# where the ball starts to fall	 
	value = randint(0,570) 
	
	# define the dimensions of the ball 
	ball1 = Ball(canvas,value,20,value+30,50) 
	
	# call function for moving of the ball 
	ball1.move_ball() 

# Function for displaying the score 
# after getting over of the game 
def score_board(): 
	root2 = Tk() 
	root2.title("Catch the ball Game") 
	root2.resizable(False,False) 
	canvas2 = Canvas(root2,width=300,height=300) 
	canvas2.pack() 
	
	w = Label(canvas2,text="\nOOPS...GAME IS OVER\n\nYOUR SCORE = "
											+ str(score) + "\n\n") 
	w.pack() 
	
	button3 = Button(canvas2, text="PLAY AGAIN", bg="green", 
						command=lambda:play_again(root2)) 
	button3.pack() 
	
	button4 = Button(canvas2,text="EXIT",bg="green", 
					command=lambda:exit_handler(root2)) 
	button4.pack() 

# Function for handling the play again request 
def play_again(root2): 
	root2.destroy() 
	main1() 

# Function for handling exit request 
def exit_handler(root2): 
	root2.destroy() 
	root.destroy() 

# Main function 
#r7
def main1(): 
	global score,dist 
	score = 0
	dist = 0
	
	# defining the dimensions of bar	 
	bar1=bar(canvas,5,560,45,575) 
	
	# defining the text,colour of buttons and 
	# also define the action after click on 
	# the button by calling suitable methods 
	button = Button(canvas,text="==>", bg="green", 
					command=lambda:bar1.move_bar(1)) 
					
	# placing the buttons at suitable location on the canvas 
	button.place(x=300,y=580) 
	
	button2 = Button(canvas,text="<==",bg="green", 
					command=lambda:bar1.move_bar(0)) 
	button2.place(x=260,y=580) 
	
	# calling the function for defining 
	# the dimensions of ball 
	ball_set() 
	root.mainloop() 
#r7
def playball():
   
    root.title("Catch the ball Game") 
    root.resizable(False,False) 
    
    # for defining the canvas 
    
    
    # variable for the vertical distance 
    # travelled by ball 
    limit = 0
    
    # variable for horizontal distance 
    # of bar from x-axis 
    dist = 5
    
    # variable for score 
    score = 0
    main1()
    retscore='scoreofballplaygameis'
    score=score*100
    remlen=16-len(str(score))
    remscore=''
    remscore=remscore+str(score)
    for i in range(remlen):
        remscore=remscore+retscore[i]
        
   # print(remscore)
    return remscore

def drawBoard(board):
     # This function prints out the board that it was passed.
     # "board" is a list of 10 strings representing the board (ignore index 0)

    print('   |   |')

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

    print('   |   |')

    print('-----------')
    print('   |   |')

    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('   |   |')

    print('-----------')

    print('   |   |')

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

    print('   |   |')



def inputPlayerLetter():

     # Lets the player type which letter they want to be.

     # Returns a list with the player’s letter as the first item, and the computer's letter as the second.

     letter = ''
     while not (letter == 'X' or letter == 'O'):
         print('Do you want to be X or O?')
         letter = input().upper()
     # the first element in the list is the player’s letter, the second is the computer's letter.
     if letter == 'X':
         return ['X', 'O']
     else:
         return ['O', 'X']
def whoGoesFirst():
     # Randomly choose the player who goes first.
     if random.randint(0, 1) == 0:
         return 'computer'
     else:
         return 'player'
def playAgain():
     # This function returns True if the player wants to play again, otherwise it returns False.
     print('Do you want to play again? (yes or no)')
     return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
     # Given a board and a player’s letter, this function returns True if that player has won.
     # We use bo instead of board and le instead of letter so we don’t have to type as much.
     return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top

    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle

    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom

    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side

    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle

    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side

    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal

    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
def getBoardCopy(board):
     # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)



    return dupeBoard
def isSpaceFree(board, move):
     # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
     # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
           print('What is your next move? (1-9)')

           move = input()
           

    return int(move)

def chooseRandomMoveFromList(board, movesList):
      # Returns a valid move from the passed list on the passed board.
     # Returns None if there is no valid move.
     possibleMoves = []

     for i in movesList:

         if isSpaceFree(board, i):

             possibleMoves.append(i)



     if len(possibleMoves) != 0:

         return random.choice(possibleMoves)

     else:

         return None



def getComputerMove(board, computerLetter):
# Given a board and the computer's letter, determine where to move and return that move.
     if computerLetter == 'X':

         playerLetter = 'O'

     else:

         playerLetter = 'X'



     # Here is our algorithm for our Tic Tac Toe AI:

     # First, check if we can win in the next move

     for i in range(1, 10):

         copy = getBoardCopy(board)

         if isSpaceFree(copy, i):

             makeMove(copy, computerLetter, i)

             if isWinner(copy, computerLetter):

                 return i



     # Check if the player could win on their next move, and block them.

     for i in range(1, 10):

         copy = getBoardCopy(board)

         if isSpaceFree(copy, i):

             makeMove(copy, playerLetter, i)

             if isWinner(copy, playerLetter):

                 return i



     # Try to take one of the corners, if they are free.

     move = chooseRandomMoveFromList(board, [1, 3, 7, 9])

     if move != None:

         return move



     # Try to take the center, if it is free.

     if isSpaceFree(board, 5):

         return 5



     # Move on one of the sides.

     return chooseRandomMoveFromList(board, [2, 4, 6, 8])



def isBoardFull(board):

     # Return True if every space on the board has been taken. Otherwise return False.

     for i in range(1, 10):

         if isSpaceFree(board, i):

             return False

     return True
#r5
def snake():
    pygame.init()

    # Colors
    white = (255, 255, 255) # rgb format
    red = (255, 0, 0)
    black = (0, 0, 0)
    
    # Creating window
    screen_width = 900
    screen_height = 600
    gameWindow = pygame.display.set_mode((screen_width, screen_height))
    
    # Game Title
    pygame.display.set_caption("BSc Game Locker")
    pygame.display.update()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 55)
    

    def text_screen(text, color, x, y):
        screen_text = font.render(text, True, color)
        gameWindow.blit(screen_text, [x,y])

    
    def plot_snake(gameWindow, color, snk_list, snake_size):
        for x,y in snk_list:
            pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
    
    # Game Loop
    def gameloop():
        pygame.init()
        exit_game = False
        game_over = False
        snake_x = 45
        snake_y = 55
        velocity_x = 0
        velocity_y = 0
        snk_list = []
        snk_length = 1
    
        food_x = random.randint(20, screen_width-20)
        food_y = random.randint(60, screen_height -20)
        score = 0
        init_velocity = 4
        snake_size = 30
        fps = 60   # fps = frames per second
        while not exit_game:
            if game_over:
                gameWindow.fill(white)
                text_screen("Game Over! Press Enter To Continue", red, 100, 250)
    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            gameloop()
    
            else:
    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            velocity_x = init_velocity
                            velocity_y = 0
    
                        if event.key == pygame.K_LEFT:
                            velocity_x = - init_velocity
                            velocity_y = 0
    
                        if event.key == pygame.K_UP:
                            velocity_y = - init_velocity
                            velocity_x = 0
    
                        if event.key == pygame.K_DOWN:
                            velocity_y = init_velocity
                            velocity_x = 0
    
                snake_x = snake_x + velocity_x
                snake_y = snake_y + velocity_y
    
                if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                    score +=1
                    food_x = random.randint(20, screen_width - 30)
                    food_y = random.randint(60, screen_height - 30)
                    snk_length +=5
    
                gameWindow.fill(white)
                text_screen("Score: " + str(score * 100), red, 5, 5)
                pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
                pygame.draw.line(gameWindow, red, (0,40), (900,40),5)
    
                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)
    
                if len(snk_list)>snk_length:
                    del snk_list[0]
    
                if head in snk_list[:-1]:
                    game_over = True
    
                if snake_x<0 or snake_x>screen_width-20 or snake_y<50 or snake_y>screen_height-20:
                    game_over = True
                plot_snake(gameWindow, black, snk_list, snake_size)
            pygame.display.update()
            clock.tick(fps)
        pygame.quit()
        retscore='scoreofgamesnakeis'
        #200scoreofgame
        scor=score*100
        #lenofscr=len(str(scor))
        remlen=16-len(str(scor))
        remscore=''
        remscore=remscore+str(scor)
        for i in range(remlen):
            remscore=remscore+retscore[i]
       
        return remscore  
    score=gameloop()
    return score    
def keyexporshrt(user):
    key=user
    user=list(user)
    
    le=len(user)
    if(le<16):
        le1=16-le
        for i in range(le1):
            key=key+user[i%le]
    elif(le>16):
        key=key[:16]
    
    
            
    return key 
def encryptaes(pt,key):
    #print(pt,key)
    
    pt=pt.encode('utf8')
    key=key.encode('utf8')
    #b'hiihello'
    #print(pt,key)
    iv = 'This is an IV456'.encode("utf8")              
    aes = AES.new(key, AES.MODE_CBC,iv)    
    encd = aes.encrypt(pt)
    print(encd)
    return encd


def tictoe():
    
    
    print('Welcome to Tic Tac Toe!')
    
    l1=[]
    
    while True:
    
         # Reset the board
    
         theBoard = [' '] * 10
    
         playerLetter, computerLetter = inputPlayerLetter()
    
         turn = whoGoesFirst()
    
         print('The ' + turn + ' will go first.')
    
         gameIsPlaying = True
    
    
    
         while gameIsPlaying:
    
             if turn == 'player':
    
                 # Player’s turn.
    
                 drawBoard(theBoard)
    
                 move = getPlayerMove(theBoard)
                 l1.append(move)
                 makeMove(theBoard, playerLetter, move)
    
    
    
                 if isWinner(theBoard, playerLetter):
    
                     drawBoard(theBoard)
    
                     print('Hooray! You have won the game!')
    
                     gameIsPlaying = False
    
                 else:
    
                     if isBoardFull(theBoard):
    
                         drawBoard(theBoard)
    
                         print('The game is a tie!')
    
                         break
    
                     else:
    
                         turn = 'computer'
    
    
    
             else:
    
                 # Computer’s turn.
    
                 move = getComputerMove(theBoard, computerLetter)
    
                 makeMove(theBoard, computerLetter, move)
    
    
    
                 if isWinner(theBoard, computerLetter):
    
                     drawBoard(theBoard)
    
                     print('The computer has beaten you! You lose.')
    
                     gameIsPlaying = False
    
                 else:
    
                     if isBoardFull(theBoard):
    
                         drawBoard(theBoard)
    
                         print('The game is a tie!')
    
                         break
    
                     else:
    
                         turn = 'player'
    
        
    
         if not playAgain():
             retscore='scoreofgametictoeis'
             #scoreofgametic200
             remlen=16-len(l1)
             remscore=''
             for i in l1:
                 remscore=remscore+str(i)
             for i in range(remlen):
                 remscore=remscore+retscore[i]
             #print(remscore)     
           
             #print(l1)
                 #200scoreofgame
             break
    return remscore      

        


    
    
    
    
def fileencrypt():
    input_file="sample.pdf"
    print("Please Enter Password To encrypt")
    user_pwrd=input()
    user_key=keyexporshrt(user_pwrd)
    owner_pwrd="helllo"
    owner_key=keyexporshrt(owner_pwrd)
    print("Games are Loading....\n")
    print("Press 1 for Snake Game\nPress 2 for tic Toe\nPress 3 for Catch a Ball")
    inpgame=int(input())
    if(inpgame==1):
        seckey=snake()
    elif(inpgame==2):
        seckey=tictoe()
    elif(inpgame==3):
        seckey=playball()
    print("Encryption is processing......")
    #r9
    #print(seckey)
    user_pass=str(encryptaes(user_key,seckey))
    owner_pass=str(encryptaes(owner_key,seckey))
    #r1
    #temporary output file with name same as input file but prepended
    # by "temp_", inside same direcory as input file.
    path, filename = os.path.split(input_file)
    #print(filename)
    output_file = os.path.join(path, "temp_" + filename)

    output = PyPDF2.PdfFileWriter()
    pdf_in=open(input_file,"rb")
    input_stream = PyPDF2.PdfFileReader(pdf_in)
    #print(input_stream)
    for i in range(0, input_stream.getNumPages()):
        output.addPage(input_stream.getPage(i))

    outputStream = open(output_file, "wb")
    #print(outputStream)
    # Set user and owner password to pdf file
    
    output.encrypt(user_pass, owner_pass, use_128bit=True)
    output.write(outputStream)
    outputStream.close()
    
    # Rename temporary output file with original filename, this
    # will automatically delete temporary file
    pdf_in.close()
    os.remove(input_file)
    os.rename(output_file, input_file)
    print("File Encrypted Successfully")
    return user_pass
def filedecrypt():
    out = PyPDF2.PdfFileWriter() 
    input_file="sample.pdf"
    print("Enter password")
    user_pwrd=input()
    
    user_key=keyexporshrt(user_pwrd)
    print("Games are Loading....\n")
    print("Press 1 for Snake Game\nPress 2 for tic Toe\nPress 3 for Catch a Ball")
    inpgame=int(input())
    if(inpgame==1):
        seckey=snake()
    elif(inpgame==2):
        seckey=tictoe()
    elif(inpgame==3):
        seckey=playball()
    print("Decryption is processing......")
    
    #print(seckey)
    user_pass=str(encryptaes(user_key,seckey))
    #user_pass=decryptaes(ciph,seckey)
    
    #print(user_pass)
    # Open encrypted PDF file with the PdfFileReader 
    file = PyPDF2.PdfFileReader(input_file) 
    
    # Store correct password in a variable password. 
    password = user_pass
    
    # Check if the opened file is actually Encrypted 
    if file.isEncrypted: 
    
    	# If encrypted, decrypt it with the password 
    	file.decrypt(password) 
    
    	# Now, the file has been unlocked. 
    	# Iterate through every page of the file 
    	# and add it to our new file. 
    	for idx in range(file.numPages): 
    		
    		# Get the page at index idx 
    		page = file.getPage(idx) 
    		
    		# Add it to the output file 
    		out.addPage(page) 
    	
    	# Open a new file "myfile_decrypted.pdf" 
    	with open(input_file, "wb") as f: 
    		
    		# Write our decrypted PDF to this file 
    		out.write(f) 
    
    	# Print success message when Done 
    	print("File decrypted Successfully.") 
    else: 
    	
    	# If file is not encrypted, print the 
    	# message 
    	print("File already decrypted.") 
        
            
    
    
    
    
    
print("***** Hi, Welcome To Game Locker *****\n")
print("Here is the Menu Loding.....")
time.sleep(2)
print("If you wish to Encrypt A File Press 1\n               Decrypt A File Press 2")
userinpt1=int(input())
if(userinpt1==1):
    fileencrypt()
elif(userinpt1==2):
    filedecrypt()    
