import math
#generates possible actions for magneto
def generate_valid_pos_for_Magneto(x,y,a,b):
	valid_p = {}
	valid = [(x-1 , y),(x , y-1),(x+1,y),(x,y+1)]
	#           left      down      right    up
	for p in valid:
		x_w , y_w = p
		if x_w <=5 and y_w <=5 and x_w > 0 and y_w > 0:
			valid_p[p] = math.dist([x_w , y_w] , [a  ,b])
	minval = min(valid_p.values())
	print(valid_p)
	print(minval)
	for k, v in valid_p.items():
		if v==minval:
			#print(k)
			return k

