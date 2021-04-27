from xml.etree import ElementTree as ET
from xml.dom import minidom 
import os

subjects={
        "1" : "MATHEMATICS" , 
        "2" : "BIOLOGY" ,
        "3" : "PHYSICS" ,
        "4" : "CHEMISTRY" ,
        "5" : "ENGLISH" ,
        "6" : "HINDI" ,
        "7" : "SANSKRIT"   
    }

class GenerateXML():
    def __init__(self):
        self.root = ET.Element('Student_Details')
           
    def Generate_XML_Elements(self):
       
        print("Please enter respective Sl.No to add subjects to the student , Enter 'q' to quit")
        self.total_grp =int(input("Number of students: "))
        self.root.set("total_students",str(self.total_grp))
        #To create number of students 
        while(self.total_grp >0  ):
            self.std = ET.SubElement(self.root,'Student')
            self.name_std = input("Enter Student Name: ")
            self.std.set('Name',self.name_std)
            self.n=int(input("Enter number of subjects taken by the student: "))
            #To insert subjects into students
            while(self.n >0):
                self.sl_no =input("Enter Subject Number: ")
                if(self.sl_no == 'q'):
                    break
                self.std_sub = ET.SubElement(self.std,'Subject')
                self.std_sub.text = subjects[self.sl_no] 
                self.std_sub.set('Max_Marks','100')
                self.std_sub.set('Min_Marks','35')
                self.marks = input("Enter Marks Obtained: (<=100)")
                self.std_sub.set('Obtained',self.marks)
                if(int(self.marks) < 35):
                       self.std_res = "FAIL"
                else:
                	self.std_res = "PASS"
                self.std_sub.set('Result',self.std_res)
                	
                self.n = self.n- 1
                
            self.total_grp = self.total_grp -1
            
            
#To create formatted XML file
    def XML_Parser(self,fileName):
        
        self.tree_strng = ET.tostring(self.root,'utf-8')
        self.re_struct = minidom.parseString(self.tree_strng)
        self.re_struct = self.re_struct.toprettyxml(indent ="\t")        
        with open (fileName, "w") as files : 
            files.write(self.re_struct)

   

if __name__ == "__main__":
    print("Subjects with respective code : ")
    for key in subjects:
        print(str(key) +" : "+str(subjects[key]))
    gen_xml = GenerateXML()
    gen_xml.Generate_XML_Elements()
    gen_xml.XML_Parser("Student_Subject.xml")
    



    


