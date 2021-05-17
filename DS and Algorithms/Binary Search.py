def log(msg) -> None:
    print("--------------------------------------------")
    print(msg)
    print("--------------------------------------------")


def binarySearch(list_of_elems=[], element_to_search=None) -> bool:
    if len(list_of_elems) and element_to_search:
        log(list_of_elems)
        left_index, right_index = 0, len(list_of_elems)-1
        while left_index <= right_index:
            middle_index = round((left_index+right_index)/2)
            log(f'${left_index},{middle_index},{right_index}')
            middle_element = list_of_elems[middle_index]
            if(middle_element == element_to_search):
                return True
            elif(middle_element > element_to_search):
                log('Into middle_element > element_to_search')
                right_index = middle_index-1
            else:
                log('Into middle_element < element_to_search')
                left_index = middle_index+1
    return False


if __name__ == '__main__':
    list_of_elems = [int(element)
                     for element in input("Enter the List elements:").split()]
    element_to_search = int(input("Enter the Element to search:"))
    # sample input
    # list_of_elems = [2, 3, 6, 4, 5, 8, 9, 7, 55]
    # element_to_search = 5

    print(binarySearch(sorted(list_of_elems), element_to_search))
