import math
from collections import deque
import numpy as np


#1 linha por grupo: MD 4 grupos e 4 linhas
#4 linhas por grupo: TA 1 grupo com 4 linhas

class CacheSimulator:
    def __init__(self, cache_size, size_line, size_groups):
        self.cache_size = int(cache_size)
        self.size_lines = int(size_line)
        self.size_groups = int(size_groups)
        self.n_lines = int(self.cache_size / self.size_lines)
        self.line_per_group =  int(self.n_lines / self.size_groups) 
        self.cache = [deque(maxlen=self.line_per_group) for _ in range(self.size_groups)]
        #for i, conjunto in enumerate(self.cache):
        #    print(f"00{i}: {conjunto}")
        self.hits = 0
        self.miss = 0
        self.counter_cache = 0
        self.V = [0] * self.n_lines
        self.aux = [0] * self.size_groups   
    
    def acessar_dado(self, idx, dado):
            if dado in self.cache[idx]:
                self.hits +=1
            else:

                self.miss +=1
                
                if len(self.cache[idx]) < self.line_per_group:
                    #print("ender", (idx * self.line_per_group) + (len(self.cache[idx]))  )
                    self.V[(idx * self.line_per_group) + (len(self.cache[idx])) ] = 1
                    self.cache[idx].append(dado)
                    
                else:
                    new_pos = (len(self.cache[idx]) + self.aux[idx]) % self.line_per_group
                    self.cache[idx][new_pos] = dado
                    self.aux[idx] +=1
                    
    #printar cachê
    def print_cache(self, file_path="output.txt"):
        with open(file_path, "a") as file:
            print("================", file=file)
            print("IDX V ** ADDR **", file=file)
            idx_print =  0

            #Verificar se os índices estão dentro dos limites
            for linha in range (self.size_groups):
                for coluna in range(self.line_per_group):
                    if 0 <= linha < len(self.cache) and 0 <= coluna < len(self.cache[linha]):
                        print(f"00{idx_print} {self.V[coluna]} {self.cache[linha][coluna]}", file=file)
                        idx_print += 1
                    else:
                        print(f"00{idx_print} {self.V[coluna]}", file=file) 
                        idx_print += 1

    #Formatar hexa
    def format_hex(self, value_hex):
        hex_size_defaut = 10
        if value_hex.startswith('0x') or value_hex.startswith('0X'):
            value_hex = value_hex[2:]
        value_hex_format = f'0x{value_hex.zfill(hex_size_defaut-2).upper()}'
        return value_hex_format
        
    #Mapear dados
    def map_to_set(self, binary_values, address_space = 32):
        exp_way = int(math.log2(self.size_groups))

        #Mapear n-way e mapeamento direto
        if(exp_way != 0):
            
            for binary_value in binary_values:
                complement = address_space - len(binary_value)
                binary_full = complement * '0' + binary_value
                
                offset = int(math.log2(int(self.size_lines)))
                binary_without_offset = binary_full[:-offset]
               
                idx_block = int(binary_without_offset[-exp_way:], 2)
                hexa_value = hex(int(binary_without_offset, 2)).upper()

                hexa_value = self.format_hex(hexa_value)
                self.acessar_dado((idx_block ), hexa_value)
                self.print_cache()
             
        #Mapeamento totalmente associativo
        else:
            for binary_value in binary_values:
                complement = address_space - len(binary_value)
                binary_full = complement * '0' + binary_value
                    
                offset = int(math.log2(int(self.size_lines)))
                binary_without_offset = binary_full[:-offset]
                idx_block = 0
                hexa_value = hex(int(binary_without_offset, 2)).upper()
                hexa_value = self.format_hex(hexa_value)
                
                self.acessar_dado(idx_block, hexa_value)
                self.print_cache()

        file_path="output.txt"         
        with open(file_path, "a") as file:
            print('\n', file=file)
            print("#hits: ", self.hits,file=file )
            print("#miss: ", self.miss ,file=file)