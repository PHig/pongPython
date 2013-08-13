# Pong
# This game can be played @ the following url
# http://www.codeskulptor.org/#user13_SlpveYUHvQ_10.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2


paddle1_vel = 0
paddle2_vel = 0
paddle1_pos = [0, 0]
paddle2_pos = [0, 0]
ball_pos = [0, 0]
ball_vel = [0, 0]


# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(movement):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [(WIDTH/2), (HEIGHT/2)]
    
    if movement == 1:
        pos = random.randrange(2, 5)
    else:
        pos = random.randrange(2, 5)
        pos =- pos
    ball_vel = [pos, random.randrange(1, 4)-8]
    

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = [HALF_PAD_WIDTH, ((HEIGHT/2) - 40)]
    paddle2_pos = [(WIDTH - HALF_PAD_WIDTH), ((HEIGHT/2) - 40)]
    paddle1_vel = 0
    paddle2_vel = 0
    ball_init(random.randrange(-1, 2))

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    
    # update paddle's vertical position, keep paddle on the screen
    
    paddle1_pos[1]=paddle1_pos[1]+paddle1_vel
    paddle2_pos[1]=paddle2_pos[1]+paddle2_vel
    if paddle1_pos[1]<=0:
       paddle1_pos[1]=0
 
    if paddle1_pos[1]>=HEIGHT-PAD_HEIGHT:
       paddle1_pos[1]=HEIGHT-PAD_HEIGHT
 
    if paddle2_pos[1]<=0:
       paddle2_pos[1]=0
 
    if paddle2_pos[1]>=HEIGHT-PAD_HEIGHT:
       paddle2_pos[1]=HEIGHT-PAD_HEIGHT
       
       
       
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    
    c.draw_line([paddle1_pos[0], paddle1_pos[1]],[paddle1_pos[0],paddle1_pos[1]+ PAD_HEIGHT], PAD_WIDTH, "White")
    c.draw_line([paddle2_pos[0], paddle2_pos[1]],[paddle2_pos[0], paddle2_pos[1]+PAD_HEIGHT], PAD_WIDTH, "White")
 
        
        
    # update ball
    
    
    
    
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    if ball_pos[0] <= paddle1_pos[0] + BALL_RADIUS + HALF_PAD_WIDTH and ball_pos[1] >= paddle1_pos[1] and ball_pos[1] <= paddle1_pos[1] + PAD_HEIGHT:
        ball_pos[0]  ==  paddle1_pos[0]
        ball_vel[0] = ball_vel[0] * - 1.1
        ball_vel[1] = ball_vel[1] *1.1
 
    if ball_pos[0] >= paddle2_pos[0] - BALL_RADIUS - HALF_PAD_WIDTH and ball_pos[1] >= paddle2_pos[1] and ball_pos[1] <= paddle2_pos[1] + PAD_HEIGHT:
        ball_pos[0]  ==  paddle2_pos[0]
        ball_vel[0] = ball_vel[0] * - 1.1
        ball_vel[1] = ball_vel[1] * 1.1
 
    if ball_pos[1] <= BALL_RADIUS :
       ball_pos[1] = BALL_RADIUS
       ball_vel[1] = ball_vel[1] * - 1
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
       ball_pos[1] = HEIGHT - BALL_RADIUS
       ball_vel[1] = ball_vel[1] * - 1
    if ball_pos[0] >= WIDTH - BALL_RADIUS:
       score1 = score1 + 1
       ball_init(0)
    if ball_pos[0] <= BALL_RADIUS:
       score2 = score2 + 1
       ball_init(1)
   
        
        
    # draw ball and scores
    
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    c.draw_text(str(score1), [WIDTH/4, HEIGHT/4], 36, "White")
    c.draw_text(str(score2), [3 * WIDTH/4, HEIGHT/4], 36, "White")
    c.draw_text("USE W & S", [WIDTH/4 - 25, HEIGHT-HEIGHT/10], 10, "White")
    c.draw_text("USE Up & Down", [3 * WIDTH/4 - 40, HEIGHT-HEIGHT/10], 10, "White") 
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 15
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel += -acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel += -acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)


# start frame
new_game()
frame.start()

