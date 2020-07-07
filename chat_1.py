# structure of coding

def read_file(filename):
	lines = []
	with open(filename, 'r') as f:
		for line in f:
			lines.append(line.strip()) # strip to delet \n
	return lines

def convert(lines):
	new = []
	person = None # 宣告預設值
	for line in lines:
		if line == 'Shang-Jung Wu':
			person = 'Shang-Jung Wu'
			continue
		elif line == 'Po-Jen':
			person = 'Po-Jen'
			continue
		if person: #如果person有值才執行
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()



