class mushroom:
    def __init__(self, classes, cap_shape, cap_color, bruises, odor, gill_attachment, gill_spacing,
                 gill_size, gill_color, stalk_shape, stalk_root, stalk_surface_above_ring,
                 stalk_surface_below_ring, stalk_color_above_ring, stalk_color_below_ring,
                 veil_type, veil_color, ring_number, ring_type, spore_print_color, population, habitat):
        self.classes = classes
        self.cap_shape = cap_shape
        self.cap_color = cap_color
        self.bruises = bruises
        self.odor = odor
        self.gill_attachment = gill_attachment
        self.gill_spacing = gill_spacing
        self.gill_size = gill_size
        self.gill_color = gill_color
        self.stalk_shape = stalk_shape
        self.stalk_root = stalk_root
        self.stalk_surface_above_ring = stalk_surface_above_ring
        self.stalk_surface_below_ring = stalk_surface_below_ring
        self.stalk_color_above_ring = stalk_color_above_ring
        self.stalk_color_below_ring = stalk_color_below_ring
        self.veil_type = veil_type
        self.veil_color = veil_color
        self.ring_number = ring_number
        self.ring_type = ring_type
        self.spore_print_color = spore_print_color
        self.population = population
        self.habitat = habitat

    def __str__(self):
        return f"{self.classes}, {self.cap_shape}, {self.cap_color}, \
{self.bruises}, {self.odor}, {self.gill_attachment}, {self.gill_spacing}, \
{self.gill_size}, {self.gill_color}, {self.stalk_shape}, {self.stalk_root}, \
{self.stalk_surface_above_ring}, {self.stalk_color_below_ring}, \
{self.veil_type}, {self.veil_color}, {self.ring_number}, {self.ring_type}, \
{self.spore_print_color}, {self.population}, {self.habitat}"


def mushroom_list_create(char_list):
    # Creates a list of mushroom objects from a list of characters representing a mushrooms characteristics
    mushroom_list = []
    for element in char_list:
        mushroom_list.append(
            mushroom(element[0], element[1], element[2], element[3], element[4], element[5], element[6],
                     element[7],
                     element[8], element[9], element[10], element[11], element[12], element[13],
                     element[14],
                     element[15], element[16], element[17], element[18], element[19], element[20],
                     element[21]))

    return mushroom_list
