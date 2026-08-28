import logging
import os
import time

import requests
import urllib3


# ============================================================
# НАСТРОЙКИ
# ============================================================

BASE_URL = "https://platform-api2.max.ru"
TOKEN_FILE = "bot_token.txt"

POLL_TIMEOUT = 30
RETRY_DELAY = 5


# ============================================================
# SSL
# ============================================================

urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)

session = requests.Session()
session.verify = False


# ============================================================
# ЛОГИ
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)


# ============================================================
# ТОКЕН
# ============================================================

def load_token():

    if not os.path.exists(TOKEN_FILE):
        raise FileNotFoundError(
            f"Файл {TOKEN_FILE} не найден."
        )

    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        token = f.read().strip()

    if not token:
        raise ValueError(
            "Файл bot_token.txt пустой."
        )

    return token


TOKEN = load_token()

HEADERS = {
    "Authorization": TOKEN,
    "Content-Type": "application/json",
}


# ============================================================
# FAQ
# ============================================================

FAQ = {

    # ============ ГОРНЫЙ ФАКУЛЬТЕТ ============
    "mining": {
        "title": "⛰️ Горный факультет",
        "questions": {

            "about": {
                "title": "ℹ️ О факультете",
                "answer": (
                    "Горный факультет (Горная академия) — один из старейших "
                    "факультетов ЗабГУ. Основан в 1966 году.\n\n"
                    "Готовит специалистов для горнодобывающей отрасли: геологов, "
                    "маркшейдеров, горных инженеров, обогатителей.\n\n"
                    "Подробнее: https://vk.ru/wall-106344971_3572"
                )
            },

            "address": {
                "title": "📍 Адрес и корпус",
                "answer": (
                    "📍 Корпус №9\n"
                    "г. Чита, ул. Кастринская, д. 1, к2\n\n"
                    "📞 Телефон: 8(3022) 26-02-40"
                )
            },

            "directions": {
                "title": "🎓 Направления подготовки",
                "answer": (
                    "• Прикладная геология\n"
                    "• Технология геологической разведки\n"
                    "• Горное дело (профили: обогащение, подземная разработка, "
                    "открытые работы, маркшейдерское дело)\n\n"
                    "Подробно: https://entrant.zabgu.ru/wp-content/themes/twentytwelve/page-templates/tilda-main-template/spec-select?step=bachelor"
                )
            },

            "inside": {
                "title": "🏢 Что внутри?",
                "answer": (
                    "• Обновлённые холлы и аудитории\n"
                    "• Столовая с вкусной и недорогой едой\n"
                    "• Интерактивный музейный комплекс\n"
                    "• Современные лаборатории\n"
                    "• Коворкинг-зоны на каждом этаже"
                )
            },
        }
    },

    # ============ ЭНЕРГЕТИЧЕСКИЙ ФАКУЛЬТЕТ ============
    "energy": {
        "title": "⚡ Энергетический факультет",
        "questions": {

            "about": {
                "title": "ℹ️ О факультете",
                "answer": (
                    "Энергетический факультет готовит специалистов в области "
                    "теплоэнергетики, электроэнергетики, электромеханики.\n\n"
                    "Кафедры: энергетики, физики и техники связи, химии, "
                    "математики и черчения.\n\n"
                    "Подробнее: https://vk.ru/wall-106344971_3574"
                )
            },

            "address": {
                "title": "📍 Адрес и корпус",
                "answer": (
                    "📍 Корпус №03\n"
                    "г. Чита, ул. Баргузинская, 49\n\n"
                    "📞 Телефон: 8(3022) 41-73-13"
                )
            },

            "directions": {
                "title": "🎓 Направления подготовки",
                "answer": (
                    "• Тепловые электрические станции\n"
                    "• Электроснабжение\n"
                    "• Электромеханика\n"
                    "• Электроэнергетические сети и системы\n"
                    "• Программное обеспечение вычислительной техники\n"
                    "• Прикладная информатика\n"
                    "• Химия\n\n"
                    "Подробно: https://entrant.zabgu.ru/wp-content/themes/twentytwelve/page-templates/tilda-main-template/spec-select?step=bachelor"
                )
            },
        }
    },

    # ============ ФКНИТ ============
    "fknit": {
        "title": "💻 ФКНИТ",
        "questions": {

            "about": {
                "title": "ℹ️ О факультете",
                "answer": (
                    "Факультет компьютерных наук и телекоммуникаций (ФКНИТ) "
                    "готовит IT-специалистов и связистов.\n\n"
                    "Кафедры: информатики и вычислительной техники, прикладной "
                    "информатики, физики и техники связи.\n\n"
                    "Подробнее: https://vk.ru/wall-106344971_3574"
                )
            },

            "address": {
                "title": "📍 Адрес и корпус",
                "answer": (
                    "📍 Корпус уточняется. Занятия могут проходить в разных корпусах.\n"
                    "Актуальную информацию смотрите на сайте ЗабГУ.\n"
                    "📞 Телефон уточняется."
                )
            },

            "directions": {
                "title": "🎓 Направления подготовки",
                "answer": (
                    "• Информатика и вычислительная техника\n"
                    "• Прикладная информатика\n"
                    "• Телекоммуникации\n\n"
                    "Подробно: https://entrant.zabgu.ru/wp-content/themes/twentytwelve/page-templates/tilda-main-template/spec-select?step=bachelor"
                )
            },
        }
    },

    # ============ УЧЁБА ============
    "study": {
        "title": "📚 Учёба",
        "questions": {

            "process": {
                "title": "📖 Учебный процесс",
                "answer": (
                    "📖 Учебный процесс включает лекции, практические и "
                    "лабораторные занятия, самостоятельную работу.\n\n"
                    "Учебный год начинается 1 сентября и заканчивается "
                    "согласно учебному плану."
                )
            },

            "missed": {
                "title": "❓ Пропуск занятий",
                "answer": (
                    "❗ Если пропустил занятие, уточни у преподавателя, "
                    "что необходимо отработать.\n\n"
                    "При длительном отсутствии по уважительной причине "
                    "обратись в деканат."
                )
            },

            "exam": {
                "title": "📝 Зачёт и экзамен",
                "answer": (
                    "📝 Зачёт и экзамен — формы промежуточной аттестации.\n\n"
                    "Форма контроля зависит от дисциплины."
                )
            },

            "deanery": {
                "title": "🏢 Вопросы к деканату",
                "answer": (
                    "🏢 По всем вопросам обращайтесь в свой деканат.\n"
                    "Контакты деканатов уточняйте на сайте ЗабГУ."
                )
            },
        }
    },

    # ============ РАСПИСАНИЕ ============
    "schedule": {
        "title": "📅 Расписание",
        "questions": {

            "where": {
                "title": "📅 Где смотреть расписание?",
                "answer": (
                    "📅 Расписание доступно в информационной системе ЗабГУ.\n"
                    "Всегда проверяйте свою группу."
                )
            },

            "group": {
                "title": "🔎 Как найти свою группу?",
                "answer": (
                    "🔎 Используйте полное обозначение группы.\n"
                    "Если не получается, обратитесь в деканат."
                )
            },

            "classroom": {
                "title": "🏢 Как узнать аудиторию?",
                "answer": (
                    "🏢 Аудитория указана в расписании.\n"
                    "При изменениях ориентируйтесь на последнюю версию."
                )
            },

            "changes": {
                "title": "🔄 Изменения в расписании",
                "answer": (
                    "🔄 Ориентируйтесь на последнюю опубликованную версию.\n"
                    "При сомнениях уточните у преподавателя или в деканате."
                )
            },
        }
    },

    # ============ ОБЩЕЖИТИЕ ============
    "hostel": {
        "title": "🏠 Общежитие",
        "questions": {

            "general": {
                "title": "🏠 Заселение в общежитие",
                "answer": (
                    "🏠 Заселение первокурсников — 29 августа.\n\n"
                    "Порядок действий:\n"
                    "1. Приезжайте в штаб на Бабушкина, 129 (1 этаж).\n"
                    "2. Оформите документы.\n"
                    "3. Администратор встретит вас в общежитии.\n\n"
                    "Необходимые документы: паспорт, справка о педикулёзе (10 дней), "
                    "флюорография (1 год), 3 фото 3×4, квитанция об оплате за 2 месяца.\n\n"
                    "Для несовершеннолетних — нотариальное согласие родителя на проживание "
                    "и отдельное согласие на самостоятельный выход."
                )
            },

            "documents": {
                "title": "📄 Документы для заселения",
                "answer": (
                    "• паспорт\n"
                    "• справка об отсутствии педикулёза (срок 10 дней)\n"
                    "• флюорография (срок 1 год)\n"
                    "• 3 фото 3×4\n"
                    "• квитанция об оплате за 2 месяца"
                )
            },

            "rules": {
                "title": "📋 Правила проживания",
                "answer": (
                    "• Соблюдать внутренний распорядок\n"
                    "• Своевременно вносить плату\n"
                    "• Бережно относиться к имуществу\n"
                    "• Предъявлять студенческий билет или паспорт при входе\n"
                    "• Гости — с 14:00 до 17:00"
                )
            },

            "problem": {
                "title": "🆘 Проблемы с общежитием",
                "answer": (
                    "Обращайтесь в подразделение по общежитиям или в деканат."
                )
            },
        }
    },

    # ============ СТИПЕНДИЯ ============
    "scholarship": {
        "title": "💰 Стипендия",
        "questions": {

            "general": {
                "title": "💰 Виды и условия",
                "answer": (
                    "• Академическая — по итогам аттестации\n"
                    "• Социальная — для льготных категорий\n"
                    "• Именные — за особые успехи\n\n"
                    "Назначается не реже 2 раз в год."
                )
            },

            "amount": {
                "title": "💵 Размер стипендии",
                "answer": (
                    "Базовая академическая:\n"
                    "• 1 608 ₽ — минимальная\n"
                    "• 3 000 ₽ — на «хорошо»\n"
                    "• 3 600 ₽ — на «хорошо» и «отлично»\n"
                    "• 4 200 ₽ — все «отлично» (1 семестр)\n"
                    "• 5 400 ₽ — все «отлично» (4 семестра)\n\n"
                    "Повышенная (по баллам ЕГЭ): от 7 200 до 28 800 ₽\n"
                    "Именные — до 8 400 ₽"
                )
            },
        }
    },

    # ============ ДОКУМЕНТЫ ============
    "documents": {
        "title": "📄 Документы",
        "questions": {

            "student_id": {
                "title": "🪪 Студенческий билет",
                "answer": (
                    "Обратитесь в подразделение по оформлению документов."
                )
            },

            "gradebook": {
                "title": "📘 Зачётная книжка",
                "answer": (
                    "Обращайтесь в деканат."
                )
            },

            "certificates": {
                "title": "📑 Заказ справок",
                "answer": (
                    "Форма заказа справок:\n"
                    "https://docs.google.com/forms/d/e/1FAIpQLSekxx7nV7fWLyARJBSpG7YCRSqzJv6TXN7qoc2N-IROIiAIpQ/viewform?usp=dialog"
                )
            },
        }
    },

    # ============ ПРАКТИКА ============
    "practice": {
        "title": "⛏️ Практика",
        "questions": {

            "general": {
                "title": "⛏️ Прохождение практики",
                "answer": (
                    "Студенты проходят практику на предприятиях:\n"
                    "• Норильский никель\n"
                    "• Хиагда\n"
                    "• Приаргунское ПГХО"
                )
            },

            "documents": {
                "title": "📄 Документы для практики",
                "answer": (
                    "Список документов уточняйте у руководителя практики."
                )
            },
        }
    },

    # ============ БИБЛИОТЕКА ============
    "library": {
        "title": "📖 Библиотека",
        "questions": {

            "where": {
                "title": "📖 Как получить литературу?",
                "answer": (
                    "Научная библиотека ЗабГУ:\n"
                    "http://zabgu.ru/php/index_library.php\n"
                    "chitantb@mail.ru\n\n"
                    "Для удалённой регистрации отправьте письмо с ФИО, датой рождения, "
                    "факультетом, группой, телефоном и адресом."
                )
            },

            "access": {
                "title": "🔐 Доступ к электронным ресурсам",
                "answer": (
                    "Доступ к ЭБС:\n"
                    "• Elibrary.ru\n"
                    "• Юрайт\n"
                    "• Лань\n"
                    "• Консультант студента\n\n"
                    "Для доступа отправьте письмо на chitantb@mail.ru."
                )
            },
        }
    },

    # ============ КАНАЛ В MAX ============
    "max_channel": {
        "title": "📲 Канал в MAX",
        "questions": {

            "join": {
                "title": "📲 Присоединиться",
                "answer": (
                    "Ссылка: https://max.ru/join/HLbC3v2ooq0KyeIHZdI1ikOrmR7KfeEutP9m1IXn4jo"
                )
            },
        }
    },

    # ============ КОНТАКТЫ ============
    "contacts": {
        "title": "📞 Контакты",
        "questions": {

            "site": {
                "title": "🌐 Официальный сайт",
                "answer": "https://zabgu.ru/php/index.php"
            },

            "faculty_contacts": {
                "title": "📞 Контакты факультетов",
                "answer": (
                    "Горный: ул. Кастринская, 1, к2, тел. 8(3022) 26-02-40\n"
                    "Энерго: ул. Баргузинская, 49, тел. 8(3022) 41-73-13\n"
                    "ФКНИТ: контакты уточняйте на сайте."
                )
            },

            "student_office": {
                "title": "🏢 Студенческий офис",
                "answer": (
                    "Информация уточняется.\n"
                    "Общие контакты: mail@zabgu.ru, 8(3022) 41-64-44"
                )
            },
        }
    }
}


