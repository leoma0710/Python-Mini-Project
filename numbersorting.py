# Input the listnumber (original list).
listnumber = [10,0.123,123,-20,0,-8,1000,25]

# Print and check if there is any wrong.
print(listnumber)

# Initial the length to zero.
length1 = 0

# Calculate the length of the input list.
for i in listnumber:
    length1 += 1

# Create a function called sorting.
def sorting(listnumbersort):
    # Transver through all elements.
    for i in range(length1):
        # Number of times needed to transver.
        for j in range(0,length1-1-i):
            # Swap the variable if the next one is greater.
            if listnumbersort[j]>listnumbersort[j+1]:
                # blank is a temporary space to store the old variable.
                blank = listnumbersort[j]
                # Transfer the next value to the old one.
                listnumbersort[j] = listnumbersort[j+1]
                # Transfer the old value to the next space.
                listnumbersort[j+1] = blank
                # Finish the action of swapping.

# Initial listnumbersort to a blank list.
listnumbersort = []
# The length of listnumbersort (must be zero).
length2 = 0

# Extend the length of listnumbersort same as the input list.
for length2 in range(length1):
    listnumbersort.append(0)

# Copy the whole original list to listnumbersort.
for i in range(length1):
    listnumbersort[i] = listnumber[i]

# Run the function "Sorting" to sort the list ascendingly.
sorting(listnumbersort)

# Show the original input.
print('Input List: ', listnumber)

# Show the final output.
print('Output List: ', listnumbersort)
