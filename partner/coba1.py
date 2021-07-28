# importing required module
from tkinter import *
# Tkinter Library GUI
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
from tkinter import filedialog
import tkinter.messagebox
import sys
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path
import xlsxwriter

# this module helps to
# play the converted audio
import os

# create tkinter window
root = Tk()

global file, header, data, indicator

# styling the frame which helps to
# make our background stylish
frame1 = Frame(root,
			bg = "lightPink",
			height = "150")

# plcae the widget in gui window
frame1.pack(fill = X)


frame2 = Frame(root,
			bg = "lightgreen",
			height = "750")
frame2.pack(fill=X)	





# styling the label which show the text
# in our tkinter window
label = Label(frame1, text = "Risk Ranking",
			font = "bold, 15",
			bg = "lightpink")

label.place(x = 180, y = 70)



# entry is used to enter the text
entry = Entry(frame2, width = 45,
			bd = 4, font = 14)

entry.place(x = 130, y = 52)	

entry1 = Entry(frame2, width = 45,
			bd = 4, font = 14)

entry1.place(x = 130, y = 90)	

label1 = Label(frame2, text = "Data Valid : ",
			font = "bold, 10",
			bg = "lightgreen")

label1.place(x = 50, y = 90)	

entry2 = Entry(frame2, width = 45,
			bd = 4, font = 14)

entry2.place(x = 130, y = 120)	

label2 = Label(frame2, text = "Skor Risk : ",
			font = "bold, 10",
			bg = "lightgreen")

label2.place(x = 50, y = 120)	

entry3 = Entry(frame2, width = 45,
			bd = 4, font = 14)

entry3.place(x = 130, y = 150)	

label2 = Label(frame2, text = "Level : ",
			font = "bold, 10",
			bg = "lightgreen")

label2.place(x = 50, y = 150)

# define a function which can
# get text and convert into audio
def getHeader(file):
    with open(file, 'r', encoding='utf8', errors="ignore") as infile:
        soup = BeautifulSoup(infile,'html.parser')
        headerList = []

        # Get Header Data
        header = soup.find_all("table")[2].find("tr")
        for items in header:
            try:
                headerList.append(items.get_text())
            except:
                continue
        # print("List Header : :",headerList)
        return headerList

def getMainData(file, header):
    with open(file, 'r',encoding='utf8', errors="ignore") as infile:
        soup = BeautifulSoup(infile,'html.parser')
        data = []

        # Get Main Data
        HTML_data = soup.find_all("table")[2].find_all("tr")[1:]
        for element in HTML_data:
            sub_data = []
            for sub_element in element:
                try:
                    sub_data.append(sub_element.get_text())
                except:
                    continue
            data.append(sub_data)

        dataframe = pd.DataFrame(data=data, columns=header)

        return dataframe

# Get sum of indicator data
def findVariable(header, data, indicator):        
    result_indicator = 0
    for column in header:
        for variable in indicator:
            if column == variable:
                # print(column, "Detect")
                dataframe = data[column].value_counts().sum()
                blank = sum(data[column] == '')
                result_indicator = dataframe-blank
                # print('Jumlah Data :', sum_data,"\n")
    return result_indicator
# institute_name_sum = findVariable(institute_name)

# Directory Information
institute_name = ["kampus", "campus", "universitas", "institut", "sekolah", "madrasah", "university", "school",]
accreditation = ['akreditasi', 'accreditation']
institute_address = ['alamat', 'address']
institute_number = ['number', 'no', 'phone']

# Educational Information
educational_history = ['riwayat_pendidikan', 'educational_history']
educational_medicine = ['catatan_rekam_medis', 'medicine']
educational_grade =[ 'grade', 'nilai']

# Personally Identifiable
personal_number = ['number', 'no', 'phone']
personal_address = ['address', 'alamat']
personal_birthday = ['birthday', 'bornday', 'tanggal_lahir']
personal_religion = ['agama', 'religion']
personal_gender = ['gender', 'jenis_kelamin']
personal_parent = ['orang_tua', 'parent', 'parent_name', 'parents']
personal_photo = ['photo', 'foto']	


# Get sum of a column data on every file

    



