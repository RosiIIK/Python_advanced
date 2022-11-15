with open('numbers.txt') as file:
    print(sum([int(line_num) for line_num in file.readlines()]))
   
  #line 2 is equal to following:
    # result = 0
    # for line in file.readlines():
    #     current_num = int(line)
    #     result += current_num
    # print(result)
