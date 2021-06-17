import time
import random
import visualize
import difference
import position_generator
from visualize import create
from difference import diff
from visualize import recreate
from position_generator import generate_valid_pos_for_Magneto
freward = 0
reward1 = -15
reward2  = -20
reward3 = 20
delta = 0.05
delay = 0.4
gamma = 0.85
grid, rect, screen, width = create(5)
begin = time.time()
position_vector = [2,3,3,5,1,5]
valid_moves = [[-1,0],[1,0],[0,-1],[0,1]]
for x in range(50):
	print(position_vector)
	#update  matrix
	matrix = []
	for i in range(5):
		m = []
		for j in range(5):
			l=0
			m.append(l)
		matrix.append(m)
	magneto_x = 5-position_vector[1] 
	magneto_y = position_vector[0]-1 
	matrix[magneto_x][magneto_y] = 1#update magneto's position
	wolverine_x = 5-position_vector[3] 
	wolverine_y = position_vector[2]-1 
	matrix[wolverine_x][wolverine_y] = 2 #update wolverine's position
	jean_x = 5-position_vector[5] 
	jean_y = position_vector[4]-1
	matrix[jean_x][jean_y] = 3	 #update jean's position
	recreate(grid, rect, screen, 5, matrix, delay, width)
	utility_matrix_old = utility_matrix_new = 	[[0,0,0,0,0],
												[0,0,0,0,0],
												[0,0,0,0,0],
												[0,0,0,0,0],
												[0,0,0,0,0]]
	#updating rewards
	if (position_vector[0],position_vector[1]) == (position_vector[4],position_vector[5]):
		X =position_vector[0]-1
		Y =position_vector[1]-1
		utility_matrix_old[X][Y] = utility_matrix_new[X][Y]= reward1
	else:
		X = position_vector[0]-1
		Y = position_vector[1]-1
		utility_matrix_old[X][Y]=utility_matrix_new[X][Y] = reward2
		X1 = position_vector[4]-1
		Y1 = position_vector[5]-1
		utility_matrix_old[X1][Y1] = utility_matrix_new[X1][Y1] = reward3
	#value iteration 
	for y in range(90):
		for i in range(5):
			for j in range(5):
				U= []
				#if magneto at Wolverine's place and Wolverine at Jean's place
				if (i+1,j+1) == (position_vector[4],position_vector[5]) and (i+1,j+1) == (position_vector[0],position_vector[1]):
					reward = reward1
				# if magneto at wolverine's place	
				elif (i+1,j+1) == (position_vector[4],position_vector[5]):
					reward = reward3
				# if wolverine at jean's place
				elif (i+1,j+1) == (position_vector[0],position_vector[1]):
					reward = reward2
				else:
					reward = 0
				#if any block other than wall
				if (i+1,j+1) != (4,3):	
					#for all valid_moves calculate utilities
					for a in valid_moves:
						new_state = (i+a[0]+1,j+a[1]+1)
						x =new_state[0]
						y = new_state[1]	
						if  new_state != (4,3) and x <= 5 and y <= 5 and x > 0 and y > 0:
							move = utility_matrix_new[x-1][y-1]
							stay =  utility_matrix_new[i][j]
							utility = reward + gamma*(move*0.95 +stay*0.05)
						else:
							z =  utility_matrix_new[i][j]
							utility = reward + gamma*z
						U.append(utility)					
					utility_matrix_new[i][j] = max(U)
		#update utility matrix 
		for i in range(5):
			for j in range(5):
				utility_matrix_old[i][j] = utility_matrix_new[i][j]
		diff_ = diff(utility_matrix_old , utility_matrix_new)
		if diff_ < delta:
			break
	
	print(utility_matrix_new)
	
	#selecting the position for wolverine with max utility
	move_f = (0,0)
	max_utility = 0					
	for move in valid_moves:
		(x,y) = (position_vector[2]+move[0],position_vector[3]+move[1])
		if (x,y) != (4,3) and x <= 5 and y <= 5 and x > 0 and y > 0 :
			if utility_matrix_old[x-1][y-1] > max_utility:
				max_utility = utility_matrix_old[x-1][y-1]
				move_f = move

	# change position of wolverine

	position_vector[2] += move_f[0]
	position_vector[3] += move_f[1]

	# change position of magneto
	x,y = position_vector[0],position_vector[1]
	while(1):
		magneto_x , magneto_y = generate_valid_pos_for_Magneto(x,y)
		if((magneto_x,magneto_y) != (5,5) and (magneto_x,magneto_y)!= (4,3)):
			position_vector[0] = magneto_x
			position_vector[1] = magneto_y
			break
	# change position of jean
	if random.randint(1,100) > 80:
		if position_vector[5] == 5:
			position_vector[4] = 5
			position_vector[5] = 2
		else:
			position_vector[4] = 1
			position_vector[5] = 5
	
	x_m = position_vector[0] 
	y_m = position_vector[1]
	x_w = position_vector[2]
	y_w = position_vector[3]
	x_j = position_vector[4]
	y_j = position_vector[5]
	if (x_w,y_w) == (x_j,y_j):
		freward += reward3
		print("WINNER : Wolverine")
		break        #wolverine wins the game 
	elif (x_w,y_w) == (x_j,y_j) and (x_w,y_w) == (x_m,y_m):
		freward += reward1
	elif (x_w,y_w) == (x_m,y_m):
		freward += reward2
end = time.time()
print(end- begin)