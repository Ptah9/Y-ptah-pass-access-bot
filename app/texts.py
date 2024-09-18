from aiogram.utils.markdown import hide_link

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
            f"{hide_link('https://raw.githubusercontent.com/Ptah9/Y-Ptah-projects-images/main/ptah-pass-images/hi.jpg')}"
            "🤖 <b>привет!</b>\n\n"
            "Здесь ты можешь предъявить свой пропуск"
            "и попасть в приватный канал + чат @ptah_9\n\n"
            # "<blockquote><b>Приватные чаты:</b>\n{chats}\n"
            # "<b>Необходимые токены:</b>\n{tokens}</blockquote>\n\n"
            "Жми на <b>предъявить пропуск</b> и проходи!\n"
            "Но помни, если ты продашь свой пропуск, бот выгонит из чата и канала!\n\n"
            "ну и не забывай подписываться на мой основной канал @what_now_ptah, там весело!\n\n"
            "<b>Подключен к:</b> {wallet}"
        ),
        "select_language": (
            f"{hide_link('https://raw.githubusercontent.com/Ptah9/Y-Ptah-projects-images/main/ptah-pass-images/waining.jpg')}"
            "👋 <b>ку!</b>\n\n"
            "выбирай язык:"
        ),
        "change_language": (
            f"{hide_link('https://raw.githubusercontent.com/Ptah9/Y-Ptah-projects-images/main/ptah-pass-images/waining.jpg')}"
            "<b>выбирай язык:</b>"
        ),
        "deny_access": (
            f"{hide_link('https://raw.githubusercontent.com/Ptah9/Y-Ptah-projects-images/main/ptah-pass-images/no.jpg')}"
            "🚫 <b> у тебя нет пропуска</b>\n\n"
            "Ты что, хотел меня обмануть???? У тебя же нет пропуска в приватку\n\n"
            "Не расстраивайся, ты можешь <b>купить себе пропуск</b> ниже и повторить попытку."
        ),
        "allow_access": (
            f"{hide_link('https://raw.githubusercontent.com/Ptah9/Y-Ptah-projects-images/main/ptah-pass-images/okay.jpg')}"
            "🎉 <b>все в норме, проходите</b>\n\n"
            "Вижу, пропуск на месте, проходи, будь как дома\n\n"
            "По кнопкам ниже подавай заявку на вступление, я сразу же их одобрю!"
        ),
        "connect_wallet": (
            f"<a href='https://ton.org/wallets?filters[wallet_features][slug][$in]=dapp-auth&pagination[limit]=-1'>Установить кошелек</a>\n\n"
            "<b>Подключи свой {wallet_name}!</b>\n\n"
            "отсканируй с помощью кошелька на телефоне:"
        ),
        "connect_wallet_proof_wrong": (
            f"{hide_link('https://raw.githubusercontent.com/Ptah9/Y-Ptah-projects-images/main/ptah-pass-images/oops.jpg')}"
            "<b>стой, проблемка</b>\n\n"
            "подпись кошелька поддельна или истекло время ожидания подключения."
        ),
        "connect_wallet_timeout": (
            f"{hide_link('https://raw.githubusercontent.com/Ptah9/Y-Ptah-projects-images/main/ptah-pass-images/oops.jpg')}"
            "<b>стой, проблемка</b>\n\n"
            "время ожидания подключения истекло."
        ),

        "admin_menu": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
            "<b>панель администратора</b>\n\nвыберите действие:"
        ),
        "chats_menu": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
            "<b>меню приватных чатов</b>\n\выберите действие:"
        ),
        "chat_info": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
            "• <b>информация о приватном чате</b>\n\n"
            "• <b>ID:</b>\n"
            "<blockquote>{chat_id}</blockquote>\n"
            "• <b>тип:</b>\n"
            "<blockquote>{chat_type}</blockquote>\n"
            "• <b>название:</b>\n"
            "<blockquote>{chat_name}</blockquote>\n"
            "• <b>ссылка приглашения:</b>\n"
            "<blockquote>{chat_invite_link}</blockquote>\n"
            "• <b>дата создания:</b>\n"
            "<blockquote>{chat_created_at}</blockquote>"
        ),
        "tokens_menu": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
            "<b>меню токенов</b>\n\nвыберите действие:"
        ),
        "token_info": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
            "• <b>информация о токене</b>\n\n"
            "• <b>тип:</b>\n"
            "<blockquote>{token_type}</blockquote>\n"
            "• <b>название:</b>\n"
            "<blockquote>{token_name}</blockquote>\n"
            "• <b>адрес:</b>\n"
            "<blockquote>{token_address}</blockquote>\n"
            "• <b>минимальная сумма:</b>\n"
            "<blockquote>{token_min_amount}</blockquote>\n"
            "• <b>дата создания:</b>\n"
            "<blockquote>{token_created_at}</blockquote>"
        ),
        "token_send_address": "<b>введите адрес токена</b>\n\nразрешены только адреса коллекций NFT и мастеров Jetton:",
        "token_send_address_error": "Недопустимый адрес токена:\n{}",
        "token_send_address_error_already_exist": "токен с адресом {address} уже существует!",
        "token_send_address_error_not_supported": "контракт {interfaces} не поддерживается.\nподдерживаются только {supported_interfaces}.",
        "token_send_amount": (
            "<b>информация о токене</b>:\n\n"
            "• <b>тип:</b>\n{token_type}\n"
            "• <b>название:</b>\n{token_name}\n\n"
            "<b>введите минимальную сумму токена</b> для доступа к приватному чату:"
        ),
        "token_edit_amount": "<b>введите новую сумму токена</b> для доступа к приватному чату:",
        "token_send_amount_error": "неверная сумма токена!",
        "admins_menu": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
            "<b>меню администраторов</b>\n\nвыберите действие:"
        ),
        "admin_info": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
            "• <b>информация об администраторе</b>\n\n"
            "• <b>ID:</b>\n"
            "<blockquote>{admin_id}</blockquote>\n"
            "• <b>имя:</b>\n"
            "<blockquote>{admin_full_name}</blockquote>\n"
            "• <b>имя пользователя:</b>\n"
            "<blockquote>{admin_username}</blockquote>\n"
            "• <b>дата создания:</b>\n"
            "<blockquote>{admin_created_at}</blockquote>"
        ),
        "admin_send_id": "<b>введите ID администратора:</b>",
        "admin_send_id_error": "недопустимый ID:\n{}",
        "admin_send_id_error_not_found": "администратор не найден. Сначала пользователь должен начать диалог с ботом.",
        "admin_send_id_error_not_member": "ID администратора должен быть числом.",
        "confirm_item_add": "<b>подтвердите</b> добавление {item} в {table}?",
        "item_added": "{item} добавлен в {table}!",
        "confirm_item_delete": "<b>подтвердите</b> удаление {item} из {table}?",
        "item_deleted": "{item} удален из {table}!"
    },
    "en": {
        "loader_text": "⏳",
        "outdated_text": "...",
        "main_menu": (
            f"{hide_link('https://telegra.ph//file/db9c5c3febe75811e41af.jpg')}"
            "🤖 <b>Hi!</b>\n\n"
            "Here you can show your pass"
            "and get into Anton’s private channel + chat of @Ptah_9\n\n"
            # "<blockquote><b>Private Chats:</b>\n{chats}\n"
            # "<b>Required Tokens:</b>\n{tokens}</blockquote>\n\n"
            "Click on <b>show pass</b> and go through!\n"
            "But remember, if you sell your pass, the bot will kick you out of the chat and channel!\n\n"
            "Well, don’t forget to subscribe to my main channel @what_now_ptah, it’s fun!\n\n"
            "<b>Connected to:</b> {wallet}"
        ),
        "select_language": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
            "👋 <b>Hello!</b>\n\n"
            "сhoose a language:"
        ),
        "change_language": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
            "<b>сhoose a language:</b>"
        ),
        "deny_access": (
            f"{hide_link('https://telegra.ph//file/ceec89ba75c903210411c.jpg')}"
            "🚫 <b>You don't have a pass</b>\n\n"
            "Did you want to deceive me??? You don't have a private pass\n\n"
            "Don't worry, you can <b>buy your pass</b> below and try again."
        ),
        "allow_access": (
            f"{hide_link('https://telegra.ph//file/6b03c59182d959cddeb02.jpg')}"
            "🎉 <b>everything is fine, come in</b>\n\n"
            "I see the pass is there, come in, make yourself at home\n\n"
            "Use the buttons below to apply for membership, I will approve them immediately!"
        ),

        "connect_wallet": (
            f"<a href='https://ton.org/wallets?filters[wallet_features][slug][$in]=dapp-auth&pagination[limit]=-1'>Get a Wallet</a>\n\n"
            "<b>Connect your {wallet_name}!</b>\n\n"
            "scan with your mobile app wallet:"
        ),
        "connect_wallet_proof_wrong": (
            f"{hide_link('https://telegra.ph//file/a4ddc111ff41692ad5200.jpg')}"
            "<b>Warning</b>\n\n"
            "the wallet signature is wrong or the connection timeout has expired."
        ),
        "connect_wallet_timeout": (
            f"{hide_link('https://telegra.ph//file/a4ddc111ff41692ad5200.jpg')}"
            "<b>Warning</b>\n\n"
            "the connection timeout has expired."
        ),

        "admin_menu": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
            "<b>administrator Panel</b>\n\nselect action:"
        ),
        "chats_menu": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
            "<b>private Chats Menu</b>\n\nselect action:"
        ),
        "chat_info": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
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
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
            "<b>Tokens Menu</b>\n\nSelect action:"
        ),
        "token_info": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
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
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
            "<b>Administrators Menu</b>\n\nSelect action:"
        ),
        "admin_info": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
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
