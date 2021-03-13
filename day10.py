def calculateDenseHash(sparse_hash, block_size):
    output = []
    for block in range(16):
        r = sparse_hash[block_size * block]
        for x in sparse_hash[(block_size * block) + 1 : block_size * ( block + 1)]:
            r ^= x
        output.append(r)    
    return output

def convertToAscii(list):
    return [ord(str(c)) for c in list]

def rotate(array, offset):
    return array[offset:] + array[:offset]

def knotHash(list, lengths, iterations=1):
    position = 0
    skip = 0

    for i in range(iterations):
        for length in lengths:
            working_list = rotate(list, position)

            sublist = working_list[:length]
            sublist.reverse()

            working_list = sublist + working_list[length:]
            list = rotate(working_list, -position)

            position = (position + length + skip) % len(list)
            skip += 1
    
    return list

list = list(range(256))
lengths = "165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153"
# lengths = ""

lengths = convertToAscii(lengths) + [17, 31, 73, 47, 23]
sparse_hash = knotHash(list,lengths, 64)

denseHashList = calculateDenseHash(sparse_hash, 16)
denseHash = ''.join([ '{:02x}'.format(c) for c in denseHashList ])

print(denseHash)
