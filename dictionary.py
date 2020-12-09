def ninja_intro(dictionary):
	for key,val in dictionary.items():
		print(f"i am {key} and i am {val} belt master ")

ninja_belts={}

while True:
	ninja_name=input('enter a ninja name:')
	ninja_belt=input('enter your ninja belt:')
	ninja_belts[ninja_name]=ninja_belt
	another=input('Add another? y/n')
	if another =='y':
		continue
	else:
		break
ninja_intro(ninja_belts)
	
	