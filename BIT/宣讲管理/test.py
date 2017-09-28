
def a():
    fail_list = []
    for i in range(3):
        fail_case = {}
        fail_case['a'] = 'a'
        fail_case['b'] = 'b'
        fail_list.append(fail_case)
    #print(fail_list)
    return fail_list
print(a())
print(a())


