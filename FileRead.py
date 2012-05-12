#code to read file

import linecache
#collecting the filename we are about to open for reading
file_name = raw_input("please enter the name of the file you want to read :")
#here we are opening the file we specified earlier
txt_file = open(file_name)
#here we are printing the file content in the command prompt
linecache.getline(txt_file,1)

# text_search = raw_input("please enter what need to be searched")

