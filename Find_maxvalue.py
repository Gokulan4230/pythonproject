def maxvalue(number_list):
    max_value = 0
    for number in number_list:
        if number > max_value:
            max_value = number
    return max_value
