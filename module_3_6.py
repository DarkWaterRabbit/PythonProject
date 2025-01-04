data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    sum_numb = 0
    sum_str = 0


    def recurse(Perm):
        nonlocal sum_numb, sum_str
        if isinstance(Perm, list) or isinstance(Perm, tuple) or isinstance(Perm, set):
            for i in Perm:
                recurse(i)
        elif isinstance(Perm, dict):
            for value in Perm.values():
                recurse(value)
            for key in Perm.keys():
                recurse(key)
        elif isinstance(Perm, int) or isinstance(Perm, str):
            if isinstance(Perm, int):
                sum_numb += Perm
            elif isinstance(Perm, str):
                sum_str += len(Perm)

    recurse(data_structure)
    return sum_numb + sum_str

result = calculate_structure_sum(data_structure)
print(result)
