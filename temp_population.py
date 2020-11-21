import numpy as np
from classes import *								#This part is not working currently
def matrix_population(car_list,CrossRoad):
	disjoint_sets = Disjoint_sets(car_list)
	for x in disjoint_sets :
		vehicle_no_dict = mapping_to_vehicle_no(x)  # Disjoint subset ke pehle element ko vehicle 1 bola second ko 2.... 
		size = len(x)
		temp = []
		for i in range(size)+1 :  # N*N*N ... N+1 times 
			temp.append(size)
		dimension_tuple = tuple(temp)
		matrix = np.zeros(dimension_tuple)
		iterator = size**(size)
		iterator_array = [0]*(size**(size+1))			
		for i in range(size**(size)) :
			iterator = iterator - 1
			index_array = numberToBase(iterator, size) #iterator joki decimal me hai uska base change kar ke dega
			index_number = convert(index_array) #array ko nummber bana ke dega concatenate karke
			if index_checking(index_array) :
				order_dictionary = order_dictionary(index_array) # {0: [0], 1: [1, 2], 2: [4], 3: [3]} order se vehicle no ki mapping
				last_key = -1 									#directory empty hui to crash ho jaayega code
				key_index = 0 
				if len(order_dictionary[0]) == 1 : #edge case jab poore negotiation me ek hi vehicle hua to.. baad me handle karna hai 
					pass
				else :
					vehicle_no_i, vehicle_no_iplus1, last_key, key_index = next_vehicles_to_negotiate(order_dictionary,last_key, key_index)
					if vehicle_no_i == None or vehicle_no_iplus1 == None  :
						if vehicle_no_i == None :
							vehicle_i = None 
						if vehicle_no_iplus1 == None :
							vehicle_iplus1 == None 
					else :
						vehicle_i = vehicle_no_dict[vehicle_no_i]
						vehicle_iplus1 = vehicle_no_dict[vehicle_no_iplus1]
						vehicle_i , vehicle_iplus1 = negotiation(vehicle_no_i, vehicle_i,vehicle_no_iplus1, vehicle_iplus1,index_array, CrossRoad )											
			else :				#index checking wala else
				Matrix_Addressing(matrix, index_array, 0) 				#matrix me Vehicle no 1  0 se address hoga
								





