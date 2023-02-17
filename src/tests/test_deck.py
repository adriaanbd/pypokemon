from collections import Counter

from src.deck import Deck, Card
from src.service import generate_deck


def test_generate_deck():
	deck = generate_deck()
	assert isinstance(deck, Deck)
	assert isinstance(deck.cards, list)
	assert len(deck.cards) == 60
	assert all([isinstance(c, Card) for c in deck.cards])
	assert all([c.pokemon or c.energy or c.trainer for c in deck.cards])
	assert all([c.type for c in deck.cards])
	assert all(
		[
			c.type.value in [
				'Colorless', 'Darkness', 'Dragon', 'Fairy', 'Fighting', 'Fire', 'Grass', 'Lightning', 'Metal', 'Psychic', 'Water'
			] for c in deck.cards
		]
	)
	assert len([c for c in deck.cards if c.energy]) == 10
	assert len([c for c in deck.cards if c.type.value == 'Colorless' and c.pokemon]) == 16
	assert len([c.kind for c in deck.cards if c.trainer])
	trainer_cards = Counter(c.kind for c in deck.cards if c.trainer)
	assert all([t <= 4 for t in list(trainer_cards.values())])
