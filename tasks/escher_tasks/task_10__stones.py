from functools import lru_cache


def stones_recursion(pile, moves):

    @lru_cache
    def win(pile):
        return any(not win(pile - m) for m in moves if pile > m)

    return 1 if win(pile) else 2


def stones_queue(pile, moves):

    all_results = {}                                            # Будемо зберігати усі результати розрахунків
    queue = [pile]                                              # Черга з усіма підзадачами, які треба розрахувати

    while queue:
        _pile = queue.pop(0)                                    # Обхід дерева - DFS
        new_piles = {_pile - m for m in moves if _pile > m}     # Усі можливі ходи гравця
        missing_results = new_piles - all_results.keys()        # Чи є попередньо розраховані результати
        if missing_results:                                     # Не усі результати були розраховані
            queue = sorted(missing_results) + [_pile] + queue   # Додамо до черги усі елементи які потрібно розрахувати
            continue                                            # Починаємо розрахунок спочатку для найменшого елементу

        # Усі попередні значення розраховані,
        # тож ми можемо розрахувати результат для поточного значення
        all_results[_pile] = any(not all_results[p] for p in new_piles)

    return 1 if all_results[pile] else 2


def stones_dynamic(pile, moves):

    all_results = {}

    for _pile in range(1, pile + 1):
        all_results[_pile] = any(not all_results[_pile - m]
                                 for m in moves if _pile > m)

    return 1 if all_results[pile] else 2
