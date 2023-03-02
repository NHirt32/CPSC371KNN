import mushroom
import file_reader
import input_switcher as insw


def switch_input(sample_data_list):
    numeric_switch = insw.input_switcher()

    for mushroom in sample_data_list:
        for i in range(len(mushroom)):
            mushroom[i] = numeric_switch.switch(mushroom[i])

    return sample_data_list


# Here we create a list of chars of mushroom characteristics from our known mushroom data
# and then convert that into a list of mushroom objects
sample_data_list = file_reader.file_read("MushroomData_8000.txt")
mushroom_list = mushroom.mushroom_list_create(sample_data_list)

# for mushrooms in mushroom_list:  # Debug printing
#     print(mushrooms)

sample_data_list = switch_input(sample_data_list)
print(sample_data_list)

# Here we create a list of chars of mushroom characteristics from our unknown mushroom data,
# add in a '?" to represent our unknown class data, and then convert that into a list of mushroom objects
unknown_data_list = file_reader.file_read("MushroomData_Unknwon_100.txt")
# Adding ? to our class component of unknown mushrooms
for index in range(len(unknown_data_list)):
    unknown_data_list[index].insert(0, '?')
unknown_mushroom_list = mushroom.mushroom_list_create(unknown_data_list)
# for mushrooms in unknown_mushroom_list:  # Debug printing
#     print(mushrooms)
