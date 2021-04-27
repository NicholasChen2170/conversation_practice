import os
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen': #一個小系列
			person = 'Allen'
			continue
		elif line == 'Tom': #一個小系列
			person = 'Tom'
			continue
		if person:
			new.append(person + '：' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	if os.path.isfile('conversation.txt'):
		print('找到檔案！')
	else:
		print('無法讀取檔案')
	lines = read_file('conversation.txt')
	filename = 'conversation,txt'
	lines = convert(lines)
	write_file('outcome.txt', lines) #輸出檔名

main()