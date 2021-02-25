import re
class Code:
    
    def __init__(self):
        self.Keyword=input("Enter keyword\n")
        self.Output_file_name = self.Keyword+".txt"
        self.Input_file=open("input.txt", 'r')
        self.Output_file = open(self.Output_file_name, "w")
        self.count=0
    def Get_Input(self):
        file_read=self.Input_file.read()
        file=file_read.split()
        file1=re.split(r"\W",str(file))
        return file1
    def Match_Input(self,file1):
        for i in range(len(file1)):
            match=re.fullmatch(self.Keyword,file1[i],re.M|re.I)
            if match:
                self.count+=1 
                str1=file1[i-8]+" "+file1[i-4]+" "+file1[i]+" "+file1[i+4]+" "+file1[i+8]+" "
                self.Output_file.write(str(str1) + ":")
                self.Output_file.write("\n")
        self.Output_file.write(str(self.count))
    def Shut_file(self):
        self.Input_file.close()
        self.Output_file.close()



myobj=Code()
file1=myobj.Get_Input()
myobj.Match_Input(file1)
myobj.Shut_file()
