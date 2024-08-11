#List
my_list=[5,3,2,4,1]
my_list.append(6)
my_list.remove(2)
my_list[1]=12
my_list.insert(0,"hi")
print("Updated List:",my_list)

#Dictionary
my_dict={"Name":"Raj","Age":20,"City":"Chennai"}
my_dict["Gender"]="Male"
my_dict["city"]="Madras"
del my_dict["Age"]
print("Updated Dictionary:",my_dict)

#Tuple
my_tupl=(2,3,4)
new=5
up_tupl=my_tupl+(new,)
up_tupl=my_tupl[:1]+my_tupl[2:]
mod_tupl=6
up_tupl=my_tupl[:2]+(mod_tupl,)+my_tupl[3:]
print("Updated Tuple:",up_tupl)