def open_or_senior(members):

    m = []
    for member in members:
        if member[0] >= 55 and member[1] > 7:
            m.append('Senior')
        else:
            m.append('Open')
    return m
