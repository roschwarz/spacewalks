import pytest
import eva_data_analaysis as eva


def test_text_to_duration_float():
	"""
    Test that text_to_duration returns expected ground truth values
    for typical durations with a non-zero minute component
    """
	assert eva.text_to_duration('10:20') == pytest.approx(10.33333)

def test_text_to_duration_integer():
	"""
    Test that text_to_duration returns expected ground truth values
    for typical whole hour durations 
    """	
	assert eva.text_to_duration("10:00") == 10



@pytest.mark.parametrize("input_value, expected_result", [
    ("Valentina Tereshkova;", 1),
    ("Judith Resnik; Sally Ride;", 2),
	("Judith Resnik; Sally Ride; Hello Name;", 3)
])
def test_calculate_crew_size(input_value, expected_result):
    """
    Test that calculate_crew_size returns expected ground truth values
    for typical crew values
    """
    actual_result = eva.calculate_crew_size(input_value)
    assert actual_result == expected_result