# number of items produced and items per box fille
import math
n = int(input("Enter the number of items? "))
N = int(input("Enter the number of items per box? "))
number_of_boxes = math.ceil(n/N)
print (f"For {n} items, packing {N} items in each box, you will need {number_of_boxes} boxes.")

