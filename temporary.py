road_num1 = road(60, 30, 45, 1)
road_num2 = road(55, 23, 40, 2)
road_num3 = road(48, 35, 60, 3)			
road_num4 = road(67, 22, 70, 4)

car1 = Car(34,5, road_num1 , road_num3, 1)
car2 = Car(45,8, road_num3 , road_num4, 2)			#Cars me starting distance wala attribute add karna hai
													#Time at start wala attribute hatana hai 
car3 = Car(20,1, road_num4, road_num2, 3)

car_list = [car1, car2, car3]
#print (Disjoint_sets(car_list))
temp_array = [0,1,1,3,2]
temp_matrix = [[1,5],[5,7]]

turn = check_turn(temp_from_road_vehicle_i, temp_to_road_vehicle_i)

temp_from_road_vehicle_i = vehicle_i.from_road
temp_to_road_vehicle_i = vehicle_i.to_road
