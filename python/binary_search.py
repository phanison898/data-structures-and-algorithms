class BinarySearchAlgorithm:

    def binary_search(self, list, target):
        start = 0
        end = len(list) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            if list[mid] == target:
                return mid
            elif target > list[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return -1


if __name__ == "__main__":

    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    target = 10

    binarySearchAlgorithm = BinarySearchAlgorithm()
    output = binarySearchAlgorithm.binary_search(list, target)

    if output >= 0:
        print(f" Element {target} found at index of {output} int the list {list}")
    else:
        print(f" Element {target} not found in the list {list}")
