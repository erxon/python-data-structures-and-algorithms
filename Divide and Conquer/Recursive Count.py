#Recursive Counting of Items in Array
def count(array):
    if len(array) == 1:
        return 1;
    else:
        return 1 + count(array[1:]);

print(count([1, 2, 3]));
