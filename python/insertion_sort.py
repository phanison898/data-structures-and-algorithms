class InsertionSort:

    def sort(self, list):
        for i in range(1, len(list)):
            key = list[i]
            j = i - 1
            while j >= 0 and list[j] > key:
                list[j + 1] = list[j]
                j = j - 1
            list[j + 1] = key


if __name__ == "__main__":
    list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    insertion_sort = InsertionSort()
    insertion_sort.sort(list)

    print(list)
