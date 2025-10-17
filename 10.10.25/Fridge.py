from decimal import Decimal
import datetime

goods = {}


def add(product_name: str):
    """Добавляет новый продукт в холодильник (ключ в словарь)."""
    if product_name in goods:
        print("Такой продукт уже хранится в холодильнике")
    else:
        goods[product_name] = []


def add_by_note(product_name: str, amount, expiration_date: str):
    """Добавляет партию продукта с количеством и сроком годности."""
    # Если продукта нет — добавляем его (без сообщения)
    if product_name not in goods:
        goods[product_name] = []

    # Преобразуем количество и дату
    amount_decimal = Decimal(str(amount))
    date_obj = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()

    # Добавляем новую партию
    goods[product_name].append({
        "amount": amount_decimal,
        "expiration_date": date_obj
    })


def find(word: str):
    """Ищет продукты по подстроке (без учёта регистра) и печатает результат."""
    word = word.strip().lower()
    found = [name for name in goods if word in name.lower()]
    if not found:
        print(f"По запросу '{word}' ничего не найдено.")
    else:
        print("Найдено:")
        for name in found:
            print("  -", name)
    return found



def amount(product_name: str):
    """Возвращает суммарное количество продукта."""
    if product_name not in goods:
        print(f"Продукт '{product_name}' не найден в холодильнике.")
        return

    total = sum(batch['amount'] for batch in goods[product_name])
    print(f"Общее количество '{product_name}': {total}")


def show_fridge():
    """Красиво отображает содержимое холодильника."""
    if not goods:
        print("Холодильник пуст 😢")
        return

    for product, batches in goods.items():
        print(f"\n{product}:")
        for i, batch in enumerate(batches, start=1):
            print(f"    Поставка {i}:")
            print(f"        Количество: {batch['amount']}")
            print(f"        Годен до: {batch['expiration_date']}")
    print()  # пустая строка в конце для красоты



while 1:
    a = ''
    b = ''
    c = None
    action = None
    print()
    print('Выберите действие: \n4. Узнать количество продукта в холодильнике.\n3. Поиск продуктов по ключевому слову.\n2. Добавить в холодильник продукт с описанием.\n'
          '1. Добавить в холодильник продукт.\n0. Закончить и показать содержимое холодильника.')
    print()
    action = input()
    if action == '0':
        show_fridge()
        break
    elif action == '1':
        add(input('Введите название продукта: '))
    elif action == '2':
        add_by_note(input('Введите название продукта: '),float(input('Введите количество продукта: ')),input('Введите срок годности (YYYY-MM-DD) продукта: '))
    elif action == '3':
        find(input('Введите ключевые слова для поиска: '))
    elif action == '4':
        amount(input('Введите название продукта для поиска его количества: '))
