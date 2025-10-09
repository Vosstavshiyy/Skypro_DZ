def filter_by_state(args: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Функция фильтрации словарей по значению ключа "state" (По умолчанию "EXECUTED")

    Пример:
    >>> filter_by_state([{state: 'EXECUTED'},{state: 'CANCELED'}], state='CANCELED')
    "[{state: 'CANCELED'}]"
    """
    return [arg for arg in args if arg.get('state') == state]


def sort_by_date(args: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция сортировки по "date" (по умолчанию — убывание)

    Пример:
    >>> sort_by_date([{'date': '2020-03-01'}, {'date': '2019-04-02'}], reverse=False)
    "[{'date': '2019-04-02'}, {'date': '2020-03-01'}]"
    """
    return sorted(args, key=lambda x: x['date'], reverse=reverse)
