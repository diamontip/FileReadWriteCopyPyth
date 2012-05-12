#code to write file

#providing name for the file to be created
filename = raw_input("Give name for the file: ")
target = open (filename, 'a') ## a will append, w will over-write 
#providing the content for the file
print "provide three lines of content for the file:"
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
#writing the entered content to the file we just created
print "entered three lines are written to the file"
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#providing information that writing task is completed
print "we have added those text to the file"
target.close()