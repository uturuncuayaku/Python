
def main():
    n_numbers = []
    n_list = []
    
    for index in range(100,150):
        n_list.append(index)
    print(n_list)

    for n in n_list:
        n_numbers.append(list(str(n)))
    print(n_numbers)

    for i in range(len(n_numbers)):
        for j in range(len(n_numbers[i])):
            print(int(n_numbers[i][j]), end=' ')
            # print(int(n_numbers[i][j+1]))
            # if(int(n_numbers[i][j])<= int(n_numbers[i][j+1])):
            #     print(n_numbers[i][j])


    #check conditions of possible passwords
    # for i, value in enumerate(n_numbers):
    #     for j in range(4):
    #         print(n_numbers[i][j])


if __name__ == "__main__":
    main()