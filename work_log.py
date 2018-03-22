import os
import datetime
import csv
import sys
from collections import OrderedDict


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
			fmtd = input("Please use DD/MM/YYYY >>  ")
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
	duration = input("Time spend >>  ")
	clr()
	notes = input("notes(optional, You can leave this empty) >>  ")
	clr()
	log_file(tasktitle, duration, notes, fmtd)
	choice=(input("The entry has been added :) Press enter to return to the menu >>  ")).lower()
	if choice != 'q':
		work_log_start()


def log_file(tasktitle, duration, notes, fmtd):
    """Saving user's entry to a csv file."""
    clr()
    with open('work_log.csv', 'w', newline='') as csvfile:
        fieldnames = ['TaskTitle', 'Duration', 'Notes', 'Date']
        csvfilewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvfilewriter.writeheader()
        csvfilewriter.writerow({
            'TaskTitle': tasktitle,
            'Duration': duration,
            'Notes': notes,
            'Date': fmtd })
    input(" Entry saved! Press enter to continue >>> ")
    work_log_start()




def exitsting_entry():
	while True:
		clr()
		print("""
		Do you want to search by 
		a) Exact Date
		b) Range of Dates
		c) exact Search
		d) Reges Pattern
		e) Return to menu""")
		choice = (input("> ")).lower()
		if choice == "a":
			search_by_date()
			input("hit enter to go back to the menu")
		elif choice == "b":
			range_of_date()
			input("hit enter to go back to the menu")
		elif choice == "c":
			search_with_string()
			input("hit enter to go back to the menu")	
		#elif choice == "b":
		 
def search_by_date():
	clr()
	logs=[]
	exitsting_entries=[]
	with open('work_log.csv', newline="") as csvfile:
		reader=csv.DictReader(csvfile, delimiter=",")
		rows = list(reader)
		for line in rows:
			exitsting_entries.append(line["Date"])
	print(exitsting_entries)		
	exact_date=(input("Tell me the exact date of your entry >> ")).lower()
	#exact_date = datetime.datetime.strptime(exact_date, "%d/%m/%Y")
	with open('work_log.csv', newline="") as csvfile:
		reader=csv.DictReader(csvfile, delimiter=",")
		rows = list(reader)
		for line in rows:
			if line['Date']==exact_date:
				logs.append(line)
	return print(logs)	

def range_of_date():
	clr()
	logs=[]
	while True:
		try:
			date1 = input("put the start date(DD/MM/YYYY) >>  ")			
			date2 = input("enddte(DD/MM/YYYY) >>  ")
		except ValueError:
			print("not the right value")	
	with open('work_log.csv', newline="") as csvfile:
		reader=csv.DictReader(csvfile, delimiter=",")
		rows = list(reader)
		for line in rows:
			if line['Date']>=line["Date"] and line['Date']<=line["Date"]:
				logs.append(line)
	return print(logs)			

def search_with_string():
	clr()
	result=[]
	word_in_str = input("What word are you looking for???>>")
	with open('work_log.csv', newline="") as csvfile:
		reader=csv.DictReader(csvfile, delimiter=",")
		rows = list(reader)
		for line in rows:
			if word_in_str in line['TaskTitle'] or word_in_str in line["Notes"]:
				result.append(line)
		else:
			print("nothing related to that word sorry!")
	return print(result)			
					
				

def search_by_pattern():
	clr()
	result=[]
	word_in_str = input("What pattern are you looking for???>>")


def work_log_start():
	while True:
		home_menu()
		choice = (input("> ")).lower()
		if choice == "c":
			print("Have a nice day! bye")
			
		elif choice == "a":
			new_entry()
		elif choice == "b":	
			exitsting_entry()
			pass
		else:
			choice=input("\n Invalid option!! Please use the menu. Enter either 'a', 'b', or 'c'. Press enter to continue")
			menu()
			break	
    	


if __name__=="__main__":
	work_log_start()
			



