import sys
import os




def main():
	if(len(sys.argv)==1):
		raise ValueError('Name of the File or Directory is missing!!')
		exit(1)
	else:
		filePath = sys.argv[1]

		try:
			if os.path.exists(filePath):
				print('Path exists :D')
			else:
				raise ValueError('File or Directory doesn\'t exist')
				exit(1)
				
		except OSError as error:
				pass
		if os.path.isfile('filePath'):
					print('Converting...')
					v2a(filePath)

		elif os.path.isdir('filePath'):
					os.system('mkdir Audio_files')
					print('Converting...')
					for file in os.listdir('filePath'):
							v2a(file)			


		



if __name__ == '__main__':
	main()
