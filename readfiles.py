def read_file(file_name):
    data = {}
    with open(file_name, 'r') as f:
        for i, line in enumerate(list(f)):
            data[i] = float(line)
    return data


data_set=read_file('foo.txt')
print(data_set)