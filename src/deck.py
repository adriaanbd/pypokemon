from enum import Enum


class PokemonType(Enum):
	COLORLESS = "Colorless"
	DARKNESS = 'Darkness'
	DRAGON = 'Dragon'
	FAIRY = 'Fairy'
	FIGHTING = 'Fighting'
	FIRE = 'Fire'
	GRASS = 'Grass'
	LIGHTNING = 'Lightning'
	METAL = 'Metal'
	PSYCHIC = 'Psychic'
	WATER = 'Water'


class Card:
	def __init__(self, pokemon=False, energy=False, trainer=False, kind=1):
		self.type = PokemonType.COLORLESS
		self.kind = kind
		self.pokemon = pokemon
		self.energy = energy
		self.trainer = trainer


def create_list_of_cards(num, pokemon=False, energy=False, trainer=False, kind=1):
	return [Card(pokemon=pokemon, energy=energy, trainer=trainer, kind=kind) for _ in range(num)]


class Deck:
	def __init__(self):
		self.cards = (
			create_list_of_cards(16, pokemon=True) +
			create_list_of_cards(10, energy=True) +
			create_list_of_cards(4, trainer=True, kind=1) +
			create_list_of_cards(4, trainer=True, kind=2) +
			create_list_of_cards(4, trainer=True, kind=3) +
			create_list_of_cards(4, trainer=True, kind=4) +
			create_list_of_cards(4, trainer=True, kind=5) +
			create_list_of_cards(4, trainer=True, kind=6) +
			create_list_of_cards(4, trainer=True, kind=7) +
			create_list_of_cards(4, trainer=True, kind=8) +
			create_list_of_cards(2, trainer=True, kind=9)
		)
