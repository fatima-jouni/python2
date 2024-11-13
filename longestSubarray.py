
arr = [0,1,1,1,0,0,1]

def longest_subarray(array):
    max_length = 0
    best_subarray = []

    # Check all subarrays
    for i in range(len(array)):
        zeros = 0
        ones = 0
        for j in range(i, len(array)):
            # Count zeros and ones in the current subarray
            if array[j] == 0:
                zeros += 1
            else:
                ones += 1
            
            # Check if the current subarray has equal 0s and 1s
            if zeros == ones:
                current_length = j - i + 1
                # Update max_length and best_subarray when a longer subarray is found
                if current_length > max_length:
                    max_length = current_length
                    best_subarray = array[i:j+1]  # Store the current subarray

    print("Longest subarray:", best_subarray)
    return max_length

longest_subarray(arr)
















"""
counter0 = 0
counter1 = 0
max = 0


for i in range(len(arr)-1):

    if arr[i] == 0:
        counter0 += 1
    else:
        counter1 += 1

    if counter0 == counter1:
        print(arr[0:i])
        max = i+1
"""