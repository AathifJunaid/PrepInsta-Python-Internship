###Please Magzimize the screen to play the game###

from tkinter import *
import random as rn


game_width = 1000
game_height = 1000
speed = 80
space_size = 20
body_parts = 2
snake_colour = "green"
food_colour = "red"
backgrond_colour = "white"



class Snake:
    
    
    def __init__(self):
        self.body_size = body_parts
        self.coordinates = []
        self.squares =[]
        
        for i in range(0,body_parts):
            self.coordinates.append([0,0])
            
        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y,x+space_size,y+space_size,fill=snake_colour,tag ="snake")
            self.squares.append(square)
            
        


class Food:
    
    def __init__(self):
        x = rn.randint(0,40)*space_size
        y = rn.randint(0,40)*space_size
        
        self.coordinates = [x,y]
        
        canvas.create_rectangle(x,y,x+space_size,y+space_size,fill = food_colour,tag = "food")
        
        


def change_direction(next_direction):
    
    
    global direction  
    
    if next_direction == 'left':
        if direction!= 'right':
            direction = next_direction
            
    elif next_direction == 'right':
        if direction!= 'left':
            direction = next_direction
            
    elif next_direction == 'up':
        if direction!= 'down':
            direction = next_direction
    
    elif next_direction == 'down':
        if direction!= 'up':
            direction = next_direction



def turn(snake,food):
    
    x,y = snake.coordinates[0]
    
    
    if direction == "up":
        y -= space_size
        
    elif direction == "down":
        y+= space_size
        
    elif direction == "left":
        x -= space_size
        
    elif direction == "right":
        x += space_size
        
        
    snake.coordinates.insert(0,(x,y))
    square = canvas.create_rectangle(x,y,x+space_size,y+space_size,fill=snake_colour)
    
    snake.squares.insert(0,square)
    
    if(x==food.coordinates[0] and y == food.coordinates[1]):
        global score 
        score += 1

        label.config(text = "Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1] 
        
    if check_collisions(snake):
        gameover()
    else:
        game.after(speed,turn,snake,food)
    
    

def check_collisions(snake):
    x,y = snake.coordinates[0]
    
    if x < 0 or x >= game_width:
        return True
    elif y < 0 or y >= game_height:
        return True
    for body_parts in snake.coordinates[1:]:
        if x == body_parts[0] and y == body_parts[1]:
            return True
    return False

def gameover():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=("New Times Roman",40),text = "Game Over",fill = "red")



game = Tk()

game.title("Snake Game")

score = 0

direction = "down"

label = Label(game,text = "Score:{}".format(score),font =("Times New Roman",20))
label.pack()

canvas = Canvas(game,bg=backgrond_colour,height=game_height,width=game_width)
canvas.pack()

game.update()

game_width = game.winfo_width()
game_height = game.winfo_height()
screen_width = game.winfo_screenwidth()
screen_height = game.winfo_screenheight()

x = int((screen_width/2) -(game_width/2))
y = int((screen_height/2) -(game_height/2))


game.geometry(f"{game_width}x{game_height}+{x}+{y}")

game.bind("<Left>", lambda event: change_direction('left'))
game.bind("<Right>", lambda event: change_direction('right'))
game.bind("<Up>", lambda event: change_direction('up'))
game.bind("<Down>", lambda event: change_direction('down'))

snake = Snake()
food = Food()

turn(snake,food)


game.mainloop()