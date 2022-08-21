import enum


class CategoriesEnums(enum.Enum):
    DEFAULT = 0
    FIX = 1
    ANY = 2
    GIRLS = 3

    labels = {
        DEFAULT: "Не выбрано",
        FIX: 'Фиксированный ковбои брейклесс 🚲',
        ANY: 'Любой тормозной ковбой 🚴',
        GIRLS: 'Cowgirls',
    }


STARTUP_MESSAGE_FOR_ADMINS = """
И так, мы в продакшене. Бот стартанул.\n\nАдминка доступна на 127.0.0.1:8000/admin
"""


R = 0.0015  # Зона действия вокруг точки - 150 метров, R == 300
