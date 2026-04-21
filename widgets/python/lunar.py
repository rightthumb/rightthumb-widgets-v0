#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

#A1695618-Converted



# Lunar Lander - need thrusters to rotate (like rice rocks,
# and instructions

try:
	import simplegui
except ImportError:
	import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

WIDTH = 1000
HEIGHT = 600
LANDING_PAD_LOC = [WIDTH - 150, HEIGHT -45]
LANDING_PAD_WIDTH = 100
LAUNCH_PAD_COORD = [(20, HEIGHT - 50), (120, HEIGHT - 50), (120, HEIGHT - 65), (20, HEIGHT - 65)]
LANDER_ACC = [.05, -.1]
MASTER_BLOCK_POS = [200, HEIGHT - 70]
ROWS = 12
COLUMNS = 20
BLOCK_WIDTH = 50
SCALE = 4
block_difficulty = 95
LUNAR_LANDER_WIDTH = 30
LUNAR_LANDER_HEIGHT = 40

hit_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Collision8-Bit.ogg")

def new_game():
	# Places Lunar Lander on launch pad with engines and thrusters off
	global lunar_lander_loc, lander_vel, in_flight, flame_color, right_flame_color, left_flame_color
	global main_engine_thrusting, left_engine_thrusting, right_engine_thrusting, block_difficulty
	main_engine_thrusting, left_engine_thrusting, right_engine_thrusting, in_flight = False, False, False, False
	lunar_lander_loc = [55, HEIGHT - 65]
	lander_vel = [0, 0]
	flame_color, right_flame_color, left_flame_color = "Black", "Black", "Black"
	global wall_blocks
	wall_blocks = []
	color = "White"
	for x in range(ROWS):
		good_block = True
		for y in range(COLUMNS):
			new_block = Block((MASTER_BLOCK_POS[0] + BLOCK_WIDTH*x, MASTER_BLOCK_POS[1] - 20*y), good_block, color)
			wall_blocks.append(new_block)
			higher = random.randrange(100)
			if higher > (block_difficulty - 3 * x):
				good_block = False
				
def new_game_training():
	global fuel_left, message, gravity, block_difficulty
	block_difficulty = 45
	new_game()
	message = "Training Mode"
	fuel_left = 2000
	gravity = 0.01 
	
def new_game_asteroid():
	global fuel_left, message, gravity, block_difficulty
	block_difficulty = 95
	new_game()
	message = "Asteroid"
	fuel_left = 100
	gravity = 0.007 

def new_game_moon():
	global fuel_left, message, gravity, block_difficulty
	block_difficulty = 95
	new_game()    
	message = "Moon"
	fuel_left = 150
	gravity = 0.01

def new_game_mars():
	global fuel_left, message, gravity, block_difficulty
	block_difficulty = 95
	new_game()
	fuel_left = 200
	message = "Mars" 
	gravity = 0.02
	
def new_game_earth():
	global fuel_left, message, gravity, block_difficulty
	block_difficulty = 95
	new_game()
	fuel_left = 400
	message = "Earth"    
	gravity = 0.06    

class Block:
	def __init__(self, pos, alive, color):
		self.position = pos
		self.alive = alive
		self.color = color
		
	def add_block(self, pos, alive, color):
		global wall_blocks
		self.append(pos)
		
	def get_position(self):
		return self.position
	
	def get_alive(self):
		return self.alive
	
	def kill_block(self):
		self.alive = False
	
	def get_color(self):
		return self.color
	
	def is_block_hit(self, lunar_lander_loc):
		global fuel_left
		block_position = self.position
		if self.get_alive():
			if (lunar_lander_loc[1] >= block_position[1]) and (lunar_lander_loc[0] + LUNAR_LANDER_WIDTH >= block_position[0]) and(lunar_lander_loc[0]  <= block_position[0] + BLOCK_WIDTH): 
				hit_sound.play()
				fuel_left = 0

		
	def draw(self, canvas):
		block_position = self.position
		if self.get_alive():
			canvas.draw_polygon([block_position, (block_position[0], block_position[1] + 20),
						(block_position[0] + BLOCK_WIDTH, block_position[1] + 20),
						(block_position[0] + BLOCK_WIDTH, block_position[1])], 1, self.get_color(), self.get_color())

	
	
def keydown(key):
	global lander_vel, lunar_lander_loc, fuel_left, flame_color, right_flame_color, left_flame_color
	global main_engine_thrusting, left_engine_thrusting, right_engine_thrusting
	if fuel_left > 0:
		if key == simplegui.KEY_MAP["up"]:
			main_engine_thrusting = True
			flame_color = "Red"
			ship_thrust_sound.set_volume(1)
			ship_thrust_sound.play()
		elif key == simplegui.KEY_MAP["left"]:
			right_engine_thrusting = True
			right_flame_color = "Red"
			ship_thrust_sound.set_volume(0.3)
			ship_thrust_sound.play()
		elif key == simplegui.KEY_MAP["right"]:
			left_engine_thrusting = True
			left_flame_color = "Red"
			ship_thrust_sound.set_volume(0.3)
			ship_thrust_sound.play()
	