# ============================================================
# КЛАВИАТУРА
# ============================================================

def callback_button(text, payload):

    return {
        "type": "callback",
        "text": text,
        "payload": payload
    }


def make_keyboard(buttons, columns=2):

    rows = []

    for i in range(0, len(buttons), columns):
        rows.append(
            buttons[i:i + columns]
        )

    return rows


def keyboard_attachment(buttons):

    return {
        "type": "inline_keyboard",
        "payload": {
            "buttons": buttons
        }
    }


# ============================================================
# ГЛАВНОЕ МЕНЮ
# ============================================================

def main_menu_keyboard():

    buttons = []

    for section_id, section in FAQ.items():

        buttons.append(
            callback_button(
                section["title"],
                f"section:{section_id}"
            )
        )

    return [
        keyboard_attachment(
            make_keyboard(
                buttons,
                columns=2
            )
        )
    ]


def main_menu_text():

    return (
        "🎓 ГОРНАЯ АКАДЕМИЯ ЗАБГУ\n\n"
        "Добро пожаловать!\n\n"
        "Выбери нужный раздел:"
    )


# ============================================================
# МЕНЮ РАЗДЕЛА
# ============================================================

def section_keyboard(section_id):

    section = FAQ[section_id]

    buttons = []

    for question_id, question in section["questions"].items():

        buttons.append(
            callback_button(
                question["title"],
                f"question:{section_id}:{question_id}"
            )
        )

    buttons.append(
        callback_button(
            "🏠 Главное меню",
            "main"
        )
    )

    return [
        keyboard_attachment(
            make_keyboard(
                buttons,
                columns=1
            )
        )
    ]


