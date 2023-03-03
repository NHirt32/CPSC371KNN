import math
import copy
import mushroom
import file_reader
import input_switcher as insw


class InvalidDataDimensionException(Exception):
    "Exception raised when euclidean distance is calculated on different dimension length"
    pass


def switch_input(sample_data_list):
    numeric_switch = insw.input_switcher()

    for mushroom in sample_data_list:
        for i in range(len(mushroom)):
            mushroom[i] = numeric_switch.switch(mushroom[i])

    return sample_data_list


def euclidean_distance(list1, list2):
    if len(list1) != len(list2):
        raise InvalidDataDimensionException

    eucl_dist = 0

    for i in range(len(list1)):
        eucl_dist += math.pow((list1[i] - list2[i]), 2)

    return math.sqrt(eucl_dist)


def determine_status(nearest_neighbors):
    e_count = 0
    p_count = 0

    for neighbor in nearest_neighbors:
        if neighbor[0] == 4:
            e_count += 1
        else:
            p_count += 1

    # If there are more poisonous or even poisonous return 'p'
    if p_count >= e_count:
        return 'p'
    else:
        return 'e'


def k_nn(sample_data, unknown_data, k):
    status_lists = []
    for unknown in unknown_data:
        max_dist = float('-inf')
        nearest_neighbors = []
        for sample in sample_data:
            temp = copy.deepcopy(sample)
            status = temp.pop(0)
            dist = euclidean_distance(unknown, temp)
            if len(nearest_neighbors) < k:
                if dist > max_dist:
                    max_dist = dist
                nearest_neighbors.append((status, dist))
            else:
                if dist < max_dist:
                    for i in range(k):
                        if nearest_neighbors[i][1] == max_dist:
                            nearest_neighbors[i] = (status, dist)
                            break
                    max_dist = float('-inf')
                    for i in range(k):
                        if nearest_neighbors[i][1] > max_dist:
                            max_dist = nearest_neighbors[i][1]

        status_lists.append(determine_status(nearest_neighbors))
        # print(nearest_neighbors)
    return status_lists


print("Reading Known Sample Data...")

sample_data_list = file_reader.file_read("MushroomData_8000.txt")
sample_data_list = switch_input(sample_data_list)
# for data in sample_data_list:
#     print(data)

print("Reading Unknown Test Data...")

unknown_data_list = file_reader.file_read("MushroomData_Unknwon_100.txt")
unknown_data_list = switch_input(unknown_data_list)
# for mushrooms in unknown_mushroom_list:  # Debug printing
#     print(mushrooms)

print("Using KNN method to determine predicted value...")

predicted_statuses = k_nn(sample_data_list, unknown_data_list, 5)

print(predicted_statuses)

print("Writing predicted results to file.")

output_file = open("predictionResultKNN.txt", "w")
output_file.truncate(0)
for prediction in predicted_statuses:
    output_file.write(prediction + "\n")
output_file.close()

print("End of program")
