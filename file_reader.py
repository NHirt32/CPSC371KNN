def file_read(requested_file):
    sample_data_file = open(requested_file, "r") # Opens known mushroom file in read mode
    sample_data_list = sample_data_file.readlines() # Reads each line into an array element

    for index, data in enumerate(sample_data_list):
        data = data.strip("\n") # Trims new line from each index
        sample_data_list[index] = data.split(',')   # Splits elements by ',' creating a 2d array

    return sample_data_list