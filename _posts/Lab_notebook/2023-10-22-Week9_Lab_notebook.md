
## What I learned this week

> ### Developing Algorithms

- a set of instructions for solving a specific problem or performing a particular task.
- Automate and simplify repetitive code
- More efficient functions
- if, elsif, else 
> > #### Using algorithms to organize lists

- SELECTION SORT: Splits list into sorted & unsorted, takes the greatest or smallest value and puts it into sorted section, repeat
- INSERTION SORT: Splits list into sorted & unsorted, takes any value from list, inserts into correct position on sorted section, repeat
> ### 3.10-3.11 Lists and Searches

> > #### Basic Operations
- Defining the List
    aList= [1,4,2,6,7,3,]
- Accessing Elements in a list
    print(aList[1])


- Storing Element at an Index to a variable
    Element = aList[3]
    print(Element)


- Setting an Element at an Index to a variable
    element = 4
    aList[5]= element
    print(aList[5])

- Insert a value at a certain index
    aList.insert(3, 10)
    print(aList[3])

- Adding another value to the list (append)
    aList.append(5)
    print(aList)

- Removing a value from the List at a specific Index
    aList.remove(2)
    print(aList)

- Accessing the Length of a list
    print(len(aList))

> > #### Performing a Binary Search
- index: organizing the data by assigning a reference value to each element
- Put the number is order either ascending or descending
- Search starts with middle number first which is found by adding the highest and lowest index number and dividing it by 2
- This divides the range by 2
- Repeat this process by shrinking the range each time till the desired target is found
- Every time the process is repeated and leads to a target it is considered a comparison

> > #### Performing a Sequential Search
- Each element in a list is examined in the order of the first element till the desired target
- Order doesn’t matter