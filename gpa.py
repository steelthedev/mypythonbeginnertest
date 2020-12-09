def gpa(gpa_dict):
	for key,val in gpa_dict.items():
		if grade=='A':
			return 5
		elif grade=='B':
		   return 4
		elif grade=='C':
		  return 3
		elif grade=='D':
		  return 2
	print({key})	
   
   
aggregate={}
while True:
	code=input('Enter your course code: ')
	grade=input('Enter grade :')
	aggregate[code]=grade
	another=input( 'Do you want to continue?y/n ')
	if another == 'y':
		continue
	else:
		break
gpa(aggregate)