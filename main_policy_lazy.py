import time
import random
import policy
import visualize
import position_generator
from visualize import create
from visualize import recreate
from position_generator import generate_valid_pos_for_Magneto
from policy import randompolicy
from policy import newpolicy
valid_moves = [[-1,0],[1,0],[0,-1],[0,1]]
freward = 0
reward1 = -15
reward2  = -20
reward3 = 20
delta = 0.5
gamma = 0.85
position_vector = [2,3,3,5,5,2]
#				    B   A  Jean
delay = 0.3
grid, lent, screen, wid = create(5)
n_iter = 80
begin = time.time()
#outer loop, each iteration means one step of all players
for z in range(n_iter):
	print(position_vector)
	#set updated positions of all players on the board
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
	
	recreate(grid, lent, screen, 5, matrix, delay, wid)
	pi  = randompolicy()
	#print(pi)
	n_pi = newpolicy()
	while(True):
		utility_matrix_old = utility_matrix_new = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
					  
		#updating utility matrix if initailly any reward exists
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
		#  policy iteration 
		for x in range(40):			
			for i in range(5):
				for j in range(5):									
					if (i+1,j+1) == (position_vector[4],position_vector[5]) and (i+1,j+1) == (position_vector[0],position_vector[1]):
						reward = reward1
					elif (i+1,j+1) == (position_vector[4],position_vector[5]):
						reward = reward3
					elif (i+1,j+1) == (position_vector[0],position_vector[1]):
						reward = reward2
					else:
						reward = 0
					#if not wall
					if (i+1,j+1) != (4,3):
						if pi[i][j] == 'n':
							a = [0,-1]
						elif pi[i][j] == 's':
							a = [0,1]
						elif pi[i][j] == 'w':
							a = [-1,0]
						elif pi[i][j] == 'e':
							a = [1,0]
							
						state = (i+a[0]+1,j+a[1]+1)
							
						if  state != (4,3) and state[0] <= 5 and state[1] <= 5 and state[0] > 0 and state[1] > 0:
							stay = utility_matrix_new[i][j]
							y_move = state[1]-1
							x_move = state[0]-1
							U = reward + gamma*(utility_matrix_new[x_move][y_move]*0.95 + stay*0.05)
						else:
							no_update = utility_matrix_new[i][j]
							U = reward + gamma*no_update
						
						#update utility matrix with max utility
						utility_matrix_new[i][j] = U
			#checking max diff 
			diff = 0
			for i in range(5):
				for j in range(5):
					diff = max(diff, abs(utility_matrix_old[i][j] - utility_matrix_new[i][j]))
			
			#updating old matrix 
			for i in range(5):
				for j in range(5):
					old = utility_matrix_old[i][j]
					new = utility_matrix_new[i][j]
					old = new

			#checking max diff
			if diff == delta:
				break

			for i in range(5):
				for j in range(5):					
					max_val = 0
					if  (i-1,j) != (4,3) and i-1 < 5 and j < 5 and i-1 >= 0 and j >= 0:
						max_val = utility_matrix_old[i-1][j]
						n_pi[i][j] = 'w'
					if  i+1 < 5 and j < 5 and i+1 >= 0 and j >= 0 and  (i+1,j) != (4,3):
						if max_val < utility_matrix_old[i+1][j]:
							max_val = utility_matrix_old[i+1][j]
							n_pi[i][j] = 'e'
					if  i < 5 and j-1 < 5 and i >= 0 and j-1 >= 0 and  (i,j-1) != (4,3):
						if max_val < utility_matrix_old[i][j-1]:
							max_val = utility_matrix_old[i][j-1]
							n_pi[i][j] = 'n' 
					if i < 5 and j+1 < 5 and i >= 0 and j+1 >= 0 and  (i,j+1) != (4,3):
						if max_val < utility_matrix_old[i][j+1]:
							max_val = utility_matrix_old[i][j+1]
		if n_pi == pi:
			break
			
		for i in range(5):
			for j in range(5):
				pi[i][j] = n_pi[i][j]
	print(pi)
	x =  random.randint(1,100)#for wolverine
	if x <= 95:
		#print("++++++",position_vector[2]-1)
		#print("++++++",position_vector[3]-1)
		if pi[position_vector[2]-1][position_vector[3]-1] == 'w':
			position_vector[2] -= 1
		elif pi[position_vector[2]-1][position_vector[3]-1] == 'e':
			position_vector[2] += 1
		elif pi[position_vector[2]-1][position_vector[3]-1] == 'n':
			position_vector[3] -= 1
		elif pi[position_vector[2]-1][position_vector[3]-1] == 's':
			position_vector[3] += 1
	
	z =  random.randint(1,100)#for magneto
	if z <= 95:	
		x,y = position_vector[0],position_vector[1]
		while(1):
			x_m , y_m = generate_valid_pos_for_Magneto(x,y)
			if((x_m,y_m) != (5,5) and (x_m,y_m)!= (4,3)):
				position_vector[0] = x_m
				position_vector[1] = y_m
				break
		
	z =  random.randint(1,100)#for jean
	if z > 80:
		if position_vector[5] == 5:
			position_vector[4] = 5
			position_vector[5] = 2
		else:
			position_vector[4] = 1
			position_vector[5] = 5
		
	if (position_vector[2],position_vector[3]) == (position_vector[4],position_vector[5]) and (position_vector[2],position_vector[3]) == (position_vector[0],position_vector[1]):
		freward += reward1
	elif (position_vector[2],position_vector[3]) == (position_vector[4],position_vector[5]):
		freward += reward3
		print('Winner : wolverine')
		break
	elif (position_vector[2],position_vector[3]) == (position_vector[0],position_vector[1]):
		freward += reward2
	
end = time.time()
print(end- begin)
