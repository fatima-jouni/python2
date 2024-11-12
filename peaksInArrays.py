#the concept of this program is to find the preak in the array
#the right and left side has their peak in between 
#like index 0 and 2 have the peak 1 ,we need to see the peaks that are greater
#than their neighbors . thus we're going to compare the peak with the previous index
#and the next index 

arr = [7,8,6,0,8,9,2,1,3]

def find_peaks(arr : list):
  list_of_indices = []
  for i in range(1, len(arr) - 1):
        # Check if arr[i] is a peak
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            list_of_indices.append(i)
            
    
  print("Indices of peaks:", list_of_indices)
  return list_of_indices

  

find_peaks(arr)
