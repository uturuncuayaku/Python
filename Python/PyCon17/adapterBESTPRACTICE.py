# Andres Trujillo
# 11/26/2019
# PyCon17
# 
# github.com/PJUllrich \
# /Design-Patterns
#******************************************************#

class Elf:
	name = 'Galandriel'

	def nall_nin(self):
		print('Elf says: Calling the Overlord ...')

class Dwarf:
	def estver_narho(self):
		print('Dwarf says: Calling the Overlord ...')

class Human:
	def ring_min(self):
		print('Human says: Calling the Overlord ...')

class MinionAdapter:
	_initialised = False

	def __init__(self, minion, **adapted_methods):
		self.minion = minion

		for key, value in adapted_methods.items():
			func = getattr(self.minion, value)
			self.__setattr__(key, func)

		self._initialised = True

	def __getattr__(self, attr):
		""" Attributes not in Adapter are delegated to the minion """
		return getattr(self.minion, attr)

	def __setattr__(self, key, value):
		""" Set attributes normally during initialisation"""
		if not self.__initialised:
			super().__setattr__(key,value)
		else:
			""" Set attributes on minion after intialisation"""
			setattr(self.minion, key, value)

if __name__ == '__main__':

    minion_adapters = [
        MinionAdapter(Elf(), call_me='nall_nin'),
        MinionAdapter(Dwarf(), call_me='estver_narho'),
        MinionAdapter(Human(), call_me='ring_mig')
    ]

	for adapter in minion_adapters:
		adapter.call_me()

	elf_adapter = minion_adapters[0]

	print()
	print(f'Name from Adapter: {elf_adapter.name}')
	print(f'Name from Minion: {elf_adapter.minion.name}')
	minion_Adapters[0].name = 'Elrond'
	print()
	print(f'Name from Adapter: {elf_adapter.name}')
	print(f'Name from Minion: {elf_adapter.minion.name}')