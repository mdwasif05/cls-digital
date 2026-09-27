#rows = 5
#for i in range (0, rows):
    #for j in range (0, i + 1):
        #print("*" , end = " ")
    #print("\n")
#rows = 5
#for i in range(rows+1, 0, -1):
    #for j in range(0, i - 1):
        #print("*", end=' ')
    #print("\n")
#rows = 5
#for j in range(1, rows + 1):
    #print(" " * (2 * (rows - j)) + "* " * j)
rows = 5
for j in range(1, rows + 1):
    print(" " * (rows - j) + "* " * j)