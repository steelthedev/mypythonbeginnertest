from space.planet import Planet
from space.calc import planet_mass,planet_vol


naboo=Planet('naboo',90000,10.56,'Rao system')

naboo_mass=planet_mass(naboo.gravity,naboo.radius)
naboo_vol=planet_vol(naboo.radius)


print(f'{naboo.name} has a mass of{naboo_mass} and a volume of {naboo_vol}')