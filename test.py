import datetime


def aa(wrd, string):
	if wrd.lower() in string:
		print("True")
		print(string)
	else:
		print("Bleh")	
	


if __name__ == '__main__':
	aa("mum", "My mum was sleeping yesterday")	