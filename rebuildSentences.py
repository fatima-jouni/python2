# the concept of this program is to create a function that reconstructs a sentence by joining words in the list
#according to the word lengths provided
#rebuild_sentence( [ "the", "sky", "is", "blue" ] , [ 3, 2, 2, 1 ] ) # Output: "the sk is b"
#Slicing lets you access a range of characters by specifying a start and end index

list_of_words = ["the", "sky", "is", "blue"]

length = [3, 2, 2, 1 ]

def rebuild_sentence(list_of_words :list, lengths : int):
  
#creating a function that takes list of words and list of length  

  for i in range (len(lengths)):

   #creating a for loop to move along each word 

    print(list_of_words[i][0:lengths[i]] , end =' ')

    # i used the slice method to access any specific index for each word
    # word[start char : end char]
    # the word is accessed using the list of words and the leangth of 
    # each word is specified by the list of lengths 

rebuild_sentence(list_of_words, length) 