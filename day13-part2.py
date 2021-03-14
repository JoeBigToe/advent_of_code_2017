with open('.\day13.txt') as fp:
    input_var = fp.read().strip().splitlines()

# create the firewall
firewall = []
for layer in input_var:
    depth, r = layer.split(": ")
    firewall.append([int(depth), int(r)])

d = 1
while(True):
    
    if not (any( e ==0 for e in [(a[0] + d) % (2*(a[1]-1)) for a in firewall])):
        print(d)
        break

    d +=1