def section_text(section_id):

    return (
        f"{FAQ[section_id]['title']}\n\n"
        "Выбери нужный вопрос:"
    )


# ============================================================
# КНОПКИ ПОСЛЕ ОТВЕТА
# ============================================================

def question_keyboard(section_id):

    buttons = [
        [
            callback_button(
                "◀️ Назад",
                f"section:{section_id}"
            ),
            callback_button(
                "🏠 Главное меню",
                "main"
            )
        ]
    ]

    return [
        keyboard_attachment(buttons)
    ]


# ============================================================
# ОТПРАВКА СООБЩЕНИЯ
# ============================================================

def send_message(user_id, text, attachments=None):

    url = f"{BASE_URL}/messages"

    params = {
        "user_id": user_id
    }

    payload = {
        "text": text
    }

    if attachments is not None:
        payload["attachments"] = attachments

    response = session.post(
        url,
        params=params,
        headers=HEADERS,
        json=payload,
        timeout=30
    )

    logging.info(
        "POST /messages -> %s",
        response.status_code
    )

    if not response.ok:
        logging.error(
            "Ответ MAX: %s",
            response.text
        )

    response.raise_for_status()

    return response.json()


# ============================================================
# ОТВЕТ НА CALLBACK
# ============================================================

def answer_callback(callback_id, text, attachments=None):

    url = f"{BASE_URL}/answers"

    params = {
        "callback_id": callback_id
    }

    message = {
        "text": text
    }

    if attachments is not None:
        message["attachments"] = attachments

    payload = {
        "message": message
    }

    response = session.post(
        url,
        params=params,
        headers=HEADERS,
        json=payload,
        timeout=30
    )

    logging.info(
        "POST /answers -> %s",
        response.status_code
    )

    if not response.ok:
        logging.error(
            "Ответ MAX: %s",
            response.text
        )

    response.raise_for_status()

    return response.json()


