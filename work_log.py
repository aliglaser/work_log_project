import os
import datetime
import csv
import sys
import collections
import re
import io





def clr():
	"""Clear the console"""
	os.system('cls' if os.name == 'nt' else 'clear')


def home_menu():
	clr()
	print("""
a) Add a new entry
b) Search in existing entries
c) Quit program
""")


def new_entry():
	clr()
	print("Date of the task")
	while True:
		try:
			fmtd = input("Please use (DD/MM/YYYY)>>  ")
			logdate = datetime.datetime.strptime(fmtd, '%d/%m/%Y')
		except ValueError:
			print("You didn't give the valid date XD!!Please try again!")
			continue
		else:	
			if logdate > datetime.datetime.now():
				print("Date can only be now or past Please try again!")
				continue
			else:
				break
	clr()
	tasktitle = input("Title of the task >>  ")
	clr()
	while True:
		duration = input("Duration time (HH:MM)>> ")
		rex = re.compile("^[0-9]{2}:[0-9]{2}")
		if not rex.match(duration):
			input("Not the right form! Hit Enter and try again ")	
		else:
		 break	
	clr()
	notes = input("notes(optional, You can leave this empty) >>  ")
	clr()
	log_file(tasktitle, duration, notes, fmtd)
	


def log_file(tasktitle, duration, notes, fmtd):
    """Saving user's entry to a csv file."""
    clr()
    filename = os.path.join(os.getcwd(),'work_log.csv')
    file_exists = os.path.exists(filename)
    print(filename)
    with open('work_log.csv', 'a', newline='') as csvfile:
    	fieldnames = ['TaskTitle', 'Duration', 'Notes', 'Date']
    	csvfilewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    	if not file_exists:
            csvfilewriter.writeheader()
    	# filename = '/Users/haleylovespurple/Documents/techdgree/work_log_project/work_log.csv'
    	csvfilewriter.writerow({
            'TaskTitle': tasktitle,
            'Duration': duration,
            'Notes': notes,
            'Date': fmtd })
    	print("""
Entry saved! Press enter to continue. 
If you want to edit the info, Hit E
If you want to delete the data, Hit D""")
    deleteOrEdit = (input(">>")).upper()
    if deleteOrEdit == "E":
    	f = open("work_log.csv")
    	lines=f.readlines()
    	lines=lines[:-1]
    	f.close()
    	cWriter = csv.writer(f, delimiter=',')
    	with open("work_log.csv", "w") as out:
    		for line in lines:
    			out.write(line.strip() + "\n")
    	new_entry()
    elif deleteOrEdit == "D":
    	f = open("work_log.csv")
    	lines=f.readlines()
    	lines=lines[:-1]
    	f.close()
    	cWriter = csv.writer(f, delimiter=',')
    	with open("work_log.csv", "w") as out:
    		for line in lines:
    			out.write(line.strip() + "\n")
    	input("Deleted! Hit Enter to continue....>> ")




def exitsting_entry():
	while True:
		clr()
		print("""
		Do you want to search by 
		a) Exact Date
		b) Range of Dates
		c) Search with word
		d) Regex Pattern
		e) Time spent
		f) Return to menu""")
		choice = (input("> ")).lower()
		if choice == "a":
			search_by_date()
			input("Hit 'Enter' to go back to the menu")
		elif choice == "b":
			range_of_date()
			input("Hit 'Enter' to go back to the menu")
		elif choice == "c":
			search_with_string()
			input("Hit 'Enter' to go back to the menu")	
		elif choice == "d":
			search_by_pattern()
			input("Hit 'Enter' to go back to the menu")
		elif choice == "e":
			search_by_duration()
		elif choice == "f":
			break	
		 
