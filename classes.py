import numpy as np
non_colliding = {(1,3):[[3,1],[3,4],[4,1]],
				(1,2):[[2,1],[2,3],[2,4],[3,1],[3,4],[4,1]],
				(1,4):[[4,1]],
				(2,1):[[1,2]],
				(2,4):[[1,2],[4,1],[4,2]],
				(2,3):[[1,2],[3,1],[3,2],[3,4],[4,1],[4,2]],
				(3,1):[[1,2],[1,3],[2,3]],
				(3,2):[[2,3]],
				(3,4):[[1,2],[1,3],[2,3],[4,1],[4,2],[4,3]],
				(4,1):[[1,2],[1,3],[1,4],[2,4],[2,3],[3,4]],
				(4,2):[[2,4],[2,3],[3,4]],
				(4,3):[[3,4]]}
class Car : 
	def __init__(self, speed,  from_road, to_road, distance_from_main_line, car_num ):
		self.speed = speed 
		self.distance_from_main_line = distance_from_main_line
		self.from_road = from_road 
		self.to_road = to_road 
		self.car_num = car_num
	def getSpeed (self) :
		return self.speed 
	def getPath(self) :
		return [self.from_road.road_num , self.to_road.road_num] 
class road :
	def __init__(self, start_line ,decision_line , speed_limit, road_num ):
		self.decision_line = decision_line 
		self.start_line = start_line
		self.speed_limit = speed_limit
		self.road_num = road_num
	def decision_area_length(self) :
		return self.start_line - self.decision_line
class CrossRoad() :
	def __init__(self,road_1,road_2,road_3,road_4, width ):
		self.road_1 = road_1
		self.road_2 = road_2
		self.road_3 = road_3
		self.road_4 = road_4 
		self.width = width 


def Disjoint_sets(car_list):
	subsets = {}
	temp_list = []
	unique_templist = []
	map_carno_car = {}
	for h in car_list :
		map_carno_car[h.car_num] = h 
	#final_disjoint_subsets = []
	#print (len(car_list))
	#print(map_carno_car)
	for i in range(1,len(car_list)+1) :
		subsets[car_list[i-1]] = [car_list[i-1]]
		temp_list.append(0)
		for j in range(1,len(car_list)+1) :
			if(i != j) :
				if [car_list[j-1].from_road.road_num,car_list[j-1].to_road.road_num] not in non_colliding[(car_list[i-1].from_road.road_num,car_list[i-1].to_road.road_num)] :
					subsets[car_list[i-1]].append(car_list[j-1])
	#print(subsets)
	#print(car_list)
	temp_list.append(0)
	for k in car_list :									#repair work
		for l in subsets[k] : 
			if (temp_list[l.car_num] == 0 ) :
				temp_list[l.car_num] = k.car_num
			else :
				t = temp_list[l.car_num] 
				for u in subsets[k] :
					temp_list[u.car_num] = t
	k = temp_list[1:]
	temp_list = k
	print(temp_list)
	unique_templist = np.unique(temp_list)
	#final_disjoint = [[]]*len(unique_templist) #to be remebered
	final_disjoint=[]
	print(unique_templist)
	#z = 0
	for x in unique_templist :
		tl=[] #temporary list jisme ek iteration ki values store karna hai
		for t in range(len(temp_list)) :
			#print(temp_list[t]==x)
			#print(final_disjoint)
			if (temp_list[t] == x) :
				tl.append(map_carno_car[t+1]) 
		final_disjoint.append(tl) #poori temporary list append karna hai 		
		#z = z+1 
	return final_disjoint
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
def convert(list): 
    s = [str(i) for i in list]  # Converting integer list to string list 
    res = int("".join(s)) # Join list items using join() 
    return(res)
def Matrix_addressing(payoff_matrix,index_array,value) :
	temp_payoff_matrix = payoff_matrix
	for i in range(len(index_array) -1 ) :
		temp = temp_payoff_matrix[index_array[i]]
		temp_payoff_matrix = temp 
	temp[index_array[i+1]] = value 
	return payoff_matrix  