# ============================================================
# LONG POLLING
# ============================================================

def get_updates(marker=None):

    url = f"{BASE_URL}/updates"

    params = {
        "timeout": POLL_TIMEOUT
    }

    if marker is not None:
        params["marker"] = marker

    response = session.get(
        url,
        params=params,
        headers=HEADERS,
        timeout=POLL_TIMEOUT + 10
    )

    response.raise_for_status()

    return response.json()


# ============================================================
# ОБРАБОТКА BOT_STARTED
# ============================================================

def handle_bot_started(update):

    user = update.get("user", {})

    user_id = user.get("user_id")

    if not user_id:
        logging.error(
            "bot_started получен, но user_id не найден: %s",
            update
        )
        return

    logging.info(
        "Новый пользователь запустил бота: %s",
        user_id
    )

    send_message(
        user_id,
        main_menu_text(),
        main_menu_keyboard()
    )


# ============================================================
# ОБРАБОТКА СООБЩЕНИЯ
# ============================================================

def handle_message(update):

    message = update.get("message", {})

    sender = message.get("sender", {})

    user_id = sender.get("user_id")

    body = message.get("body", {})

    text = body.get("text", "")

    logging.info(
        "message_created: user_id=%s text=%r",
        user_id,
        text
    )

    if not user_id:
        return

    if not text:
        return

    if text.lower().strip() in (
        "/start",
        "start",
        "начать",
        "меню",
        "главное меню"
    ):

        send_message(
            user_id,
            main_menu_text(),
            main_menu_keyboard()
        )

    else:

        send_message(
            user_id,
            (
                "👋 Выбери нужный раздел кнопками ниже.\n\n"
                "Ничего вводить не нужно."
            ),
            main_menu_keyboard()
        )


