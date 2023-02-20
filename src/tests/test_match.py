from src.deck import Deck, from_deck_to_deck_dto
from src.match import create_challenge, Challenge, Player, DeckDTO


def test_solo_challenge():
	challenger = opponent = Player()
	challenge = create_challenge(challenger, opponent)
	assert isinstance(challenge, Challenge)
	assert challenge.type == "solo"
	assert challenge.is_playable() is False

	assert challenger.set_deck(DeckDTO.empty_deck()) is None
	assert challenge.is_playable() is False

	deck_dto = from_deck_to_deck_dto(Deck())
	assert challenger.set_deck(deck_dto) is None
	assert challenge.is_playable() is True
