distances = [
    [0, 143, 108, 118, 121, 88, 121, 57, 92],    # home
    [143, 0, 35, 63, 108, 228, 182, 73, 162],    # A
    [108, 35, 0, 45, 86, 193, 165, 42, 129],     # B
    [118, 63, 45, 0, 46, 190, 203, 73, 105],     # C
    [121, 108, 86, 46, 0, 172, 224, 98, 71],     # D
    [88, 228, 193, 190, 172, 0, 174, 160, 108],  # E
    [121, 182, 165, 203, 224, 174, 0, 129, 212], # F
    [57, 73, 42, 73, 98, 160, 129, 0, 117],      # G
    [92, 162, 129, 105, 71, 108, 212, 117, 0]]    # H

home = 0
A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
G = 7
H = 8

print distances[A][B]
print distances[A][C]
print distances[B][C]

# A -> B = 35
# A -> C = 63
# B -> C = 45

# C -> A
# C -> B



