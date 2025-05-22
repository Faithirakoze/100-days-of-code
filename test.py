def descending_order(num):
    i = 0
    my_list = []
    while num != 0:
        my_list.append(num % 10)
        num = int(num/10)
    for index in range(len(my_list)):
        for number in my_list:
            if my_list[1] != my_list[-1]:
                if my_list[1] <  my_list[i+1]:
                    my_list[1], my_list[i+1] = my_list[i+!], my_list[1]
                i += 1

