
lines = []
with open('[LINE] 3.txt', 'r') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split('\t')
	time = s[0][:5]
	name = s[0][5:]
	print(time, name)