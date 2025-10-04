def get_mask_card_number(arg: int) -> str:
    """
    Функция возврата маски номера карты

    Пример:
    >>> get_mask_card_number(7000792289606361)
    '7000 79** **** 6361'
    """
    mask = str(arg)
    if len(mask) != 16:  # Проверка длины
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{mask[0:4]} {mask[4:6]}** **** {mask[-4::]}"


def get_mask_account(arg: int) -> str:
    """
    Функция возврата маски номера счета

    Пример:
    >>> get_mask_account(73654108430135874305)
    '**4305'
    """
    mask = str(arg)
    return f"**{mask[-4::]}"

def foo():
    pass
