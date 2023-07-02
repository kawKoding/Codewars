def same_structure_as(original, other):
    def recursLength(lis):
        count = len(lis)
        for i in lis:
            if isinstance(i, list):
                count = count + recursLength(i)
        return count

    length1 = 0
    length2 = 0
    if type(original) == type(other):
        for arr in original:
            try:
                length1 += recursLength(arr)
            except:
                1 == 1
        for ar in other:
            try:
                length2 += recursLength(ar)
            except:
                1 == 1
    else:
        return False

    for pos, val in enumerate(original, 0):
        if isinstance(val, str):
            original = original.pop(pos)

    for pos, val in enumerate(other, 0):
        if isinstance(val, str):
            other = other.pop(pos)

    lengthDict1 = {

    }

    lengthDict2 = {

    }

    def recursNest(lis):
        count = 1
        for l in lis:
            if isinstance(l, list):
                count = count + 1 + recursNest(l)
        return count

    i = 0
    while i != len(original):
        try:
            for pos, elem in enumerate(original, 1):
                try:
                    lengthDict1[f"nestLengthSubOt{pos}"] = recursNest(elem)
                    i += 1
                except:
                    lengthDict1[f"nestLengthSubOt{pos}"] = 0
                    i += 1
        except (TypeError, IndexError) as error:
            lengthDict1[f"nestLengthSubOt{pos}"] = 0
            i += 1

    v = 0
    while v != len(other):
        try:
            for pos, elem in enumerate(other, 1):
                try:
                    lengthDict2[f"nestLengthSubOt{pos}"] = recursNest(elem)
                    v += 1
                except:
                    lengthDict2[f"nestLengthSubOt{pos}"] = 0
                    v += 1
        except (TypeError, IndexError) as error:
            lengthDict2[f"nestLengthSubOt{pos}"] = 0
            v += 1

    if (lengthDict1 == lengthDict2) & (length1 == length2):
        return True
    else:
        return False