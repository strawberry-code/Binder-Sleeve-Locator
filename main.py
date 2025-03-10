from binder_utils import find_sleeve

if __name__ == "__main__":
    # Example usage
    sleeve_number = 43
    page, side, sleeve_number_on_side = find_sleeve(sleeve_number)
    print(f"Card number {sleeve_number} is on page {page}, side {side}, number {sleeve_number_on_side}.")

    sleeve_number = 18
    page, side, sleeve_number_on_side = find_sleeve(sleeve_number)
    print(f"Card number {sleeve_number} is on page {page}, side {side}, number {sleeve_number_on_side}.")

    sleeve_number = 19
    page, side, sleeve_number_on_side = find_sleeve(sleeve_number)
    print(f"Card number {sleeve_number} is on page {page}, side {side}, number {sleeve_number_on_side}.")