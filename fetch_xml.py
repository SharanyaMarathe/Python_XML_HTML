import xml.etree.ElementTree as ET
import os


class fetch_xml_details():

        def __init__(self,fileName):
                self.std_tree = ET.parse(fileName)
                self.std_root = self.std_tree.getroot()
                
        def fetch_student_details(self):
               
                for self.grps in self.std_root:
                        print("<----->"+(self.grps.attrib['Name'])+"<----->")
                        for self.sub in self.grps:
                            print("Subjects: "+str(self.sub.text))
                            print("Result: "+str(self.sub.attrib['Result']))
                                        
             
if __name__ == "__main__":
    gen = fetch_xml_details('Student_Subject.xml')
    gen.fetch_student_details()

	
	
