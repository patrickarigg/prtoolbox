from prtoolbox.weather import weather_at_lewagon

def test_weather_at_lewagon():
    assert 'weather' in weather_at_lewagon()
