An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array).

Other than some generic containers like list, Python in its definition can also handle containers with specified data types. The array can be handled in python by a module named “array“. They can be useful when we have to manipulate only a specific data type values.

Operations on Array :
1. array(data type, value list):- This function is used to create an array with data type and value list specified in its arguments.
2. append():- This function is used to add the value mentioned in its arguments at the end of the array.
3. insert(i,x) :- This function is used to add the value(x) at the ith position specified in its argument.
4. pop():- This function removes the element at the position mentioned in its argument and returns it.
5. remove():- This function is used to remove the first occurrence of the value mentioned in its arguments.
6. index() :- This function returns the index of the first occurrence of value mentioned in arguments.
7. reverse() :- This function reverses the array.