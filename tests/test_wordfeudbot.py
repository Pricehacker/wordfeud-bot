import wordfeudbot.main as wfbot


def test_is_emoji():
    assert wfbot.is_emoji('😁')
    assert wfbot.is_emoji('😂')
    assert wfbot.is_emoji('🤣')
    assert wfbot.is_emoji('😃')
    assert wfbot.is_emoji('😄')
    assert wfbot.is_emoji('👩')
    assert wfbot.is_emoji('👨')
    assert wfbot.is_emoji('🧑🏿')
    assert wfbot.is_emoji('🎈')
    assert wfbot.is_emoji('🎆')
    assert wfbot.is_emoji('🍋')
    assert wfbot.is_emoji('🛹')
    assert wfbot.is_emoji('⚡')
    assert wfbot.is_emoji('💟')
    assert wfbot.is_emoji('⏪')
    assert wfbot.is_emoji('🕕')