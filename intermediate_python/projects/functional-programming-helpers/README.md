## Create own Higher Order Functions

### Aim 
To further understand functional programming by creating own higher-order functions and using them to process data from a CSV file.

### Project Description
Implement two higher-order functions:

1. **count()**: This function will return the frequency of an element in an iterable.
2. **average()**: This function will commpute the average of elements in an iterable of numbers.

### count() 

The `count()` function is a special type of `filter()` function that returns the number of occurrences of an element instead of a **Boolean** value. It accepts the following parameters:

- **predicate**: A condition that, when evaluated to **True**, allows a counter to increment by one.
- **itr**: The collection containing the element of interest.

### average()

The `average()` function computes the arithmetic mean of a collection. It is immplemented recursively to adhere to functional programming principles and only accepts one parameter:
- **itr**: The collection to be averaged.


---
**Note** the function `reduce()` can accept a third parameter that serves as the initial value, allowing a initial conditionn that is not of the same type as the collection `reduce()` is operating on.

```python
reduce(lambda x, y: x + y, some_collection, initial_value)
```
