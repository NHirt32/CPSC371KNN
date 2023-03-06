import math
import copy
import mushroom
import file_reader
import input_switcher as insw


class InvalidDataDimensionException(Exception):
    "Exception raised when euclidean distance is calculated on different dimension length"
    pass


def switch_input(sample_data_list):
    "Switches alphabetical input characters to numeric for calculations"
    numeric_switch = insw.input_switcher()

    for mushroom in sample_data_list:
        for i in range(len(mushroom)):
            mushroom[i] = numeric_switch.switch(mushroom[i])

    return sample_data_list


def euclidean_distance(list1, list2):
    "Calculates the euclidean distance between two data entries"
    if len(list1) != len(list2):
        raise InvalidDataDimensionException

    eucl_dist = 0

    for i in range(len(list1)):
        # Add the square of difference between each list entry
        eucl_dist += math.pow((list1[i] - list2[i]), 2)

    return math.sqrt(eucl_dist)


def determine_status(nearest_neighbors):
    "Counts p/e instances in nearest neighbors and returns most populous"
    "In the case of tie, it will return poisonous"
    e_count = 0
    p_count = 0

    for neighbor in nearest_neighbors:
        if neighbor[0] == 4:
            e_count += 1
        else:
            p_count += 1

    if p_count >= e_count:
        return 'p'
    else:
        return 'e'


def k_nn(sample_data, unknown_data, k):
    status_lists = []
    # For every unknown piece of data
    for unknown in unknown_data:
        max_dist = float('-inf')
        nearest_neighbors = []
        # for every known piece of sample data
        for sample in sample_data:
            temp = copy.deepcopy(sample)
            status = temp.pop(0)
            # calculate the distance between them
            dist = euclidean_distance(unknown, temp)
            # if we do not have a full list of nearest neighbors just add sample
            if len(nearest_neighbors) < k:
                if dist > max_dist:
                    max_dist = dist
                nearest_neighbors.append((status, dist))
            else:
                # if sample is closer than the furthest nearest neighbor
                if dist < max_dist:
                    # replace the max_dist nearest neighbor with the sample
                    for i in range(k):
                        if nearest_neighbors[i][1] == max_dist:
                            nearest_neighbors[i] = (status, dist)
                            break
                    # recompute the nearest neighbor
                    max_dist = float('-inf')
                    for i in range(k):
                        if nearest_neighbors[i][1] > max_dist:
                            max_dist = nearest_neighbors[i][1]

        # Using nearest neighbor, find whether more p/e is more populous and
        # add to result status_lists
        status_lists.append(determine_status(nearest_neighbors))
        print(nearest_neighbors)
    return status_lists


# print("\n\n\n\n")

# actual_results = file_reader.file_read("accuracy_results.txt")
# test_results = file_reader.file_read("predictionResultKNN.txt")

# count = 0
# for i in range(len(actual_results)):
#     if actual_results[i] != test_results[i]:
#         count += 1

# print(count)


print("Reading Known Sample Data...\n")

sample_data_list = file_reader.file_read("MushroomData_8000.txt")
sample_data_list = switch_input(sample_data_list)

print("Reading Unknown Test Data...\n")

unknown_data_list = file_reader.file_read("MushroomData_Unknwon_100.txt")
unknown_data_list = switch_input(unknown_data_list)

# Get k-value input, determines nearest neighbor
while True:
    try:
        k = int(input("What k value would you like to use? [1,100] (Recommended\
[1-10])\n"))
        if k >= 1 and k <= 100:
            break
    except:
        pass
    print("Input must be an integer value in the range of [1, 100]")


print("\nUsing KNN method to determine predicted value...\n")

predicted_statuses = k_nn(sample_data_list, unknown_data_list, k)


print("\nPrinting unknown predictions...\n")

print(predicted_statuses)

print("\nWriting predicted results to file...\n")

output_file = open("predictionResultKNN.txt", "w")
output_file.truncate(0)
for prediction in predicted_statuses:
    output_file.write(str(prediction) + "\n")
output_file.close()

print("End of program")


# ==============================================================================#
