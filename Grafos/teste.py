def insertion_sort(array):
    for index in range(1, len(array)):
        current_element = array[index]
        while index > 0 and array[index - 1] > current_element:
            array[index] = array[index - 1]
            index -= 1
        array[index] = current_element

array = [9,8,7,6,5,4,3,2,1,0]

def main():
    insertion_sort(array)
    print(array)
if __name__ == '__main__':
    main()