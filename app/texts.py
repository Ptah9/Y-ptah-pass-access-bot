from aiogram.utils.markdown import hide_link

from .texts_pics import pictures

# Add other languages and their corresponding codes as needed.
SUPPORTED_LANGUAGES = {
    "ru": "🇷🇺 Русский",
    "en": "🇬🇧 English",
}

TEXT_BUTTONS = {
    "ru": {
        "add": "﹢ добавить",
        "back": "‹ назад",
        "main": "≡ главная",
        "retry": "↻ повторить",
        "delete": "× удалить",
        "confirm": "✓ подтвердить",

        "connect_wallet": "подключить {wallet_name}",
        "open_wallet": "перейти в {wallet_name}",
        "disconnect_wallet": "× отключиться",

        "change_language": "↻ изменить язык",
        "get_access": "🪪 предъявить пропуск",

        "newsletter": "📰 поспамить пользователям",
        "admins_menu": "👨‍💻 админы",
        "chats_menu": "💬 чаты",
        "tokens_menu": "💎 токены",
        "edit_min_amount": "✎ изменить минимальную сумму",
    },
    "en": {
        "add": "﹢ add",
        "back": "‹ back",
        "main": "≡ main",
        "retry": "↻ retry",
        "delete": "× delete",
        "confirm": "✓ confirm",

        "connect_wallet": "connect {wallet_name}",
        "open_wallet": "go to {wallet_name}",
        "disconnect_wallet": "× disconnect",

        "change_language": "↻ change Language",
        "get_access": "🪪 show pass",

        "newsletter": "📰 newsletter",
        "admins_menu": "👥 admins",
        "chats_menu": "💬 chats",
        "tokens_menu": "💎 tokens",
        "edit_min_amount": "✎ edit minimum amount",
    }
}

