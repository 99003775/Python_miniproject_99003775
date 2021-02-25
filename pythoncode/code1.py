# Author Amit Kumar
# Ps No:99003775
# Date 02/25/2021
import re  # import Regular Expression module
    
cycle=int(input("enter number of word"))

 
class Code:  # Class Name
    def __init__(self):  # To initilize obj It is constracter
        self.word = input("Enter keyword\n")  # To take user input
        self.Output_file_name = self.word+".txt"  # to make txt file
        self.Input_file = open("input.txt", 'r')  # open input file in read mode
        self.Output_file = open(self.Output_file_name, "w")  # open output file in write mode
        self.count = 0  # initilize count variable
        
    def Get_Input(self):   # meathod to read  file text
        file_read = self.Input_file.read()  # read file
        file = file_read.split()  # spliting input word
        file1 = re.split(r"\W", str(file))
        return file1  # returning file1 to origin
        
    def Match_Input(self, file1):
        for i in range(len(file1)):  # loop for traverse file1
            match = re.fullmatch(self.word, file1[i], re.M | re.I)  # escapes special characters
            if match:
                self.count += 1  # if match found increase count value
                str1 = file1[i-9]+" "+file1[i-4]+" "+file1[i]+" "+file1[i+4]+" "+file1[i+9]+" "  # for Obtained pattern
                self.Output_file.write(str(str1) + ":")  # convert str1 value in string
                self.Output_file.write("\n")  # for next line
        self.Output_file.write(str(self.count))
    def Shut_file(self):
        self.Input_file.close()  # closing input file
        self.Output_file.close()  # closing outputfile
for loop in range(cycle):
    myobj = Code()  # create object
    file1 = myobj.Get_Input()  # call Get_input meathod
    myobj.Match_Input(file1)  # call Match_input meathod
    myobj.Shut_file()   # close file
