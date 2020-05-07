import numpy as np
from classes import * 
def nash_equilibrium(payoff_matrix, vehicle_list) :
	size = len(vehicle_list) 
	temp = [] 
	for i in range(size) :
		temp.append(size)
	dimesnsion_tuple = tuple(temp)
	flag_matrix = np.ones(dimesnsion_tuple)
	for i in range(size) :
		for j in range(size**size) :
			index_array = numberToBase(j,size)
			leading_zeroes = []
			for t in range(size - len(index_array)) :
				leading_zeroes.append(0)
			index_array = leading_zeroes + index_array
			#print("Index Array =")
			#print(index_array)
			#print("#####")  
			temp_index_array = []
			for z in index_array :
				temp_index_array.append(z)  			
			max_value  = read_from_matrix(payoff_matrix[i], index_array)
			#print( max_value )
			#print("****")
			#print(index_array)
			for k in range(size) :
				temp_index_array[i] = k
				#print(temp_index_array)
				#print("%%%%%")
				#print(index_array)
				value = read_from_matrix(payoff_matrix[i],temp_index_array)
				if (value > max_value) :
					#print(value)
					#print("'''''")
					#print(index_array)
					flag_matrix = Matrix_addressing(flag_matrix, index_array , 0)
					#print("!!!!!")
					#print(flag_matrix)
				elif (value < max_value) :
					flag_matrix = Matrix_addressing(flag_matrix, temp_index_array, 0)
					#print("?????")
					#print(flag_matrix)
	return flag_matrix 
	
A = [[[-8,0],[-10,-1]],[[-8,-10],[0,-1]]]
vehic = [0,1]
print(nash_equilibrium(A,vehic))