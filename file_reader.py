def file_read(requested_file):
    # Opens known mushroom file in read mode
    sample_data_file = open(requested_file, "r")
    # Reads each line into an array element
    sample_data_list = sample_data_file.readlines()

    for index, data in enumerate(sample_data_list):
        data = data.strip("\n")  # Trims new line from each index
        # Splits elements by ',' creating a 2d array
        sample_data_list[index] = data.split(',')

    return sample_data_list
