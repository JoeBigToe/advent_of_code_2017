def solve():
    with open('.\day7.txt') as fp:
        input_var = fp.read().strip().splitlines()

        tree = {}
        parented_nodes = set()

        for line in input_var:
            splitted_line = line.split(' -> ')
            node = splitted_line[0]
            child_nodes = None if len(splitted_line) == 1 else splitted_line[1].split(', ')
            
            node_name, weight = node.split()
            weight = weight.strip('()')

            tree.update(
                {
                    node_name: [
                        int(weight),
                        child_nodes
                    ]
                }
            )

            if child_nodes:
                for node in child_nodes:
                    parented_nodes.add(node)

    # for key in tree.keys():
    #     if not(key in parented_nodes):
    #         print(key)
    
    return tree

def is_tower_unbalanced(tower):

    summed_tower = [ sum(i) for i in tower ]

    group = {}
    for i in range(len(summed_tower)):
        item = summed_tower[i]
        if item in group.keys():
            group[item] += 1
        else:
            group.update({item : 1})
    
    if len(group.keys()) == 1:
        return 0
    
    foreign_sum = 0
    foreign_element = 0
    common_sum = 0
    common_element = 0

    # print(tower)
    for key in group.keys():
        if group[key] == 1:
            foreign_sum = key
            foreign_element = tower[summed_tower.index(key)][0]
        else:
            common_sum = key
            common_element = tower[summed_tower.index(key)][0]
    
    # return 1
    # print(tower, " -> ", summed_tower)
    return foreign_element - (foreign_sum - common_sum)

def sum_subtree(tree, node):
    if not (tree[node][1]):
        return tree[node][0]

    for child in tree[node][1]:
        sum_subtree(tree, child)

    tower_weight = [
        [
            tree[child][0], 
            sum(sum_subtree(tree, grandchild) for grandchild in tree[child][1]) if tree[child][1] else 0
        ] for child in tree[node][1]
    ]

    unbalance = is_tower_unbalanced(tower_weight)
    if unbalance:
        print("Found unbalance", unbalance)
        # return sum(sum(tower_element) for tower_element in tower_weight)

    return tree[node][0]+sum(sum(tower_element) for tower_element in tower_weight)

tree = solve()
# print(solve())
sum_subtree(tree, 'hmvwl')
# sum_subtree(tree, 'tknk')



