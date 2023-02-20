from dataclasses import dataclass
from typing import List


@dataclass
class DeckDTO:
	cards: List[str]

	@classmethod
	def empty_deck(cls):
		return cls(list())


class Player:
	def __init__(self):
		self.deck = DeckDTO.empty_deck()

	def set_deck(self, deck: DeckDTO):
		assert isinstance(deck, DeckDTO)
		self.deck = deck


class Challenge:
	type = "solo"

	def __init__(self, challenger: Player, opponent: Player):
		self.challenger = challenger
		self.opponent = opponent

	def is_playable(self) -> bool:
		has_sixty_cards = len(self.challenger.deck.cards) == 60 and len(self.opponent.deck.cards)
		if not has_sixty_cards:
			return False
		return all([self.challenger.deck, self.opponent.deck])


def create_challenge(challenger: Player, opponent: Player):
	return Challenge(challenger, opponent)
