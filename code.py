# it will replace if there is same name of two file 
#if file has no extension then it will create folder of file name and move it in the folder

import os
import shutil 

 # function for get extension
def get_extension(path): 
	y=path.split('/')
	last=y[len(y)-1]
	a=last.split('.')
	ext=a[len(a)-1]
	return ext


# function for get file name
def file_name (path):			
	y=path.split('/')
	last=y[len(y)-1]
	return last

	
destination_folder = '/home/dharmendra/Desktop/myfolder'
source_folder= '/home/dharmendra/Desktop/pl'
#bigfiles=[0 for x in range(10)]
#dir_bigfiles=[0 for x in range(10)]
bigfiles={}
filetree = [os.path.join(r,file) for r,d,f in os.walk(source_folder) for file in f]
for files in filetree:
	temp=os.path.getsize(files)/1000000.0		#change size byte to MB
	bigfiles[files]=temp;

#for key ,value in sorted(bigfiles.iteritems(),key=lambda (k,v):(v,k)):
ff=sorted(bigfiles.items(),key=lambda x:x[1] ,reverse = True)


for i in range(0,10):
	print(ff[i])
	print("\n")

for fil in filetree:
	source_files = fil
	ext=get_extension(source_files)
	domain=destination_folder+"/"+ext
	if not os.path.exists(domain):
		os.makedirs(domain)
	if os.path.exists(domain+file_name(source_files)):
		os.remove(domain+file_name(source_files))
	shutil.copy(source_files, domain)