def play():	
	file1 = filedialog.askdirectory()	
	entry.insert(0, file1)	
	path = r'file1'
	assert os.path.isfile(path)
	with open(path, "r") as f:
	    pass			
	total_institute_name = total_accreditation = total_institute_address = total_institute_number = 0
	total_educational_history = total_educational_medicine = total_educational_grade = 0
	total_personal_number = total_personal_address = total_personal_birthday = total_personal_religion = total_personal_gender = total_personal_parent = total_personal_photo = 0		
	header = getHeader(file)			
	data = getMainData(file, header)		
	if file.is_file():
		total_institute_name += findVariable(header, data, institute_name)			
		total_accreditation += findVariable(header, data, accreditation)	
		total_accreditation += findVariable(header, data, accreditation)			
		total_institute_address += findVariable(header, data, institute_address)			
		total_institute_number += findVariable(header, data, institute_number)			
		total_educational_history += findVariable(header, data, educational_history)			
		total_educational_medicine += findVariable(header, data, educational_medicine)			
		total_educational_grade += findVariable(header, data, educational_grade)			
		total_personal_number += findVariable(header, data, personal_number)			
		total_personal_address += findVariable(header, data, personal_number)			
		total_personal_birthday += findVariable(header, data, personal_birthday)			
		total_personal_religion += findVariable(header, data, personal_religion)			
		total_personal_gender += findVariable(header, data, personal_gender)			
		total_personal_parent += findVariable(header, data, personal_parent)			
		total_personal_photo += findVariable(header, data, personal_photo)		
				
		print("Directory Information")
		print("Nama Institusi : ", total_institute_name)
		print("Akreditasi : ", total_accreditation)
		print("Alamat Institusi : ", total_institute_address)
		print("Nomor Telepon : ", total_institute_number,"\n")
		print("Educational Information")
		print("Riwayat Pendidikan : ", total_educational_history)
		print("Catatan Rekam Medis : ", total_educational_medicine)
		print("Nilai : ", total_educational_grade,"\n")
		print("Personally Identifiable")
		print("No Hp Siswa : ", total_personal_number)
		print("Alamat Rumah Siswa : ", total_personal_address)
		print("Tempat Tanggal Lahir : ", total_personal_birthday)
		print("Agama : ", total_personal_religion)
		print("Jenis Kelamin : ", total_personal_gender)
		print("Nama Orang Tua : ", total_personal_parent)
		print("Foto Diri : ", total_personal_photo)
			# End Result
		directory_information = total_institute_name + total_accreditation + total_institute_address + total_institute_number
		educational_information = total_educational_history + total_educational_medicine + total_educational_grade
		personally_identifiable = total_personal_number + total_personal_address + total_personal_birthday + total_personal_religion + total_personal_gender + total_personal_parent + total_personal_photo
		print("Directory Information : ", directory_information)
		print("Educational Information : ", educational_information)
		print("Personally Identifiable : ", personally_identifiable)	
		total = directory_information+educational_information+personally_identifiable	
		entry1.insert(0, total)	
		valids=total	
		mins= 24.0	
		maxs= 1337.0	
		batas_min = 0.0	
		batas_max = 10.0	
		normalisasi = (valids-mins)/(maxs-mins)	
		skors = float(normalisasi)	
		skors = normalisasi *(batas_max-batas_min)+batas_min	
		entry2.insert(0, skors)	
		if (skors < 3.9):	
			tkinter.messagebox.showinfo("Risk Ranking SITIAPNF", "Hasilnya : Low")	
			entry3.insert(END, "Low")	
			return	
		elif ((skors > 4.0) and (skors <= 7.0)):	
			tkinter.messagebox.showinfo("Risk Ranking SITIAPNF", "Hasilnya : Medium")	
			entry3.insert(END, "Medium")	
			return	
		else :	
			tkinter.messagebox.showinfo("Risk Ranking SITIAPNF", "Hasilnya : High")	
			entry3.insert(END, "High")	
			return	

# cereate a button which holds
# our play function using command = play
btn = Button(frame2, text = "SUBMIT",
			width = "15", pady = 10,
			font = "bold, 15",
			command = play, bg='yellow')

btn.place(x = 250,
		y = 250)

# give a title
root.title("SITIAPNF")	
root.title("SITIAPNF Risk Ranking")   
p1 = PhotoImage(file = 'apk.png')   #logo aplikasi
root.iconphoto(False, p1)



# we can not change the size
# if you want you can change
root.geometry("650x550+350+200")

# start the gui
root.mainloop()
