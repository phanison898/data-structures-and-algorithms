class SearchAlgorithm:

    def linear_search(self, list, target):
        for index, value in enumerate(list):
            if value == target:
                return index
        return -1


if __name__ == "__main__":

    list = [1, 2, 3, 4, 5]
    target = 1

    searchAlgorithm = SearchAlgorithm()
    output = searchAlgorithm.linear_search(list, target)

    print(f"Linear search = {output}")
