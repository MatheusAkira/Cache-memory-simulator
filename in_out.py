import numpy as np
import math 


# Function to convert hexadecimal to binary and adjust 
# the 10 least significant bits"
def hex_to_bin_and_adjust(hex_value, size_line):
    binary_value = bin(int(hex_value, 16))[2:]
    exp = int(math.log2(int(size_line)))
    binary_with_adjustment = binary_value[:-exp] + '0' * exp
    hex_with_adjustment = '0x' + hex(int(binary_with_adjustment, 2))[2:].upper().zfill(8)
    return binary_value, binary_with_adjustment, hex_with_adjustment

def input(arg):
    # store arguments
    cache_size = arg[0]
    size_line = arg[1]
    size_group = arg[2]
    name_file = arg[3]

    hex_values = []
    binary_values = []
    adjusted_binary_values = []
    adjusted_hex_values = []

    with open(name_file, 'r') as file:
        for line in file:
            hex_value = line.strip()
            hex_values.append(hex_value)
            binary, adjusted_binary, adjusted_hex = hex_to_bin_and_adjust(hex_value, size_line)
            binary_values.append(binary)
            adjusted_binary_values.append(adjusted_binary)
            adjusted_hex_values.append(adjusted_hex)
    
    return (
            cache_size, size_line, size_group, name_file, 
            hex_values, binary_values, adjusted_binary_values, 
            adjusted_hex_values
    )