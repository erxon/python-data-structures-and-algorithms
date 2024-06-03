#Recursive Find the Max Num
def find_max(array):
    max_num = 0
    if len(array) == 1:
        max_num = array[0]
        return max_num
    if array[0] > find_max(array[1:]):
        max_num = array[0]
        return max_num
            

print(max([70, 120, 90]))
