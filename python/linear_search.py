class LinearSearchAlgorithm:

    def linear_search(self, list, target):
        for index, value in enumerate(list):
            if value == target:
                return index
        return -1


if __name__ == "__main__":

    list = [3, 5, 22, 8, 123, 6]
    target = 5

    linearSearchAlgorithm = LinearSearchAlgorithm()
    output = linearSearchAlgorithm.linear_search(list, target)

    if output >= 0:
        print(f" Element {target} found at index of {output} int the list {list}")
    else:
        print(f" Element {target} not found in the list {list}")
