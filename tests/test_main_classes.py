from casino.main_classes import CardDeck
# "casino." allows the script to reference the files in the folder casino | relevant for pytest

def test_card_deck():
    deck = CardDeck()
    assert len(deck.cards) == 52
    pass

def test_draw_cards():
    deck = CardDeck(num_copies=1)
    card = deck.draw_cards()
    assert card == ["A"]