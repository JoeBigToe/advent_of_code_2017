import re

with open('.\day9.txt') as fp:
        stream = fp.read().strip()

# Remove escape chars
while(True):
    new_stream = re.sub('!.', '', stream, count=1)
    if new_stream == stream:
        break

    stream = new_stream

# remove garbage

# Part 2: Calculate the amount of garbage
garbage = re.findall('<(.*?)>', stream)
print(sum([ len(garbage_content) for garbage_content in garbage ]))

stream = re.sub('<.*?>', '', stream)


# count subgroups
def countSubGroups(stream_collection, level):
    # subgroups = re.findall('{.*}', stream)

    sum = 0
    balance = 0
    group_min = 0
    group_max = 0
    
    re.sub('^}+', '', stream_collection)
    re.sub('{+$', '', stream_collection)

    if len(stream_collection) == 2:
        return level
    
    for i in range(len(stream_collection)):
        balance += 1 if stream_collection[i] == '{' else -1
        group_max += 1
        if balance == 0:
            sum += level + countSubGroups(stream_collection[group_min+1:group_max-1], level + 1)
            break
    
    if group_max < len(stream_collection):
        sum +=  countSubGroups(stream_collection[group_max:], level)


    # for subgroup in subgroups:
    #     sum += countSubGroups(subgroup[1:-1], level + 1)

    return sum

stream_collection = ''.join(re.findall('[{}]', stream))
# print(countSubGroups(stream_collection, 1))

