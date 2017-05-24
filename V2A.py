import sys
import os

def v2a(file,flag,filePath):
	try:
		if file.endswith(".mp3"):
			os.system('cp '+filePath + '/' + "\"%s\"" %file + ' ' + 'Audio_files/' + filePath + '/' )
			return
		elif file.endswith(".wav"):
			wav2mp3(file,flag,filePath)
		elif file.endswith(".avi") or file.endswith(".flv") or file.endswith(".mp4") or file.endswith(".mov") or file.endswith(".wmv") or file.endswith(".mkv"):
			
			rest2mp3(file,flag,filePath) 
	except Exception as e:
		raise e

def wav2mp3(file,flag,filePath):
	
	file_name,extension = os.path.splitext(file)
	if flag:
		
		conversion2mp3 = 'lame ' +filePath+'/' +"\"%s\"" %file_name  +'.wav' +  ' '+'Audio_files/'+ filePath+'/'+ "\"%s\"" %file_name + '.mp3'
		
		
	else:
		conversion2mp3 = 'lame ' + "\"%s\"" %file_name+ '.wav'  + ' '+'Audio_files/'+ "\"%s\"" %file_name + '.mp3'		
	
	
	os.system(conversion2mp3)

def rest2mp3(file,flag,filePath):
	
	file_name,extension = os.path.splitext(file)
	if flag:
		conversion2wav = 'ffmpeg -i ' + filePath +'/' +'\"%s\"' %file_name + extension + ' ' + filePath+'/'+ "\"%s\"" %file_name + '.wav'
	else:
		conversion2wav = 'ffmpeg -i ' + '\"%s\"' %file_name + extension + ' ' + "\"%s\"" %file_name + '.wav'	
	
	
	os.system(conversion2wav)
	wav2mp3(file,1,filePath)
	delete_wav = 'rm ' +filePath+'/'+ "\"%s\"" %file_name + '.wav'
	os.system(delete_wav)

def recur_dir(filePath):
	for file in os.listdir(filePath):
						
						temp=filePath+'/'+file

						if os.path.isdir(temp):
							os.system('mkdir Audio_files/'+temp)
							recur_dir(temp)
						else:
							v2a(file,1,filePath)	

						
						


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
				raise Exception('File or Directory doesn\'t exist')
				exit(1)
				
		except OSError as error:
				raise error
		
					
		if os.path.isfile(filePath):
					os.system('mkdir Audio_files')
					print('Converting...')
					if(filePath.count('/')>0):
						v2a(filePath,1,filePath)
					else:
						v2a(filePath,0,filePath)
						
					
					

		elif os.path.isdir(filePath):
					os.system('mkdir Audio_files')
					os.system('mkdir Audio_files/' + filePath)
					print('Converting...')
					
					recur_dir(filePath)







if __name__ == '__main__':
	main()