# ============================================================
# ОБРАБОТКА CALLBACK
# ============================================================

def handle_callback(update):

    callback = update.get("callback", {})

    callback_id = callback.get("callback_id")

    payload = callback.get("payload")

    logging.info(
        "message_callback: callback_id=%s payload=%r",
        callback_id,
        payload
    )

    if not callback_id:
        logging.error(
            "В callback отсутствует callback_id:\n%s",
            update
        )
        return

    if payload == "main":

        answer_callback(
            callback_id,
            main_menu_text(),
            main_menu_keyboard()
        )

        return

    # ----------------------------------------
    # РАЗДЕЛ
    # ----------------------------------------

    if isinstance(payload, str) and payload.startswith("section:"):

        section_id = payload.split(":", 1)[1]

        if section_id not in FAQ:

            answer_callback(
                callback_id,
                "❌ Такой раздел не найден.",
                main_menu_keyboard()
            )

            return

        answer_callback(
            callback_id,
            section_text(section_id),
            section_keyboard(section_id)
        )

        return

    # ----------------------------------------
    # ВОПРОС
    # ----------------------------------------

    if isinstance(payload, str) and payload.startswith("question:"):

        parts = payload.split(":")

        if len(parts) != 3:

            answer_callback(
                callback_id,
                "❌ Некорректная кнопка.",
                main_menu_keyboard()
            )

            return

        section_id = parts[1]
        question_id = parts[2]

        if section_id not in FAQ:

            answer_callback(
                callback_id,
                "❌ Раздел не найден.",
                main_menu_keyboard()
            )

            return

        questions = FAQ[section_id]["questions"]

        if question_id not in questions:

            answer_callback(
                callback_id,
                "❌ Вопрос не найден.",
                section_keyboard(section_id)
            )

            return

        question = questions[question_id]

        answer_callback(
            callback_id,
            question["answer"],
            question_keyboard(section_id)
        )

        return

    # ----------------------------------------
    # НЕИЗВЕСТНЫЙ CALLBACK
    # ----------------------------------------

    answer_callback(
        callback_id,
        "❌ Неизвестная команда.",
        main_menu_keyboard()
    )


