input_temp = input()
alpha = input_temp[0]
num = int(input_temp[1])

case_num = 0

if 'b' < alpha < 'g':
    if 2 < num < 7:
        case_num = 8
    elif num == 1 or num == 8:
        case_num = 4
    elif num == 2 or num == 7:
        case_num = 6
elif alpha == 'b' or alpha == 'g':
    if 2 < num < 7:
        case_num = 6
    elif num == 1 or num == 8:
        case_num = 3
    elif num == 2 or num == 7:
        case_num = 4
elif alpha == 'a' or alpha == 'h':
    if 2 < num < 7:
        case_num = 4
    elif num == 1 or num == 8:
        case_num = 2
    elif num == 2 or num == 7:
        case_num = 3

print(case_num)