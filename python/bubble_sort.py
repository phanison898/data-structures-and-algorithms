class BubbleSort:

    def sort(self, list):
        for i in range(len(list) - 1):
            for j in range(len(list) - i - 1):
                if list[j] > list[j + 1]:
                    temp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = temp


if __name__ == "__main__":
    list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    bubble_sort = BubbleSort()
    bubble_sort.sort(list)

    print(list)
