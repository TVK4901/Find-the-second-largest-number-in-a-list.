def second_largest(input_list):
    if len(input_list) < 2:
        return None 

    largest = 0
    second_largest=largest

    for num in input_list:
        if num > largest:  
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:  
            second_largest = num

    return second_largest


input_list = [10, 20, 4, 45, 99]
output = second_largest(input_list)
print(output)  
