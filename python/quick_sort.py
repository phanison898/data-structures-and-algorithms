class QuickSort:

    def sort(self, array):
        if len(array) <= 1:
            return array
        else:
            pivot = array[len(array) // 2]
            left = [x for x in array if x < pivot]
            middle = [x for x in array if x == pivot]
            right = [x for x in array if x > pivot]
            return self.sort(left) + middle + self.sort(right)


if __name__ == "__main__":
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    quick_sort = QuickSort()
    output = quick_sort.sort(array)
    print(output)
