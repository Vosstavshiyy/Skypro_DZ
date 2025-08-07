#from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card


def main() -> None:
    print("Маскировка карты:", mask_account_card('Visa Platinum 7000792289606361'))
    print("Маскировка счета:", mask_account_card('Счет 73654108430135874305'))


if __name__ == "__main__":
    main()
