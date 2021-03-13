global checked_nodes, pipes

with open('.\day12.txt') as fp:
    input_var = fp.read().strip().splitlines()

def search_pipe_connections(key):
    checked_nodes.add(key)
    for connection in pipes[key]:
        if not (connection in checked_nodes):
            search_pipe_connections(connection)

    pipes.pop(key)
    return

checked_nodes = set()
pipes = {}
groups = 0

# create a hastable where the key is the programid and the values are all the programs that the key communicate with
for connection in input_var:
    program_id, pairs_s = connection.split(' <-> ')
    pairs = pairs_s.split(', ')

    pipes.update({ program_id: pairs })

while( len(pipes) ):
    search_pipe_connections( list(pipes.keys())[0] )
    groups += 1

print(groups)