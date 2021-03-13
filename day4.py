
def solve():

    valid_passes = 0
    with open('.\day4.txt') as fp:
        for line in fp.read().strip().splitlines():
            list_of_words = set()
            add = 1
            for word in line.split():
                modified_word = ''.join(sorted(word))
                if modified_word in list_of_words:
                    add = 0
                    break
                else:
                    list_of_words.add(modified_word)
            
            valid_passes += add

    return valid_passes

print(solve())
