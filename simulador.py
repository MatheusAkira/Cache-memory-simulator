import in_out as io
import sys
import cache as simulator

if __name__ == "__main__":

    cache_size, size_line, size_groups, \
    name_file, hex_values, binary_values, \
    adjusted_binary_values, adjusted_hex_values = io.input(sys.argv[1:])

    simulator = simulator.CacheSimulator(cache_size, size_line, size_groups)

   
    # Mapear os dados para a cache
    simulator.map_to_set(binary_values)


    