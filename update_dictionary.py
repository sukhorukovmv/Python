#!/usr/bin/python3

def update_dictionary(d, key, value):
    if key in d:
        d.setdefault(key, []).append(value)
    else:
        d.setdefault(2 * key, []).append(value)
    return d
d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
