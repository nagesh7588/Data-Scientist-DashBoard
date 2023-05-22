#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_place_value(number, digit):
    number_str = str(number)
    digit_str = str(digit)
    
    if digit_str not in number_str:
        return -1  # Digit not found in the number
    
    place_value = len(number_str) - number_str.index(digit_str)
    return place_value

# Example usage
number = 248760
digit = 4
place_value = find_place_value(number, digit)
print(f"The place value of {digit} in {number} is {place_value}.")


# In[2]:


def find_place_value(number, digit):
    number_str = str(number)
    digit_str = str(digit)
    
    if digit_str not in number_str:
        return -1  # Digit not found in the number
    
    place_value = len(number_str) - number_str.index(digit_str)
    return place_value

# Example usage
number = 248760
digit = 4
place_value = find_place_value(number, digit)
print(f"The place value of {digit} in {number} is {place_value}.")


# In[3]:


num1 = 579798797
num2 = 6996796876

result = num1 + num2

print("The sum of", num1, "and", num2, "is:", result)


# In[1]:


num1 = 579798797
num2 = 6996796876

result = num1 + num2

print("The sum of", num1, "and", num2, "is:", result
     )


# In[2]:


x = [11,22,33,44,55]
for i in x:
    print(i)


# # empty

# In[3]:


x = [11,22,33,44,55]
for i in range(len(x)):
    print(i)


# In[ ]:


x = [11,22,33,44,55]
for i in range(len(x)):
    print(i,"---",x[i])


# # List      ------------------    [  ]

# In[4]:


# wap to create a list with the help of user input
num = int(input("enter your range = "))
new_list = []
for i in range(num):
    y = input("enter your elements = ")
    if y.isdigit():
        new_list.append(int(y))
    else:
        new_list.append(y)
print(new_list)


# In[ ]:





# In[8]:


# q1. wap to multiple each element together
x = [1,2,3,4,5]
x = [1, 2, 3, 4, 5]
result = 1

for num in x:
    result *= num

print("The result is:", result)


# In[9]:


x = [1, 2, 3, 4, 5]
result = 1

for num in x:
    result *= num

print("The result is:", result)


# In[10]:


x = [1, 2, 3, 4, 5]
sum_of_elements = sum(x)
print("Sum of elements:", sum_of_elements)


# In[11]:


#Q1
x = ["hello","hi"]
y = ["sonu","monu"]
# output:-
# z = ["hello sonu", "hello monu", "hi sonu", "hi monu"]
z = []
for i in x:
    for j in y:
        z.append(i+" "+j)
print(z)


# In[1]:


# wap to remove all 33
# Q1
x = [11,22,33,44,33,33,33]
# Q2
# x = ['m', 'na', 'i', 'am']
# x = ['y', 'me', 's', 'an']



# In[2]:


# Q1
x = [11, 22, 33, 44, 33, 33, 33]

# Remove all occurrences of 33
x = [num for num in x if num != 33]

print(x)


# # tuple  ------------  ( )

# # list and tuple are same, except List element can be changed and its bracket are square brackets whereas Tuple elements can't be changed and its bracket is round.

# In[2]:


x = (1,2,3,4,5)
print(min(x))
print(max(x))
print(sum(x))


# In[3]:


x = (1,2,3)
y = (4,5,6)
z = x+y
print(z)


# # Tuple, it's must to have 2 elements in a tuple

# # data structure = set

# # Set is a collection of unique elements and it is unordered. It is unindexed. Set is immutable.

# # set has curly bracket---------{}

# In[5]:


x = {1,"hello", "hi", 2.4, '5', 11, 41, 5, 'het'}


# In[6]:


print(x)


# In[ ]:





# In[7]:


x = {1,22,3,11,4}
# print(x)
x.add(6.7)
print(x)


# In[10]:


x={1,2,3,4}
y={1,5,6,4}
x.difference(y)

# x  is the main and y is secondary


# In[11]:


x={1,2,3,4}
y={1,5,6,4}
z=x.intersection(y)
print(z)


# In[13]:


x={11,21,23,41}
# x.remove(21)
x.discard(22)
x.pop()
# pop removes any element
print(x)


# In[14]:


x={1,2,3,5}
x.isdisjoint


# # SET where do we use set

# In[16]:


x = [1,1,1,1,14,1,1,1,1,2,2,2,2,2,]
y = set(x)
x = list(y)
print(x)


# # SET is over

# # Dictionary 
# - dict is a collection of key value pair
# - dict is ordered
# - dict is unindexed
# - dict is mutable

# In[18]:


x = {
    
    # a is a key
    'a' : 1,
    'b' : 2,
    'c' : 3,
    7   : 45,
    5.6 : 67
    
}
print(x)
print(x[7])


# In[20]:


x = {
    
    # a is a key
    'a' : 1,
    'b' : 2,
    'c' : 3,
    7   : 45,
    5.6 : 67
    
}
# print(x)
# print(x[7])
print(x.get('d', 'no result'))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




