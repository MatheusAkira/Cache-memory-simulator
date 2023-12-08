import sys

def extract_index(address, block_size, cache_size, num_sets):
    index_mask = (cache_size // block_size) 
    if(num_sets//index_mask == 1):
        return True, 0
    return False, (address // block_size) % (index_mask//num_sets)

def format_block_address(address):
    return f"0x{address & 0xFFFFF000:08X}"

def simulate_cache(cache_size, line_size, num_sets, memory_accesses):
    num_lines = cache_size // line_size
    lines_per_set = num_lines // num_sets
    cache = [{'valid': False, 'block_address': 0} for _ in range(num_lines)]
    hits = 0
    misses = 0
    with open('output.txt', 'w') as output_file:
        with open(memory_accesses, 'r') as file:
            accesses = file.readlines()
            for access in accesses:
                access = int(access.strip(), 16)
                set_start = 0
                set_end = num_lines 

                if(not extract_index(access, line_size, cache_size, num_sets)[0]):
                    index = extract_index(access, line_size, cache_size, num_sets)[1]
                    set_start = index * lines_per_set
                    set_end = min(set_start + lines_per_set, num_lines)
                
                block_address = access & ~(line_size - 1)

                found = False
                for i in range(set_start, set_end):
                    if cache[i]['valid'] and cache[i]['block_address'] == block_address:
                        hits += 1
                        found = True
                        break

                if not found:
                    misses += 1
                    for i in range(set_start, set_end):
                        if not cache[i]['valid']:
                            cache[i]['valid'] = True
                            cache[i]['block_address'] = block_address
                            break

                
                output_file.write("================\n")
                output_file.write("IDX V ** ADDR **\n")  # Adiciona o cabeçalho
                for i in range(num_lines):
                    output_file.write(f"{i:03d} {int(cache[i]['valid'])} {format_block_address(cache[i]['block_address'])}\n")

  
        output_file.write(f"\n#hits: {hits}\n")
        output_file.write(f"#miss: {misses}\n")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: python simulador.py <tamanho_cache> <tamanho_linha> <tamanho_grupo> <arquivo_acessos>")
        sys.exit(1)

    cache_size = int(sys.argv[1])
    line_size = int(sys.argv[2])
    num_sets = int(sys.argv[3])
    memory_accesses = sys.argv[4]

    simulate_cache(cache_size, line_size, num_sets, memory_accesses)
