from package_enums import package_enums

def sort(width: int, height: int, length: int, mass: int) -> package_enums:
    """
    Classify a package based on its dimensions and mass.

    A package is categorized into one of three types:
    - STANDARD: if it is neither bulky nor heavy
    - SPECIAL: if it is bulky or heavy, but not both
    - REJECTED: if it is both bulky and heavy

    A package is considered:
    - Bulky if its volume (width × height × length) >= 1,000,000 cm³
      or any single dimension >= 150 cm
    - Heavy if its mass >= 20 kg

    Args:
        width (int): Width of the package in centimeters.
        height (int): Height of the package in centimeters.
        length (int): Length of the package in centimeters.
        mass (int): Mass of the package in kilograms.

    Returns:
        package_enums: The classification of the package (STANDARD, SPECIAL, REJECTED).
    """
    volume = width * height * length
    is_bulky = (volume >= 1000000) or (width >= 150 or height >= 150 or length >= 150)
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return package_enums.REJECTED
    elif is_bulky or is_heavy:
        return package_enums.SPECIAL
    else:
        return package_enums.STANDARD