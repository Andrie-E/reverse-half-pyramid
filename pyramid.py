# Print a downward Half-Pyramid Pattern of Star (asterisk)

# Pseudocode
# indicate number of row
rows = 5
# Outer loop: Iterate from 6 to 1 in reverse order
for i in range(rows, 0, -1):
# Inner loop: Iterate 
    for j in range(0, i):
# Print '*' 
        print("*", end=' ')
# Move to the next line after inner loop
    print(" ")
