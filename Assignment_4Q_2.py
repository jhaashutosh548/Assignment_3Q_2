def triple_numbers(lst):
    tripled_list = list(map(lambda num: num * 3, lst))
    return tripled_list
input_list = [1, 2, 3, 4, 5, 6, 7]
result = triple_numbers(input_list)
print(result)