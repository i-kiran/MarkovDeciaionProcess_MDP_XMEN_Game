def diff(utility_matrix_old ,  utility_matrix_new):
	diff1 = 0
	for i in range(5):
		for j in range(5):
			diff2 = abs(utility_matrix_old[i][j] - utility_matrix_new[i][j])
			diff1 = max(diff1, diff2)
	return diff1
