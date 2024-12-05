def balancer(input_str):
    open_count = 0
    change_to_open = 0

    for char  in input_str:
        if char == '(':
            open_count += 1
        else: #char == ')'
            if open_count > 0:
                open_count -= 1
            else:
                change_to_open += 1
                open_count += 1

    return change_to_open + open_count / 2


input_str = input()
print(int(balancer(input_str)))
