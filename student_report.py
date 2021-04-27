import xml.etree.ElementTree as ET
from datetime import datetime, date
import logging
import os


def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)

def add_br_tag(tag):
    return "<%s>" % (tag)
    
def add_link(tag, h, pathoffile, filename):
    return "<%s %s %s >%s </%s>" % (tag, h, pathoffile, filename, tag)


class Html_Report_Generate():
    def __init__(self, filename):
        #to get details from xml file  
        self.tree = ET.parse(filename)
        self.root = self.tree.getroot()
        

    def html_page(self):
        
        self.summary = add_tags('h1 style="font-size:30px;"', 'Report of students of Class 12')
        self.summary += add_tags('h3', 'Total Number of students: ' + str(self.root.attrib['total_students']))
        self.summary += add_tags('h4', 'Time and date of test execution : ' + str(date.today().strftime("%B %d, %Y")) + "  , "+str(datetime.now().strftime("%H:%M:%S")))
        self.summary = add_tags('div style="background-color:white; border:1px; width:500px; display: inline-block;"',self.summary)
        self.summary += add_br_tag('br')
        
        

    def html_table(self):

        sort_table = """function sort_table() {
                  var input, filter, table, tr, td, j,i,ch, txtValue,ele;
                  ele=document.getElementById("List_check")
                  ch=ele.getElementsByTagName("input")
                  for (j=0;j<ch.length;j++){
                    if (ch[j].checked){
                      filter =(ch[j].value.toUpperCase())}
                
                  }
                  table = document.getElementById("myTable");
                  tr = table.getElementsByTagName("tr");
                  
                  // Loop through all table rows, and hide those who don't match the search query
                  for (i = 0; i < tr.length; i++) {
                    td = tr[i].getElementsByTagName("td")[6];
                    
                    if (td) {
                      txtValue = td.textContent || td.innerText;
                      if (txtValue.toUpperCase().indexOf(filter) > -1) {
                        tr[i].style.display = "";
                      } else {
                        tr[i].style.display = "none";
                      }
                    }
                  }
                }
                function read_all(){
                   location.reload()
                   var  chk;
                   chk = document.getElementById("all");
                   chk.checked=True;
                }
                """
        
        self.pass_check = add_tags('input type="checkbox" id="pass" value="Pass" onclick="sort_table()"',
                                   "Pass" )
        self.fail_check = add_tags('input type="checkbox" id="fail" value="Fail" onclick="sort_table()"',
                                   "Fail" )
        
        self.all_check = add_tags('input type="checkbox" id="all" value="All" onclick="read_all()"', "All")
        self.checkBoxes = self.pass_check + self.fail_check + self.all_check
        self.checkBoxes = add_tags('div style="background-color:white; border:1px; width:300px; display: inline-block; font-weight:bold;" id="List_check"', self.checkBoxes)
        self.checkBoxes+=add_br_tag('br')
        self.main_content = self.summary +self.checkBoxes +add_br_tag('br')+add_br_tag('br')
        
        
        self.main_content += add_tags('script', sort_table)

        self.c = 0
        # for creating table add_tags('th','File') +add_tags('td',str(self.ele.attrib['file']))
        self.table_head = add_tags('th', 'SL.NO') + add_tags('th', 'Student Name') + add_tags('th','Subject') + add_tags('th','Maximum Marks') + add_tags('th', 'Minimum Marks') +add_tags('th', 'Obtained Marks') +add_tags('th', 'Result')
        self.table_head = add_tags('tr style="font-weight:bold"', self.table_head)
        
        
        for self.ele in self.root: 
            self.c = self.c + 1
            self.table_data = add_br_tag('br')
            for self.subele in self.ele:
                
                if (str(self.subele.attrib['Result']) == "PASS"):
                     res_data = add_tags('td style="background-color:#393;font-weight:bold"',
                                    str(self.subele.attrib['Result']))
                elif (str(self.subele.attrib['Result']) == "FAIL"):
                     res_data = add_tags('td style="background-color:Salmon ;font-weight:bold"', str(self.subele.attrib['Result']))
            
                self.table_data += add_tags('td', str(self.c)) +add_tags('td',self.ele.attrib['Name'])+add_tags('td', str(self.subele.text)) + add_tags('td', str(self.subele.attrib['Max_Marks']))+ add_tags('td',str(self.subele.attrib['Min_Marks']))+add_tags('td', str(self.subele.attrib['Obtained']))+res_data 
                 
                self.table_data = add_tags('tr', self.table_data)
                
            self.table_head += self.table_data
         
        self.table_head = add_tags('table border=1 width=100% bgcolor=white id="myTable" ', self.table_head)
        
        self.main_content += self.table_head   
        self.main_content = add_tags('html width=100%',self.main_content)  
   
   
    def write_html(self, filename):
        with open(filename, "w+") as f:
            f.write(self.main_content)
        


if __name__ == '__main__':
    xml_file = 'Student_Subject.xml'
    html_file = Html_Report_Generate(xml_file)
    html_file.html_page()
    html_file.html_table()
    html_filename = 'Report.html'
    html_file.write_html(html_filename)
