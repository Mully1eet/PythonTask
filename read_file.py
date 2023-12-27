import pandas


def get_avg_age(filename):
    r = pandas.read_table(filename, sep=",")
    out = dict()
    for row in r.values:
        if out.get(row[2]):
            out[row[2]] = (out[row[2]] + row[1]) / 2
        else:
            out[row[2]] = row[1]
    return out

