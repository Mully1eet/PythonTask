def find_in_different_registers(words: list[str]):
    di = dict()
    forbidden = list()
    out = list()

    for word in words:
        if word in di:
            di[word] += 1
        else:
            di[word] = 1
    for key in di.keys():
        if di[key] > 1:
            forbidden.append(key.lower())
    for key in di.keys():
        if key.lower() not in forbidden and key.lower() not in out:
            out.append(key.lower())
    return out