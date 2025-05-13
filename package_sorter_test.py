from package_enums import package_enums
from package_sorter import sort

#Standard
def test_standard_package():
    assert sort(50, 50, 50, 10) == package_enums.STANDARD

def test_standard_length_edge():
    assert sort(50, 149, 50, 10) == package_enums.STANDARD

def test_standard_height_edge():
    assert sort(50, 50, 149, 10) == package_enums.STANDARD

def test_standard_width_edge():
    assert sort(149, 50, 50, 10) == package_enums.STANDARD


# Basic Specials
def test_bulky_only():
    assert sort(100, 100, 100, 10) == package_enums.SPECIAL

def test_heavy_only():
    assert sort(50, 50, 50, 25) == package_enums.SPECIAL


# Dimension Specials
def test_bulky_by_dimension_width():
    assert sort(151, 50, 50, 10) == package_enums.SPECIAL

def test_bulky_by_dimension_length():
    assert sort(50, 151, 50, 10) == package_enums.SPECIAL

def test_bulky_by_dimension_height():
    assert sort(50, 50, 151, 10) == package_enums.SPECIAL

def test_bulky_by_dimension_length_exact():
    assert sort(50, 150, 50, 10) == package_enums.SPECIAL

def test_bulky_by_dimension_height_exact():
    assert sort(50, 50, 150, 10) == package_enums.SPECIAL

def test_bulky_by_dimension_width_exact():
    assert sort(150, 50, 50, 10) == package_enums.SPECIAL

def test_edge_case_exactly_20_kg():
    assert sort(50, 50, 50, 20) == package_enums.SPECIAL

def test_rejected_both_bulky_and_heavy():
    assert sort(200, 200, 200, 25) == package_enums.REJECTED 