# ============================================================
# ОБРАБОТКА UPDATE
# ============================================================

def process_update(update):

    update_type = update.get("update_type")

    logging.info(
        "Получено событие: %s",
        update_type
    )

    logging.debug(
        "FULL UPDATE: %s",
        update
    )

    if update_type == "bot_started":
        handle_bot_started(update)
        return

    if update_type == "message_created":
        handle_message(update)
        return

    if update_type == "message_callback":
        handle_callback(update)
        return

    logging.info(
        "Событие %s пока не используется.",
        update_type
    )


# ============================================================
# MAIN
# ============================================================

def main():

    logging.info("==========================================")
    logging.info("ГОРНАЯ АКАДЕМИЯ ЗАБГУ — FAQ БОТ")
    logging.info("==========================================")
    logging.info("Бот запускается...")
    logging.info("SSL-проверка отключена.")
    logging.info("Long Polling включён.")
    logging.info("Ожидание событий MAX...")

    marker = None

    while True:

        try:

            data = get_updates(marker)

            updates = data.get("updates", [])

            logging.info(
                "Получено обновлений: %d",
                len(updates)
            )

            for update in updates:

                try:

                    process_update(update)

                except Exception as error:

                    logging.exception(
                        "Ошибка обработки update: %s",
                        error
                    )

            if "marker" in data:

                marker = data["marker"]

        except requests.exceptions.RequestException as error:

            logging.error(
                "Ошибка HTTP: %s",
                error
            )

            time.sleep(RETRY_DELAY)

        except KeyboardInterrupt:

            logging.info(
                "Бот остановлен."
            )

            break

        except Exception as error:

            logging.exception(
                "Неожиданная ошибка: %s",
                error
            )

            time.sleep(RETRY_DELAY)


if __name__ == "__main__":
    main()