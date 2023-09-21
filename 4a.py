import random
def merge_sort(rec):
    if len(rec) > 1:
        mid = len(rec) // 2
        left_half = rec[:mid]
        right_half = rec[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                rec[k] = left_half[i]
                i += 1
            else:
                rec[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            rec[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            rec[k] = right_half[j]
            j += 1
            k += 1
            return rec

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

n=int(input('enter the number of elements: ' ))
my_list = []
for i in range(n):
    my_list.append(random.randint(0, 999))

print("\nUnsorted List")
print(my_list)
print("Sorting using Insertion Sort")
insertion_sort(my_list)
print(my_list)

my_list = []
for i in range(n):
    my_list.append(random.randint(0, 999))
print("\nUnsorted List")
print(my_list)
print("Sorting using Merge Sort")
merge_sort(my_list)
print(my_list)