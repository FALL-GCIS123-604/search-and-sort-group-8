import random
import time


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Splitting the array into odd and even indexed parts
    odd_indexes = arr[1::2]
    even_indexes = arr[::2]

    # Recursively sort both halves
    odd_sorted = merge_sort(odd_indexes)
    even_sorted = merge_sort(even_indexes)

    # Merging sorted odd and even parts
    i = j = k = 0
    while i < len(even_sorted) and j < len(odd_sorted):
        if even_sorted[i] < odd_sorted[j]:
            arr[k] = even_sorted[i]
            i += 1
        else:
            arr[k] = odd_sorted[j]
            j += 1
        k += 1

    # Checking if any element was left in either half
    while i < len(even_sorted):
        arr[k] = even_sorted[i]
        i += 1
        k += 1

    while j < len(odd_sorted):
        arr[k] = odd_sorted[j]
        j += 1
        k += 1

    return arr
        
        
# Phase 1
def generate_sorted_data(size):
    list = [] # Create list
    for i in range(size):
        new_number = random.randint(1,100) # Adds a random number into the variable new number
        if new_number not in list: # IF new number isnt in the list puts it into the list using append
            list.append(new_number)
    #print(list)
    
    
    
    #Phase 3
    if size < 100: # Here we use if size less than 100 so that if the size is more than that we can use merge sort because insertion sort would be too slow
        
        for i in range(1,len(list)): # This is insertion sort code:
            current=list[i] # Starts by taking a number from the list from i
            j=i-1 # takes the number left of the chosen number
            while list[j]>current and j>=0: # while the number left of the current is more than it, and the index of the number on the left is 0 or more
                list[j+1]=list[j] # move the number on the left to the right
                j-=1 #changes the index accordingly
            list[j+1]=current # moves the number from the left to the right
        print(list)
        return list
    
    else:
    
        merge_sort(list)
        print(list)
        return list


#Phase 2

def binary_search(list,target): #This function makes the user take the list generated and requires a target number to be searched for inputted
    
    found = False #indicates that the item searched for is currently not found by default
    lowerBound = 0
    upperBound = len(list) - 1

    item = target
    while found == False and lowerBound <= upperBound: #checks to see if the item being searched for hasn't already been found. The loop will continue to run as long as this is false. As long as the lowerbound is less than the upperbound means that the number is still yet to be searched for, if it was greater than the loop will stop
        midpoint = (upperBound + lowerBound)//2 #rounds mid point down to whole number

        if list[midpoint] == item:
            found = True #returns true only if the index value is equal to the item entered for search

        elif list[midpoint] < item:
            lowerBound = midpoint + 1 #sets a new lowerbound to the index after the midpoint if the item being searched for is greater than the midpoint value
        else:
            upperBound = midpoint - 1 #sets a new upperbound to the index after the midpoint if the item being searched for is less than the midpoint value
    if found == True:
        print("Item found at index",midpoint) #prints the midpoint with an appropriate message if the value is found
    else:
        print("Item not found") #prints the midpoint with an appropriate message if the value is not found


#Phase 4

def timed_search(arr,target):
    #LINEAR SEARCH
    
    linear_t1 = time.perf_counter()
    if target not in arr:               #considers target not being in the array
        print("target not found")
    else:
        for i in range(len(arr)):
            if arr[i]==target:
                print(f"Target found at index {i}.")
                linear_t2 = time.perf_counter()
                print(f"Time taken for Linear search: {linear_t2-linear_t1}")       #checking time taken for linear search
                
        
                
        #BINARY SEARCH
        
        binary_t1 = time.perf_counter()
        binary_search(arr,target)
        binary_t2 = time.perf_counter()
        
        print(f"Time taken for Binary search: {binary_t2-binary_t1}.")      #checking time taken for binary search.
                
    
'''
Answer to the question:
The choice of sorting algorithms greatly impact the performance of searching algorithms, 
for example, using binary search instead of linear search on a sorted list is a very fast way 
to search for an item, while using merge sort would be the fastest way as it does not require a 
sorted list and is efficient with a time complexity of (O(n log n)). Binary search is much faster 
than linear search in large sorted data because when you use linear search you would have to go 
through say for example the list is 1000 elements, linear search would compare each and every element 
in that list. Binary search on the other hand could find the number  you are looking for by eliminating 
half the list on the first go by finding out if your number is greater or less than certain numbers within 
the list, making it so that instead of going through 1000 elements maybe you could only go through 3 or 4. 
With efficient sorting methods like merge sort it can greatly minimize the time needed to organize data, 
hence making use of binary search would be much more efficient and with less time because we greatly 
reduced the amount of time needed to sort a list.

'''



master_array = generate_sorted_data(120)        
timed_search(master_array,55)







        
        
