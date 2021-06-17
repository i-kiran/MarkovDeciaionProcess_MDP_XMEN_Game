import random
#generates possible actions for magneto
def generate_valid_pos_for_Magneto(x,y):
		valid_p = []
		valid = [(x-1 , y),(x , y-1),(x+1,y),(x,y+1)]
		#           left      down      right    up    
		for pos in valid:
			x_w , y_w = pos
			if x_w <=5 and y_w <=5 and x_w > 0 and y_w > 0:
				valid_p.append(pos)
		x,y  = valid_p[random.randrange(len(valid_p))]
		return(x,y)

