def smallest(ns):
    if len(ns) != 0:
        bottom = ns[0]

    def loop(ns, bottom):
        if ns != []:
            if ns[0] < bottom:
                ns.remove(ns[0])
                return smallest(ns)
            else:
                ns.remove(bottom)
                return smallest(ns)
        else:
            return bottom

    if len(ns) == 0:
        return None
    else:
        return min(ns)


def smallest_while(ns):
    i = 0
    j = 0
    res = 0

    if len(ns) == 0:
        return None
    if len(ns) == 1:
        return ns[0]

    while i < len(ns):
        j = i + 1
        if j >= len(ns):
            j = len(ns) - 1
        if ns[i] < ns[j]:
            res = ns[i]
        else:
            res = ns[j]
        i += 1

    return res


def smallest_for(ns):
    if len(ns) == 0:
        return None
    if len(ns) == 1:
        return ns[0]

    res = ns[0]

    for i in ns:

        if i < res:
            res = i
        else:
            res = res
    return res


# Test Code
print(smallest([5,2,3,6,4,3,7,5,8,2]))
print(smallest([5,2]))
print(smallest([5]))
print(smallest([]))
print()
print(smallest_while([5,2,3,6,4,3,7,5,8,2]))
print(smallest_while([5,2]))
print(smallest_while([5]))
print(smallest_while([]))
print()
print(smallest_for([5,2,3,6,4,3,7,5,8,2]))
print(smallest_for([5,2]))
print(smallest_for([5]))
print(smallest_for([]))