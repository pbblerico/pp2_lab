comp_list, fair_amount = {}, 0
for i in range(int(input())):
    student, amount = input().split()
    if student not in comp_list:
        comp_list[student] = int(amount)
    else:
        comp_list[student] += int(amount)
    fair_amount = max(fair_amount, comp_list[student])
lucky, not_lucky = 'is lucky!', 'has to receive {} tenge'
new_comp_list = sorted(comp_list)
for i in new_comp_list:
    if comp_list[i] == fair_amount: print(i, lucky)
    else: print(i, not_lucky.format(fair_amount - comp_list[i]))
    