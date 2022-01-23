def bubble_sort(given_list: list):
    swapped = True
    while swapped:
        swapped = False
        for j in range(len(given_list) - 1):
            if given_list[j] > given_list[j + 1]:
                given_list[j], given_list[j + 1] = given_list[j + 1], given_list[j]
                swapped = True
    return given_list
