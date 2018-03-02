
from itertools import islice

filename = 'Vela_to_Hydra_Diff_Originate.txt'
N = 6

def main():

	file = open(filename,'r')
	lines = file.readlines()
	file.close()
	lines_gen = islice(lines, N)
	for line in lines_gen:
		print line

def parse():
	with open(filename, 'r') as infile:
		lines = []
		for line in infile:
			line = line.strip()
			# if line == '' or line is None:
			# 	continue
			print len(lines)
			lines.append(line)
			print 'REGULAR   ',lines

			if len(lines) >= N and lines[4].find('CustomObject') != -1:
				print lines
				print lines[4].find('CustomObject'),lines[-1].find('</CustomObject>')

				if lines[-1].find('</CustomObject>') == -1:
					continue
				else:
					process(lines)
					lines = []
					# break
			elif len(lines) >= N:
				print 'lines > N'
				lines = []

def process(lines):
	print '4  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  ',lines
	with open('output-file.txt', 'a') as the_file:
		# if lines[4].find('CustomObject') != -1:

	    the_file.write(str(lines[1]))
	    the_file.write('\n')
	# print lines


parse()


# main()