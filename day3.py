import math

element = 265149

bottom_rigth_corner = element
while (True):
    if ( math.sqrt(bottom_rigth_corner).is_integer() ):
        break
    bottom_rigth_corner += 1

print("bottom right corner: ", bottom_rigth_corner)

ring = (math.sqrt(bottom_rigth_corner) -1 ) / 2

maximum_distance_to_core = ring * 2
print("Maximum distance to core: ", maximum_distance_to_core)

# Create hashtable with this ring numbers and their distance to the core
bottom_rigth_corner_previous_ring = (math.sqrt(bottom_rigth_corner)-2)**2
edge_size_half = (bottom_rigth_corner - bottom_rigth_corner_previous_ring) / 8
middle_points = [ bottom_rigth_corner_previous_ring + i*edge_size_half for i in range(8) ]

ring_element = middle_points[0]
incrementor = -1
distance = maximum_distance_to_core
while(True):
    if ( ring_element == element ):
        print(distance)
        break

    ring_element += 1
    distance += incrementor

    if (ring_element in middle_points):
        incrementor *= -1









