from example import get_weather

def test_get_weather():
    assert get_weather(22) == "Hot"