
birthdays={'Funke': 'may 27', 'aanu':'jan 3rd', 'iyanu': 'march 26'}

while True:
	print('Enter a name:(Blank to quit)')
	name=input()
	if name =='':
		break
	if name in birthdays:
		print(birthdays[name] + ' is the birthday of ' + name)
	else:
		print('I do not have birthday information for ' + name)
		print('Good news , you can add their birthday. what is their date?')
		bday=input()
		birthdays[name]=bday
		print('Birthday Database successfully updated')

