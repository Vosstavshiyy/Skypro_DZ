from .masks import get_mask_account, get_mask_card_number


def mask_account_card(arg: str) -> str:
    """
    Функция возврата маски номера карты и номера счета

    Пример 1:
    >>> mask_account_card('Visa Platinum 7000792289606361')
    'Visa Platinum 7000 79** **** 6361'

    Пример 2:
    >>> mask_account_card('Счет 73654108430135874305')
    'Счет **4305'
    """
    arr = arg.split()
    for i in range(len(arr)):
        if arr[i].isdigit() and len(arr[i]) <= 16:
            arr[i] = get_mask_card_number(arr[i])
        elif arr[i].isdigit() and len(arr[i]) > 16:
            arr[i] = get_mask_account(arr[i])
    return ' '.join(arr)
