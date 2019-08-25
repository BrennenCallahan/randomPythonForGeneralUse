import xlrd
import xlwt
filename=raw_input("What is the name of your excel file? ")
workbook = xlrd.open_workbook(filename)
worksheet = workbook.sheet_by_name('Sheet1') #don't touch


#find number of rows to parse
excel_sheet = workbook.sheet_by_index(0)
noRows=excel_sheet.nrows





#this block will create the required XML header,  
XML=raw_input("What would you like your xml file to be called (dont write '.xml')?")
newFile=open("temp.xml","w+")
header1=raw_input("What is the name of the application? ")
header2=raw_input("What is the category of this application? ")
header3=raw_input("Who is the vendor of this application? ")
header4=raw_input("What is the appID of this application? ")
str1='<Application-Component ATTRIBUTEYOUWANT="'+header1+'" ATTRIBUTEYOUWANT="'+header1+'" ATTRIBUTEYOUWANT="'+header2+'" ATTRIBUTEYOUWANT="'+header3+'" ATTRIBUTEYOUWANT="'+header4+'" >'+"\n"
newFile.write(str1)#writes the above header to new file


#this block is where you determine which columns to parse and converts the string to an int.
number1=raw_input("Please enter the number of the column you want to parse for the process name.")
number2=raw_input("Please enter the number of the column you want to parse for the ports.")
number3=raw_input("Please enter the number of the column you want to parse for the commandLine.")
int_n1=int(number1)
int_n2=int(number3)
int_n3=int(number3)



#loops through  process signature, port, cmdline columns, row by row, if the entry is empty, populates it with ""
#parse 1-3 are the attributes you are parsing the data sheet for, REPLACE THEM WITH THE ATTRIBUTE NAMES YOU WANT FOR YOUR XML


for x in range (1,noRows):
 #-------------LOOP THROUGH PROCESS SIGNATURES-----------" 
 emptyParse1='<parse1=""'
 emptyParse2=' parse2=""'
 emptyParse3=' parse3="" />\n'

# templateEmpty= ' template=""'

 if worksheet.cell(x,int_n1).value != '':
   parse1= worksheet.cell(x,int_n1).value
   str2='<parse1="'+parse1+'"'
   
   
   newFile.write(str2)
 else:
   newFile.write(emptyParse1)


 # ------------------LOOP THROUGH PORTS-------------"

 if worksheet.cell(x,int_n2).value != '':
    parse2=worksheet.cell(x,int_n2).value
    str3=' parse2="'+str(parse2)+'"'
    
    newFile.write(str3)
   
 
 else:
     newFile.write(emptyParse2)


 # ----------------LOOP THROUGH COMMANDLINE------------"

 if worksheet.cell(x,int_n3).value != '':
    parse3= worksheet.cell(x,int_n3).value
    str4=' cmdline="'+parse3+'" />\n'
    newFile.write(str4)
 else:
   newFile.write(emptyParse3)

######################################################################################
#template loop copy and fill in the column, and the name of the attribute, can go in the middle before or after port, due to closing on cmdline
# if worksheet.cell(x,int_numberX).value != '':
#    parseX=worksheet.cell(x, int_numberX).value
#    strx=' template="'+str(templateEmpty)+'"'
    
#    newFile.write(strX)


# else:
#     newFile.write(templateEmpty)
#######################################################################################




#close file, at this point there will be all of the required info, and then empty entries for empty rows that were included
newFile.close()#close temp.xml



#clean file of empty rows matching delete_list
infile ="temp.xml"
outfile =XML+".xml"         #creates the final XML file with the name  the user input
delete_list = ['<parse1="" parse2="" parse3="" />',"\n"] #ADD WHATEVER YOU WANT HERE TO CLEAN YOUR FILE AUTOMATICALLY OF THOSE ENTRIES
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:

    for word in delete_list:

        line = line.replace(word, "") #REPLACES WORDS IN DELETE_LIST WITH ""

    fout.write(line)

fin.close()


closeXML="\n</Application-Component>"
fout.write(closeXML)
fout.close()


