def createDict(keys, values):

    while len(keys) > len(values):
        values.append(None)

    return dict(zip(keys, values))