def search_by_date():
	clr()
	logs=[]
	exitsting_entries=[]
	with open('work_log.csv', newline="") as csvfile:
		reader=csv.DictReader(csvfile, delimiter=",")
		rows = list(reader)
		for line in rows:
			exitsting_entries.append(line["Date"])
	print("****Existing Dates****")
	for entry in exitsting_entries:
		print(entry)
	
	while True:
		exact_date=input("Tell me the exact date of your entry >> ")
		try:
			exact_date_log = datetime.datetime.strptime(exact_date, "%d/%m/%Y")
		except ValueError:
			input("*******Not The Right Format. Hit Enter to Continue*****")
			continue
		else:
			with open('work_log.csv', newline="") as csvfile:
				reader=csv.DictReader(csvfile, delimiter=",")
				rows = list(reader)
				for line in rows:
					if line['Date']==exact_date:
						logs.append(line)
			for log in logs:
				print("+++++++++++++++++++++++++++++")
				for data in log:
					print(log[data])
	


def range_of_date():
	clr()
	logs=[]
	while True:
		try:
			date1 = input("put the start date(DD/MM/YYYY) >>  ")
			date1_valid = datetime.datetime.strptime(date1, '%d/%m/%Y')
			date2 = input("enddte(DD/MM/YYYY) >>  ")
			date2_valid = datetime.datetime.strptime(date2, '%d/%m/%Y')
		except ValueError:
			print("not the right value")
		else:		
			with open('work_log.csv', newline="") as csvfile:
				reader=csv.DictReader(csvfile, delimiter=",")
				rows = list(reader)
				for line in rows:
					if line['Date']>=line["Date"] and line['Date']<=line["Date"]:
						logs.append(line)
			break			
	if len(logs) <= 0:
		print("No result")
	else:
		for log in logs:
			print("++++++++++++++++++++++++++++++++++++++++")
			for data in log:
				print(log[data])


def search_with_string():
	clr()
	result=[]
	word_in_str = input("What word are you looking for? >> ")
	with open('work_log.csv', newline="") as csvfile:
		reader=csv.DictReader(csvfile, delimiter=",")
		rows = list(reader)
		for line in rows:
			if word_in_str in line['TaskTitle'] or word_in_str in line["Notes"]:
				result.append(line)
	if len(result) > 0:
		for log in result:
				print("++++++++++++++++++++++++++++++++++++++++")
				for data in log:
					print(data +":"+log[data])
	else:				
		print("nothing related to that word sorry!")
				
					
				

def search_by_pattern():
	clr()
	result=[]
	word_in_str = input("What pattern are you looking for???>> ")
	search_pattern = r'' + word_in_str
	with open('work_log.csv', newline="") as csvfile:
		reader=csv.DictReader(csvfile, delimiter=",")
		rows = list(reader)
		for line in rows:
			if re.findall(search_pattern, line['TaskTitle']) or re.findall(search_pattern, line['Notes']):
				result.append(line)
	for log in result:
			print("++++++++++++++++++++++++++++++++++++++++")
			for data in log:
				print(data +":"+log[data])	

def search_by_duration():
	clr()
	result=[]
	exitsting_entries = []
	with open('work_log.csv', newline="") as csvfile:
		reader=csv.DictReader(csvfile, delimiter=",")
		rows = list(reader)
		for line in rows:
			exitsting_entries.append(line["Duration"])		
	for entry in exitsting_entries:
		print("++++++++++++++++++")
		print(entry)
	while True:
		duration = input("Choose the duration time>> ")
		rex = re.compile("^[0-9]{2}:[0-9]{2}")
		if rex.match(duration):
			with open('work_log.csv', newline="") as csvfile:
				reader=csv.DictReader(csvfile, delimiter=",")
				rows = list(reader)
				for line in rows:
					if line['Duration']== duration:
						result.append(line)
			for log in result:
				print("+++++++++++++++++++++++++++++")
				for data in log:
					print(data + ":" +log[data])
		else:
			print("Not the right format")			


		 		


def work_log_start():
	while True:
		home_menu()
		choice = (input("> ")).lower()
		if choice == "c":
			print("Have a nice day! bye")
			break
			sys.exit
		elif choice == "a":
			new_entry()
		elif choice == "b":	
			exitsting_entry()
		else:
			choice=input("\n Invalid option!! Please use the menu. Enter either 'a', 'b', or 'c'. Hit 'Enter' to continue")
			continue
    	



if __name__=="__main__":
	work_log_start()
			



