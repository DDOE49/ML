t = []
i = 0


def remove_one(x, xs):
    global t
    if xs != []:
        if x == xs[0]:
            xs.remove(x)
            t.extend(xs)
            d = t
            t = []
            return d
        else:
            t.append(xs[0])
            if (len(xs) == 1):
                d = t
                t = []
                return d
            return remove_one(x, xs[1:])
    else:
        return xs


def remove_one_loop(x, xs):
    res = []
    return remove_one_loop2(x, xs, res)


def remove_one_loop2(x, xs, res):
    if xs != []:
        if x == xs[0]:
            xs.remove(x)
            res.extend(xs)
            return res
        else:
            res.append(xs[0])
            if (len(xs) == 1):
                return res
            return remove_one_loop2(x, xs[1:], res)
    else:
        return xs


def remove_one_while(x, xs):
    global i
    while i < len(xs):
        if (len(xs) == 0):
            return xs
        if (x == xs[i]):
            xs.remove(x)
            i = 0

            return xs
        i += 1
    i = 0
    return xs


# Test Code
print(remove_one(3,[]))
print(remove_one(3,[3]))
print(remove_one(3,[3,3,3,3]))
print(remove_one(3,[2]))
print(remove_one(3,[2,3,2,3]))
print(remove_one(3,[2,2,2,3]))
print(remove_one(3,[2,2,2,2]))
print()
print(remove_one_loop(3,[]))
print(remove_one_loop(3,[3]))
print(remove_one_loop(3,[3,3,3,3]))
print(remove_one_loop(3,[2]))
print(remove_one_loop(3,[2,3,2,3]))
print(remove_one_loop(3,[2,2,2,3]))
print(remove_one_loop(3,[2,2,2,2]))
print()
print(remove_one_while(3,[]))
print(remove_one_while(3,[3]))
print(remove_one_while(3,[3,3,3,3]))
print(remove_one_while(3,[2]))
print(remove_one_while(3,[2,3,2,3]))
print(remove_one_while(3,[2,2,2,3]))
print(remove_one_while(3,[2,2,2,2]))