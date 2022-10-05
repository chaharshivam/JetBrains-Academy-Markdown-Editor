num = input()
running_sum = 0
new_list = [int(x) for x in num]
running_sum_list = list()
for i in new_list:
    running_sum += i
    running_sum_list.append(running_sum)
print(running_sum_list)