def keyup(key):
	global flame_color, left_flame_color, right_flame_color
	global main_engine_thrusting, left_engine_thrusting, right_engine_thrusting
	if key == simplegui.KEY_MAP["up"]:
		main_engine_thrusting = False
		flame_color = "Black"
		ship_thrust_sound.pause()
	elif key == simplegui.KEY_MAP["left"]:
		right_engine_thrusting = False
		right_flame_color = "Black"
		ship_thrust_sound.pause()
	elif key == simplegui.KEY_MAP["right"]:
		left_engine_thrusting = False
		left_flame_color = "Black"
		ship_thrust_sound.pause()
		
def draw(canvas):
	
	global in_flight, fuel_left, message, gravity, flame_color, left_flame_color, right_flame_color
	global main_engine_thrusting, left_engine_thrusting, right_engine_thrusting, lander_vel
	
	# Main surface of celestial body
	canvas.draw_line((0, HEIGHT - 50), (WIDTH, HEIGHT - 50), 2, "White")
	
	# Landing pad
	canvas.draw_line(LANDING_PAD_LOC,
					(LANDING_PAD_LOC[0]+LANDING_PAD_WIDTH,
					LANDING_PAD_LOC[1]), 12, "Red")
	
	# Launch pad
	canvas.draw_polygon(LAUNCH_PAD_COORD, 1, "White", "Black")
	
	# Lunar lander body
	canvas.draw_polygon([lunar_lander_loc, (lunar_lander_loc[0] + LUNAR_LANDER_WIDTH, lunar_lander_loc[1]),
						(lunar_lander_loc[0] + LUNAR_LANDER_WIDTH / 2, lunar_lander_loc[1] - LUNAR_LANDER_HEIGHT)], 1, "Red", "White")
	
	# Navigation Lines
	if in_flight and lunar_lander_loc[0] > WIDTH / 2:
		canvas.draw_line((lunar_lander_loc[0], lunar_lander_loc[1]), LANDING_PAD_LOC, 1, "Green")
		canvas.draw_line((lunar_lander_loc[0] + LUNAR_LANDER_WIDTH, lunar_lander_loc[1]), (LANDING_PAD_LOC[0] + LANDING_PAD_WIDTH, LANDING_PAD_LOC[1]), 1, "Green")
		
	for b in wall_blocks:
		b.is_block_hit(lunar_lander_loc)
		if b.get_alive():
			b.draw(canvas) 


	# Main engine flame
	canvas.draw_polygon([(lunar_lander_loc[0] + LUNAR_LANDER_WIDTH / 3, lunar_lander_loc[1] + LUNAR_LANDER_HEIGHT * 0.05),
						(lunar_lander_loc[0] + LUNAR_LANDER_WIDTH * 2 / 3, lunar_lander_loc[1] + LUNAR_LANDER_HEIGHT * 0.05),
						(lunar_lander_loc[0] + LUNAR_LANDER_WIDTH / 2, lunar_lander_loc[1] + LUNAR_LANDER_HEIGHT / 2)], 1, flame_color, flame_color)
	
	# Thruster flames
	canvas.draw_line((lunar_lander_loc[0] - 6, lunar_lander_loc[1] - 25),
					(lunar_lander_loc[0] + 6, lunar_lander_loc[1] - 25), 5, left_flame_color)
	canvas.draw_line((lunar_lander_loc[0] + 24, lunar_lander_loc[1] - 25),
					(lunar_lander_loc[0] + 36, lunar_lander_loc[1] - 25), 5, right_flame_color)    