def read_from_matrix(matrix,index_array):
	temp = matrix
	for i in range(len(index_array)):
		temp = temp[index_array[i]]
	return temp 
def index_checking(index_array) :
	sorted_index_array = sorted(index_array)
	sorted_index_array = np.unique(sorted_index_array)
	for k in range(len(sorted_index_array)) : #order 1 se chalu karna hai ya 0 se dhyaan rakhna hai uska 
		if(sorted_index_array[0] != 0) :	#idhar 0 se chalu kar raha hu
			return False 
		if (k > 0) :
			if (sorted_index_array[k] - sorted_index_array[k-1] > 1 ) :
				return False 
	else :
		return True 
def mapping_to_vehicle_no(disjoint_subset) :
	mapping_dict = {}
	for m in len(disjoint_subset) :
		mapping_dict[m+1] : disjoint_subset[m]
	return mapping_dict 
def order_dictionary(index_array) :
	order_dictionary = {}
	sorted_index_array = sorted(index_array)
	sorted_unique_index_array = np.unique(sorted_index_array)
	for k in sorted_unique_index_array :
		order_dictionary[k] = []
		for i in range(len(index_array)) :
			if index_array[i] == k :
				order_dictionary[k].append(i) 
	return order_dictionary
def next_vehicles_to_negotiate(ordered_dictionary,last_key,key_index) :
	if len(ordered_dictionary) > 0 :
		if last_key == -1 :				
			if len(ordered_dictionary[0]) > 1 :
				vehicle_no_i = ordered_dictionary[0][0]
				vehicle_no_iplus1 = ordered_dictionary[0][1] 
				last_key = 0 
				key_index = 1
				return vehicle_no_i , vehicle_no_iplus1, last_key, key_index 
		else : 
			if (len(ordered_dictionary[last_key]) - 1 == key_index ):
				if (len(ordered_dictionary) -1 == last_key) :
					return ordered_dictionary[last_key][key_index], None , last_key+1 , 0  
				else :
					return ordered_dictionary[last_key][key_index] , ordered_dictionary[last_key+1][0] , last_key+1, 0
			else :
				return ordered_dictionary[last_key][key_index], ordered_dictionary[last_key][key_index+1], last_key, key_index+1
def check_intersecting_paths(vehicle_i,vehicle_iplus1):
	if ([vehicle_iplus1.from_road, vehicle_iplus1.to_road] not in non_colliding[(vehicle_i.from_road, vehicle_i.to_road)]) :
		return False 
	else : 							#False return karega jab nahi intersect hoga
		return True 
def check_turn(vehicle):
	turn_dict = {
				(1,3): "Straight",
				(1,2): "Left",
				(1,4): "Right",
				(2,1): "Right" ,
				(2,4): "Straight",
				(2,3): "Left",
				(3,1): "Straight",
				(3,2): "Right",
				(3,4): "Left",
				(4,1): "Left",
				(4,2): "Straight",
				(4,3): "Right"
	}
	return turn_dict[tuple(vehicle.getPath())]
def motion_equation(vehicle,CrossRoad):
	path = vehicle.getPath()

"""def check_collision(vehicle_i, vehicle_iplus1):
	if (check_intersecting_paths(vehicle_i,vehicle_iplus1) == False ) :
		return False 
	else :

	turn = check_turn([tuple(vehicle.getPath())])
	time_to_reach = vehicle.distance_from_main_line / vehicle.speed
	if (turn == "Straight") :
		if (vehicle.from_road == 1):
			y = CrossRoad.width/4 
			x = vehicle


def negotiation(vehicle_no_i, vehicle_i, vehicle_no_iplus1, vehicle_iplus1, index_array, CrossRoad) :
	if (vehicle_iplus1 == None or vehicle_i == None ) :
		pass 
	else :	
		if (index_array[vehicle_no_i] == index_array[vehicle_no_iplus1]) :
			if (check_collision(vehicle_i, vehicle_iplus1) == False) : 
				return vehicle_i, vehicle_iplus1
			else :
				vehicle_i_motion = motion_equation(vehicle_i,CrossRoad)
				vehicle_iplus1_motion = motion_equation(vehicle_iplus1,CrossRoad)
				

	"""			



