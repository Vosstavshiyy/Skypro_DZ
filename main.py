from src.masks import get_mask_account, get_mask_card_number


def main() -> None:
    print("Маскировка карты:", get_mask_card_number(7000792289606361))
    print("Маскировка счета:", get_mask_account(73654108430135874305))


if __name__ == "__main__":
    main()
