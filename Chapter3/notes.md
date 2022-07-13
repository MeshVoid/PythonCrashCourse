# **LISTS IN PYTHON**

Lists allow you to store sets of information in one place, whether you
have just a few items or millions of items. 

List - is a colection of items in a particular order. You can put anything
you want into a list from int, strings, float values.

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
```

You can acces individual values from a list like a variable.

```python
print(f"My first bicycle was a {bicycles[0].title()}.")
print(message)
```

Access last item:
```python
bicycles[-1]
```

# **Modifying Elements in a List**

To change an element, use the name of the list followed by the index
of the element you want to change, and then provide the new value
you want that item to have.
```python
motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

#modify element 0 in a list

motorcycles[0] = 'ducati'

print(motorcycles)
```

# **Adding Elements to a List**

Use append() method to add item to the list. 
When you append a new item it will be added to the end of the list.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducatti')
print(motorcycles)
```

# **Inserting elements into a list**

Use _insert()_ method
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
```

# **Removing elements from a list**

Remove elements from a list using a del statement:
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
```
If you use del statement to remove elements of the list,
you won't be able to access the deleted value.

You can also use **_pop()_** method to delete items in a list
```python
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
```

You can use pop() to remove any item by including 
the index number othe item you want to remove:

```python
motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was {first_owned.title()}.")
```

! Remember that each time you use pop(), the item you work with is no
longer stored in the list.

# **pop() method or del statement?**

If you’re unsure whether to use the del statement or the pop() method, 
here’s a simple way to decide: when you want to delete an item from a 
list and not use that item in any way, use the del statement; 
if you want to use an item as you remove it, use the pop() method

# **Removing an Item by value**

If you only know the value of the item you want to remove, you can use
the _**remove()**_ method.
```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)
```
_Remember that the remove() method deletes ony the first occurrence of the
value you specify. If there's a possibility the value appears more than
once in the list, you'll need to use a loop to make sure all occurrences
of the value are removed._



# **ORGANIZING LISTS**

Python’s sort() method makes it relatively easy to sort a list.
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
```
the sort() method changes the order of the list permanently.

You can also sort the list in reverse, using argument reverse=True to the sort() method.
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
```


# **Sorting a List Temporarily with the sorted() Function**


To maintain the original order of a list but present it in a sorter order, you can use
sorted() function. The sorted() function lets you display your list in a particular order
but desn't affect the actural order of the list

```python
cars = ['bmw','audi','toyota','subaru']
print("\n Here is the original list:")

print(cars)
print("\nHere is the sorted list:")

print(sorted(cars))
print("\nHere is the original list again:")

print(cars)
```


# **Printing a list in reverse order**

To reverse the original order of a list, you can use the reverse() method. If we originally stored the list of cars in chronological order according to when we owned them, we could easily rearrange the list into reverse chronological order:

```python
print("\n")
print(cars)
cars.reverse()
print(cars) 
```

 Notice that reverse() doesn't sort backward alphabetically; it just reverses the order of the list!
 reverse() changes the list permanently, but you cal revert to the original order anytime by applying reverse() to the same list a second time.

 # **Finding the Length of a List**

 You can quickly find the length of a list by using the **_len()_** function. The list in this example has four items, so its length is 4:

 