# Inset picture

	if lunar_lander_loc[1] < 0:
		
		# Inset Frame
		canvas.draw_polygon([(0, HEIGHT), (WIDTH / SCALE, HEIGHT), (WIDTH / SCALE, 0), (0, 0)],
							1, "White", "Black")
		
		# Inset Description
		canvas.draw_text("Extended View - 4x height", (10, 20), 20, "White")
		canvas.draw_text('"Disappears when back on main screen"', (5, 40), 16, "Red")

		# Inset Launch Pad
		canvas.draw_polygon([(20 / SCALE, HEIGHT - 50 / SCALE),
							(120 / SCALE, HEIGHT - 50 / SCALE),
							(120 / SCALE, HEIGHT - 65 / SCALE),
							(20 / SCALE, HEIGHT - 65 / SCALE)], 1, "White", "Black")
		
		# Inset ground line
		canvas.draw_line((0, HEIGHT - 50 / SCALE), (WIDTH / SCALE, HEIGHT - 50 / SCALE), 1, "White")
		
		# Inset landing pad
		canvas.draw_line((LANDING_PAD_LOC[0] / SCALE, HEIGHT - 45 / SCALE),
					((LANDING_PAD_LOC[0] + LANDING_PAD_WIDTH) / SCALE,
					HEIGHT - 45 / SCALE), 12 / SCALE, "Red")
		
		# Inset Lunar Lander
		if lunar_lander_loc[0] + 30 < WIDTH:
			canvas.draw_polygon([(lunar_lander_loc[0] / SCALE, (HEIGHT - (HEIGHT - lunar_lander_loc[1]) / SCALE)),
							((lunar_lander_loc[0] + LUNAR_LANDER_WIDTH) / SCALE, (HEIGHT - (HEIGHT - lunar_lander_loc[1]) / SCALE)),
							((lunar_lander_loc[0] + (LUNAR_LANDER_WIDTH / 2)) / SCALE, (HEIGHT - (HEIGHT - lunar_lander_loc[1] + LUNAR_LANDER_HEIGHT) / SCALE))],
							1, "Red", "White")
		
		# Inset Navigation Line
		if lunar_lander_loc[0] > WIDTH / 2:
			canvas.draw_line(((lunar_lander_loc[0] + LUNAR_LANDER_WIDTH / 2) / SCALE, (HEIGHT - (HEIGHT - lunar_lander_loc[1]) / SCALE)),
							((LANDING_PAD_LOC[0] + LANDING_PAD_WIDTH / 2) / SCALE, HEIGHT - 45 / SCALE), 1, "Green")

	
	# Fuel status notification
	canvas.draw_text("Fuel remaining: " + str(fuel_left), [280, 40], 40, "White")
	
	# Other messages
	canvas.draw_text(message, [400, 130], 60, "Blue")

	if lander_vel[1] > 1.3:
		safe_speed = False
		speed_color = "Red"
	elif 0.8 < lander_vel[1] < 1.3:
		safe_speed = True
		speed_color = "Yellow"
	else:
		safe_speed = True
		speed_color = "Green"
		
	canvas.draw_text("Vertical Speed: " + str(lander_vel[1]), [657, 40], 40, speed_color)    
	
	if (lunar_lander_loc[1] + lander_vel[1] < HEIGHT - 64) or (lunar_lander_loc[1] + lander_vel[1] < HEIGHT - 50) and lunar_lander_loc[0] > 120:
		if main_engine_thrusting:
			lander_vel[1] += LANDER_ACC[1]
			fuel_left -= 1
		if right_engine_thrusting:
			lander_vel[0] -= LANDER_ACC[0]
			fuel_left -= 0.5
		if left_engine_thrusting:
			lander_vel[0] += LANDER_ACC[0]
			fuel_left -= 0.5
		lunar_lander_loc[0] += lander_vel[0]
		lunar_lander_loc[1] += lander_vel[1]
		if lander_vel[1] <= -1:
			in_flight = True
		if in_flight:
			lander_vel[1] += gravity
			message = ""
		if fuel_left < 0:
			fuel_left = 0
			flame_color, right_flame_color, left_flame_color = "Black", "Black", "Black"
			ship_thrust_sound.pause()
			main_engine_thrusting, right_engine_thrusting, left_engine_thrusting = False, False, False 
	
	elif not safe_speed:
		message = "CRASH!"
		fuel_left = 0
		hit_sound.pause()
	elif (lunar_lander_loc[0] + 15 >= LANDING_PAD_LOC[0]) and (lunar_lander_loc[0] + 15 <= LANDING_PAD_LOC[0] + LANDING_PAD_WIDTH):
		message = "SAFE LANDING!"
		hit_sound.pause()
	elif (lunar_lander_loc[0] >= 110) and (lunar_lander_loc[0] + 15 < LANDING_PAD_LOC[0]):
		message = "CRASH!"
		fuel_left = 0
		hit_sound.pause()
	else:
		if in_flight:
			message = "CRASH!"
			fuel_left = 0
			hit_sound.pause()    

ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")            
			
frame = simplegui.create_frame("Lunar Lander", WIDTH, HEIGHT)
frame.add_button("New Game - Training (1/6 normal gravity)", new_game_training, 140)
frame.add_button("New Game - Asteroid (1/9 normal gravity)", new_game_asteroid, 140)
frame.add_button("New Game - Moon (1/6 normal gravity)", new_game_moon, 140)
frame.add_button("New Game - Mars (1/3 normal gravity)", new_game_mars, 140)
frame.add_button("New Game - Earth (normal gravity)", new_game_earth, 140)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

new_game_training()
frame.start()