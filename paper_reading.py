with open('input.txt', 'r') as f:
    arr = f.readlines()
    f.close()
print(arr)

out_strs = []
out_str = ''
for element in arr:
    if element == '\n':
        out_strs.append(out_str)
        out_str = ''
    else:
        out_str += ' ' + element.split('\n')[0]
out_strs.append(out_str)

with open('out.txt', 'w') as f:
    for element in out_strs:
        f.write(element.strip())
        f.write('\n\n')
    f.close()