import os
import subprocess

wd = os.getcwd()
os.chdir('..')
os.chdir('Challenges')
for file in os.listdir():
	if file[-4].isdigit():
		command = subprocess.run('python ' + file, capture_output=True)
		print(command.args, command.stdout.decode('ascii'))
os.chdir(wd)