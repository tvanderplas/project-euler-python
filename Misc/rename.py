import os

for file in os.listdir():
	if file[0] == 'P':
		os.rename(file, file.replace('Project Euler ', 'pe_'))