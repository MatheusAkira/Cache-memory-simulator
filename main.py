import in_out as io
import sys

if __name__ == "__main__":

    cache_size, size_line, size_group, \
    name_file, hex_values, binary_values, \
    adjusted_binary_values, adjusted_hex_values = io.input(sys.argv[1:])

    print("cache_size :", cache_size)
    print("size_line :", size_line)
    print("size_group: ", size_group)
    print("name_file :", name_file)
    print("hex_values :", hex_values)
    print("binary_values :", binary_values)
    print("adjusted_binary_values :", adjusted_binary_values)
    print("adjusted_hex_values  :", adjusted_hex_values)