import json

// Overall, the code is well structured and follows logic
// WELL DONE

with open('database.txt', 'r') as data:
    names = data.read()
    name = ''
    for char in names:
        if char.isalpha() or char == ',':
            name += char
        else:
            pass
name = name.split(',')
name = list(set(name))

with open('input.txt', 'r') as inp:
    input_text = inp.read()

count_of_names = {val: 0 for val in name}

for val in name:
    count_of_names[val] += input_text.count(val)
    input_text = input_text.replace(val, 'X')

tmp = count_of_names.copy()
for if_zero in count_of_names:
    if tmp[if_zero] <= 0:
        del tmp[if_zero]
    else:
        pass

print(count_of_names)
output_data = {
    "Text": input_text,
    "ProperNouns": tmp
}
with open('output.json', 'w') as out:
    json.dump(output_data, out, indent=2)
