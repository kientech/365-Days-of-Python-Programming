# Coding With Kien - 365 Days of Python Programming
# Intermediate - Day 01

# Find the most frequent element in a list

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
 
    return num
 
List = [2, 1, 2, 2, 1, 3]
print(f"The most frequent element is: {most_frequent(List)}")

# Input: [2, 1, 2, 2, 1, 3]
# Output: The most frequent element is: 2 