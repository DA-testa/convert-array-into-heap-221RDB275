# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range(n // 2, -1, -1):
        sort_heap(data, i, n)
    return swaps

def sort_heap(data, i, swaps):
    lChild = 2 * i
    rChild = 2 * i + 1
    mz = i
    if lChild < n:
        mz = lChild
    if rChild < n:
        mz = rChild
    if i != mz:
        swaps.append((i, mz))
        sort_heap(data, mz, swaps)

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    # input from keyboard
    input_type = input()
    if input_type == "I":
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    # checks if lenght of data is the same as the said lenght
        
    elif input_type == "F":
        file_name = input()
        path = "./test/" + file_name
        with open(path, 'r', encoding = 'utf-8') as test:
            n = int(test.readline())
            data = list(map(int, test.readline().split()))
            assert len(data) == n
    else:
        return

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