TEXT_MESSAGES = {
    "ru": {
        "loader_text": "⏳",
        "outdated_text": "...",

        "main_menu": (
            f"{hide_link(pictures['Hi'])}"
            "🤖 <b>привет!</b>\n\n"
            "Здесь ты можешь предъявить свой пропуск Ptah pass "
            "и получить все привилегии, которые он может дать на данный момент\n\n"
            # "<blockquote><b>Приватные чаты:</b>\n{chats}\n"
            # "<b>Необходимые токены:</b>\n{tokens}</blockquote>\n\n"
            "Жми на <b>предъявить пропуск</b> и проходи!\n"
            "Но помни, если ты продашь свой пропуск, бот заберет у тебя все привилегии и выгонит из всех приватных чатов!\n\n"
            "ну и не забывай подписываться на канал Ptah Industries - @Ptah_Industries, там будут выкладываться все новости, и основной канал Птаха - @what_now_ptah, там весело и полезно!\n\n"
            "<b>Подключен к:</b> {wallet}"
        ),
        "select_language": (
            f"{hide_link(pictures['Waiting'])}"
            "👋 <b>ку!</b>\n\n"
            "выбирай язык:"
        ),
        "change_language": (
            f"{hide_link(pictures['Waiting'])}"
            "<b>Выбери язык:</b>"
        ),
        "deny_access": (
            f"{hide_link(pictures['No'])}"
            "🚫 <b> у тебя нет пропуска</b>\n\n"
            "Ты что, хотел меня обмануть???? У тебя же нет пропуска в приватку\n\n"
            "Не расстраивайся, ты можешь <b>купить себе пропуск</b> ниже и повторить попытку."
        ),
        "allow_access": (
            f"{hide_link(pictures['Okay'])}"
            "🎉 <b>все в норме, проходите</b>\n\n"
            "Вижу, пропуск на месте, проходи, будь как дома\n\n"
            "По кнопкам ниже подавай заявки на вступление, я сразу же их одобрю!"
        ),
        "user_kicked": (
            "пользователя {user} [{wallet}] выгнали отовсюду!"
        ),

        "connect_wallet": (
            f"<a href='https://ton.org/wallets?filters[wallet_features][slug][$in]=dapp-auth&pagination[limit]=-1'>Установить кошелек</a>\n\n"
            "<b>Подключи свой {wallet_name}!</b>\n\n"
            "отсканируй с помощью кошелька на телефоне:"
        ),
        "connect_wallet_proof_wrong": (
            f"{hide_link(pictures['Oops'])}"
            "<b>стой, проблемка</b>\n\n"
            "подпись кошелька поддельна или истекло время ожидания подключения."
        ),
        "connect_wallet_timeout": (
            f"{hide_link(pictures['Oops'])}"
            "<b>стой, проблемка</b>\n\n"
            "время ожидания подключения истекло."
        ),

        "admin_menu": (
            f"{hide_link(pictures['Main'])}"
            "<b>Панель администратора</b>\n\nВыберите действие:"
        ),
        "chats_menu": (
            f"{hide_link(pictures['Main'])}"
            "<b>Меню приватных чатов</b>\n\nВыберите действие:"
        ),
        "chat_info": (
            f"{hide_link(pictures['Main'])}"
            "• <b>Информация о приватном чате</b>\n\n"
            "• <b>ID:</b>\n"
            "<blockquote>{chat_id}</blockquote>\n"
            "• <b>Тип:</b>\n"
            "<blockquote>{chat_type}</blockquote>\n"
            "• <b>Название:</b>\n"
            "<blockquote>{chat_name}</blockquote>\n"
            "• <b>Ссылка приглашения:</b>\n"
            "<blockquote>{chat_invite_link}</blockquote>\n"
            "• <b>Дата создания:</b>\n"
            "<blockquote>{chat_created_at}</blockquote>"
        ),
        "tokens_menu": (
            f"{hide_link(pictures['Main'])}"
            "<b>Меню токенов</b>\n\nВыберите действие:"
        ),
        "token_info": (
            f"{hide_link(pictures['Main'])}"
            "• <b>Информация о токене</b>\n\n"
            "• <b>Тип:</b>\n"
            "<blockquote>{token_type}</blockquote>\n"
            "• <b>Название:</b>\n"
            "<blockquote>{token_name}</blockquote>\n"
            "• <b>Адрес:</b>\n"
            "<blockquote>{token_address}</blockquote>\n"
            "• <b>Минимальная сумма:</b>\n"
            "<blockquote>{token_min_amount}</blockquote>\n"
            "• <b>Дата создания:</b>\n"
            "<blockquote>{token_created_at}</blockquote>"
        ),
        "token_send_address": "<b>Введите адрес токена</b>\n\nРазрешены только адреса коллекций NFT и мастеров Jetton:",
        "token_send_address_error": "Недопустимый адрес токена:\n{}",
        "token_send_address_error_already_exist": "Токен с адресом {address} уже существует!",
        "token_send_address_error_not_supported": "Контракт {interfaces} не поддерживается.\nПоддерживаются только {supported_interfaces}.",
        "token_send_amount": (
            "<b>Информация о токене</b>:\n\n"
            "• <b>Тип:</b>\n{token_type}\n"
            "• <b>Название:</b>\n{token_name}\n\n"
            "<b>Введите минимальную сумму токена</b> для доступа к приватному чату:"
        ),
        "token_edit_amount": "<b>Введите новую сумму токена</b> для доступа к приватному чату:",
        "token_send_amount_error": "Неверная сумма токена!",
        "admins_menu": (
            f"{hide_link(pictures['Main'])}"
            "<b>Меню администраторов</b>\n\nВыберите действие:"
        ),
        "admin_info": (
            f"{hide_link(pictures['Main'])}"
            "• <b>Информация об администраторе</b>\n\n"
            "• <b>ID:</b>\n"
            "<blockquote>{admin_id}</blockquote>\n"
            "• <b>Имя:</b>\n"
            "<blockquote>{admin_full_name}</blockquote>\n"
            "• <b>Имя пользователя:</b>\n"
            "<blockquote>{admin_username}</blockquote>\n"
            "• <b>Дата создания:</b>\n"
            "<blockquote>{admin_created_at}</blockquote>"
        ),
        "admin_send_id": "<b>Введите ID администратора:</b>",
        "admin_send_id_error": "Недопустимый ID:\n{}",
        "admin_send_id_error_not_found": "Администратор не найден. Сначала пользователь должен начать диалог с ботом.",
        "admin_send_id_error_not_member": "ID администратора должен быть числом.",
        "confirm_item_add": "<b>Подтвердите</b> добавление {item} в {table}?",
        "item_added": "{item} добавлен в {table}!",
        "confirm_item_delete": "<b>Подтвердите</b> удаление {item} из {table}?",
        "item_deleted": "{item} удален из {table}!"
    },
    "en": {
        "loader_text": "⏳",
        "outdated_text": "...",

        "main_menu": (
            f"{hide_link(pictures['Hi'])}"
            "🤖 <b>Hi!</b>\n\n"
            "Here you can show your Ptah pass "
            "and get all the privileges it can give at the moment\n\n"
            # "<blockquote><b>Private Chats:</b>\n{chats}\n"
            # "<b>Required Tokens:</b>\n{tokens}</blockquote>\n\n"
            "Click on <b>show pass</b> and go through!\n"
            "But remember, if you sell your pass, the bot will take away all your privileges and kick you out of all private chats!\n\n"
            "also don’t forget to subscribe to the Ptah Industries channel - @Ptah_Industries, all the news will be posted there, and the main Ptah channel - @what_now_ptah, it’s fun and useful there!\n\n"
            "<b>Connected to:</b> {wallet}"
        ),
        "select_language": (
            f"{hide_link(pictures['Hi'])}"
            "👋 <b>Hello!</b>\n\n"
            "Choose a language:"
        ),
        "change_language": (
            f"{hide_link(pictures['Hi'])}"
            "<b>Choose a language:</b>"
        ),
        "deny_access": (
            f"{hide_link(pictures['No'])}"
            "🚫 <b>You don't have a pass</b>\n\n"
            "Did you want to deceive me??? You don't have a private pass\n\n"
            "Don't worry, you can <b>buy your pass</b> below and try again."
        ),
        "allow_access": (
            f"{hide_link(pictures['Okay'])}"
            "🎉 <b>everything is fine, come in</b>\n\n"
            "I see the pass is there, come in, make yourself at home\n\n"
            "Use the buttons below to apply for membership, I will approve them immediately!"
        ),
        "user_kicked": (
            "User {user} [{wallet}] was kicked from chat and chanel!"
        ),

        "connect_wallet": (
            f"<a href='https://ton.org/wallets?locale=en&filters[wallet_features][slug][$in]=dapp-auth&pagination[limit]=-1'>Get a Wallet</a>\n\n"
            "<b>Connect your {wallet_name}!</b>\n\n"
            "Scan with your mobile app wallet:"
        ),
        "connect_wallet_proof_wrong": (
            f"{hide_link(pictures['Oops'])}"
            "<b>Warning</b>\n\n"
            "The wallet signature is wrong or the connection timeout has expired."
        ),
        "connect_wallet_timeout": (
            f"{hide_link(pictures['Oops'])}"
            "<b>Warning</b>\n\n"
            "The connection timeout has expired."
        ),

        "admin_menu": (
            f"{hide_link(pictures['Main'])}"
            "<b>Administrator Panel</b>\n\nSelect action:"
        ),
        "chats_menu": (
            f"{hide_link(pictures['Main'])}"
            "<b>Private Chats Menu</b>\n\nSelect action:"
        ),
        "chat_info": (
            f"{hide_link(pictures['Main'])}"
            "• <b>Private Chat Information</b>\n\n"
            "• <b>ID:</b>\n"
            "<blockquote>{chat_id}</blockquote>\n"
            "• <b>Type:</b>\n"
            "<blockquote>{chat_type}</blockquote>\n"
            "• <b>Name:</b>\n"
            "<blockquote>{chat_name}</blockquote>\n"
            "• <b>Invite Link:</b>\n"
            "<blockquote>{chat_invite_link}</blockquote>\n"
            "• <b>Creation Date:</b>\n"
            "<blockquote>{chat_created_at}</blockquote>"
        ),
        "tokens_menu": (
            f"{hide_link(pictures['Main'])}"
            "<b>Tokens Menu</b>\n\nSelect action:"
        ),
        "token_info": (
            f"{hide_link(pictures['Main'])}"
            "• <b>Token Information</b>\n\n"
            "• <b>Type:</b>\n"
            "<blockquote>{token_type}</blockquote>\n"
            "• <b>Name:</b>\n"
            "<blockquote>{token_name}</blockquote>\n"
            "• <b>Address:</b>\n"
            "<blockquote>{token_address}</blockquote>\n"
            "• <b>Minimum Amount:</b>\n"
            "<blockquote>{token_min_amount}</blockquote>\n"
            "• <b>Creation Date:</b>\n"
            "<blockquote>{token_created_at}</blockquote>"
        ),
        "token_send_address": "<b>Enter Token Address</b>\n\nOnly NFT collection and Jetton master addresses are allowed:",
        "token_send_address_error": "Invalid token address:\n{}",
        "token_send_address_error_already_exist": "Token with address {address} already exists!",
        "token_send_address_error_not_supported": "Contract {interfaces} is not supported.\nOnly {supported_interfaces} are supported.",
        "token_send_amount": (
            "<b>Token Information</b>:\n\n"
            "• <b>Type:</b>\n"
            "<blockquote>{token_type}</blockquote>\n"
            "• <b>Name:</b>\n"
            "<blockquote>{token_name}</blockquote>\n\n"
            "<b>Enter the minimum token amount</b> to access the private chat:"
        ),
        "token_edit_amount": "<b>Enter the new token amount</b> to access the private chat:",
        "token_send_amount_error": "Invalid token amount!",
        "admins_menu": (
            f"{hide_link(pictures['Main'])}"
            "<b>Administrators Menu</b>\n\nSelect action:"
        ),
        "admin_info": (
            f"{hide_link(pictures['Main'])}"
            "• <b>Administrator Information</b>\n\n"
            "• <b>ID:</b>\n"
            "<blockquote>{admin_id}</blockquote>\n"
            "• <b>Name:</b>\n"
            "<blockquote>{admin_full_name}</blockquote>\n"
            "• <b>Username:</b>\n"
            "<blockquote>{admin_username}</blockquote>\n"
            "• <b>Creation Date:</b>\n"
            "<blockquote>{admin_created_at}</blockquote>"
        ),
        "admin_send_id": "<b>Enter Administrator ID:</b>",
        "admin_send_id_error": "Invalid ID:\n{}",
        "admin_send_id_error_not_found": "Administrator not found. First, the user needs to start a conversation with the bot.",
        "admin_send_id_error_not_member": "Administrator ID must be a number.",
        "confirm_item_add": "<b>Confirm</b> adding {item} to {table}?",
        "item_added": "{item} added to {table}!",
        "confirm_item_delete": "<b>Confirm</b> deleting {item} from {table}?",
        "item_deleted": "{item} deleted from {table}!"
    }
}