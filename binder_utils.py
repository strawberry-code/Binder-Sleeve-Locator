def find_sleeve(sleeve_number):
    """
    Calculates the page, side, and sleeve number within the side in a binder.

    Args:
      sleeve_number: The sleeve number to find.

    Returns:
      A tuple containing the page number, side ("front" or "back"),
      and sleeve number on the side (from 1 to 9).
    """

    sleeves_per_page = 18
    page = (sleeve_number + sleeves_per_page - 1) // sleeves_per_page
    remainder = sleeve_number % sleeves_per_page

    if remainder == 0:
        remainder = 18

    side = "front" if remainder <= 9 else "back"
    sleeve_number_on_side = remainder if remainder <= 9 else remainder - 9

    return page, side, sleeve_number_on_side