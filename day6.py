memory = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]
# memory = [0, 2, 7, 0]

def redistribute(memory):
    blocks_to_distribute = highest_no_blocks = max(memory)
    i = index_highest_block = memory.index(highest_no_blocks)
    memory[index_highest_block] = 0

    while( blocks_to_distribute ):
        i += 1
        if ( i >= len(memory) ):
            i = 0
        
        memory[i] += 1
        blocks_to_distribute -= 1
    
    return memory


def solve(memory):

    list_of_memories = {}
    cycles = 0

    while(True):
        hash_value = ''.join([ str(n) for n in memory ])
        if ( hash_value in list_of_memories.keys() ):
            return cycles - list_of_memories[hash_value]
        
        list_of_memories.update({hash_value:cycles})
        memory = redistribute(memory.copy())
        cycles += 1


print(solve(memory))
