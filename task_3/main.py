files = ['1.txt', '2.txt', '3.txt']

content = {}
for file_name in files:
	with open(file_name, 'r', encoding='utf-8') as file:
		lines = file.readlines()
		content[file_name] = lines


for file_name, lines in content.items():
	content[file_name] = [f'{file_name}\n', f'{len(lines)}\n'] + lines

sorted_content = {k: v for k, v in sorted(content.items(), key=lambda item: item[1][1])}

with open('result.txt', 'w', encoding='utf-8') as file:
	for lines in sorted_content.values():
		file.writelines(lines)
