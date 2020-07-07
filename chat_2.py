# structure of coding

def read_file(filename):
	lines = []
	with open(filename, 'r') as f:
		for line in f:
			lines.append(line.strip()) # strip to delet \n
	return lines

def convert(lines):
	new = []
	person = None # 宣告預設值，Hint: when to create a variable and store an infor temporarily
	pt_word_count = 0
	pt_sticker_count = 0
	pt_good_count = 0
	yl_word_count = 0
	yl_sticker_count = 0
	yl_good_count = 0
	for line in lines:
		s = line.split('\t')
		time = s[0]
		name = s[1]
		if name == '曾柏仁':
			if s[2] == '[貼圖]':
				pt_sticker_count += 1
			elif s[2] == '☎ 未接來電':
				pt_good_count += 1
			else:
				for msg in s[2:]:
					pt_word_count += len(msg)
		elif name == '佑容':
			if s[2] == '[貼圖]':
				yl_sticker_count += 1
			elif s[2] == '☎ 未接來電':
				yl_good_count += 1
			else:
				for msg in s[2:]:
					yl_word_count += len(msg)
	print('pt says', pt_word_count, 'words')
	print('pt sends', pt_sticker_count, 'stickers')
	print('pt missed', pt_good_count, 'call' )

	print('yl says', yl_word_count, 'words')
	print('yl sends', yl_sticker_count, 'stickers')
	print('yl missed', yl_good_count, 'call' )

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('[LINE] 與佑容的聊天.txt')
	convert(lines)
	# write_file('output.txt', lines)


main()



