import mushroom
import file_reader

# Here we create a list of chars of mushroom characteristics from our known mushroom data
# and then convert that into a list of mushroom objects
sample_data_list = file_reader.file_read("MushroomData_8000.txt")
mushroom_list = mushroom.mushroom_list_create(sample_data_list)
for mushrooms in mushroom_list: # Debug printing
    print(mushrooms.classes)

# Here we create a list of chars of mushroom characteristics from our unknown mushroom data,
# add in a '?" to represent our unknown class data, and then convert that into a list of mushroom objects
unknown_data_list = file_reader.file_read("MushroomData_Unknwon_100.txt")
for index in range(len(unknown_data_list)): # Adding ? to our class component of unknown mushrooms
    unknown_data_list[index].insert(0, '?')
unknown_mushroom_list = mushroom.mushroom_list_create(unknown_data_list)
for mushrooms in unknown_mushroom_list: # Debug printing
    print(mushrooms.classes)