class Planet:
	def __init__(self,name,radius,gravity,system):
		self.name=name
		self.radius=radius
		self.gravity=gravity
		self.system=system
		
krypton = Planet('krypton',90000,10.56,'Rao system')
print(f'The name of my planet is :{krypton.name}')
print(f'it has a radius of {krypton.radius}')
