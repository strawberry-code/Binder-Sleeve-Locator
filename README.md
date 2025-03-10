# Binder Sleeve Locator

This Python function calculates the page, side, and sleeve number within the side in a binder with 18 sleeves per page.

## Usage

```python
def find_sleeve(sleeve_number):
  # ... (function code)
```

# Example usage
```
sleeve_number = 43
page, side, sleeve_number_on_side = find_sleeve(sleeve_number)
print(f"Card number {sleeve_number} is on page {page}, side {side}, number {sleeve_number_on_side}.")
```

Let's say you have the Pokémon card "Toxtricity Expansion OBF(IT)" which is card number 072/197. To find its location in your binder, you can use the find_sleeve function:
```Python

from binder_utils import find_sleeve

sleeve_number = 72
page, side, sleeve_number_on_side = find_sleeve(sleeve_number)
print(f"Toxtricity is on page {page}, side {side}, number {sleeve_number_on_side}.")
```

This will output:
```
Toxtricity is on page 4, side back, number 9.
``` 

So, the Toxtricity card is located on page 4, on the back side, in the 9th sleeve.
