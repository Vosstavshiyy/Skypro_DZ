from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date


test_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
             ]


def main() -> None:
    print(f"Маскировка карты: {mask_account_card('Visa Platinum 7000792289606361')} \nМаскировка счета: {mask_account_card('Счет 73654108430135874305')}\n")
    print(f"Вывод даты: {get_date('2024-03-11T02:26:18.671407')}\n")
    print(f"Фильтрация по 'EXECUTED': {filter_by_state(test_data)} \nФильтрация по 'CANCELED': {filter_by_state(test_data, state='CANCELED')}\n")
    print(f"Сортировка по дате (убывание): {sort_by_date(test_data)} \nСортировка по времени (восрастание): {sort_by_date(test_data, reverse=False)}\n")


if __name__ == "__main__":
    main()
