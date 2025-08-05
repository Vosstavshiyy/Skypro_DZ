"""
Пакет для работы с маскировкой данных.

Функции:
- get_mask_card_number: Маскировка номера карты
- get_mask_account: Маскировка номера счета
"""

from .masks import get_mask_account, get_mask_card_number

__all__ = ["get_mask_card_number", "get_mask_account"]
__version__ = "1.0.0"
author = "Vosstavshiy"
