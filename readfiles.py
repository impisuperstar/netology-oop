
FILES = ['1.txt', '2.txt']


def write_with_sort(FILES):
    files = []
    result = ''
    for file in FILES:
        with open(file) as f:
            output = f.readlines()
            files.append(
                {'name': file, 'length': len(output), 'output': output})

    sorted_by_age = sorted(files, key=lambda x: x['length'])
    for file in sorted_by_age:
        result += '{name}\n{length}\n{text}\n'.format(
            name=file['name'], length=file['length'], text=''.join(file['output']))
    return result


print(write_with_sort(FILES))
