def binary_search(ls, data):
    first_element = 0
    last_element = len(ls) - 1
    was_found = False
    loops = 0
    while first_element <= last_element and not was_found:
        loops = loops + 1
        mid = (first_element + last_element) // 2
        if ls[mid] == data:
            was_found = True
        else:
            if ls[mid] > data:
                last_element = mid - 1
            else:
                first_element = mid + 1

    print("loops = " + str(loops))
    return was_found

print(binary_search([1, 3, 6, 8, 10, 13, 16, 17,20], 8))
