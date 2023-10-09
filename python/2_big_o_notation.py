import random

def main():
    sample_list = random.sample(range(1, 21), 10)
    sample_list.append(19)
    print("sample list:", sample_list)

    # O(1) - Constant Time
    # Ex: accessing an element in a list using its index
    print(sample_list[5])

    # O(n) - Linear time
    # Ex: searching for an element in an unsorted list
    element = 19
    for i, x in enumerate(sample_list):
        if x == element:
            print(f"found {x} on index: {i}")

    # O(n^2) - Quadratic time
    # Ex: Bubble sort
    new_list = sample_list.copy()
    n = len(new_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if new_list[j] > new_list[j+1]:
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
    print("new ordered list:", new_list)


if __name__=='__main__':
    main()