with open('.\day13.txt') as fp:
    input_var = fp.read().strip().splitlines()

# create the firewall
firewall = {} 
for layer in input_var:
    depth, range = layer.split(": ")
    firewall.update( { depth: [int(range), 1, 0] } )

layer = 0
severity = 0

while( layer <= max([int(a) for a in firewall.keys()]) ):

    layer = str(layer)
    
    # Check if packet was caught
    if layer in firewall.keys():
        if ( firewall[layer][2] == 0 ):
            severity += int(layer) * firewall[layer][0]
    
    # move the security scanner
    for firewall_layer in firewall.keys():
        firewall[firewall_layer][2] += firewall[firewall_layer][1]
        if ( firewall[firewall_layer][2] in [ 0, (firewall[firewall_layer][0] - 1) ] ):
            firewall[firewall_layer][1] *= -1
    
    layer = int(layer)
    layer += 1 

print(severity)