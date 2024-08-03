data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(args):
    counter = 0
    for i in args:
        if isinstance(i, list):
            counter += sum(i)
    for j in args:
        if isinstance(j, dict):
            counter += sum(j.values())
            j = list(j)
            for q in j:
                if isinstance(q, str):
                    counter += len(q)
    for w in args:
        if isinstance(w, tuple):
            for l in w:
                if isinstance(l, int):
                    counter += l
            for b in w:
                if isinstance(b, dict):
                    counter += sum(b.values())
            for d in w:
                if isinstance(d, dict):
                    d = list(d)
                    for o in d:
                        if isinstance(o, str):
                            counter += len(o)
    for r in args:
        if isinstance(r, str):
            counter += len(r)
    for z in args:
        if isinstance(z, tuple):
            for p in z:
                if isinstance(p, list):
                    for x in p:
                        if isinstance(x, set):
                            for x1 in x:
                                if isinstance(x1, tuple):
                                    for x2 in x1:
                                        if isinstance(x2, int):
                                            counter += x2
                                        elif isinstance(x2, str):
                                            counter += len(x2)
                                        elif isinstance(x2, tuple):
                                            for x3 in x2:
                                                if isinstance(x3, str):
                                                    counter += len(x3)
                                                elif isinstance(x3, int):
                                                    counter += x3
    return counter


result = calculate_structure_sum(data_structure)
print(result)
