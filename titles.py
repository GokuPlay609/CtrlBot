# Standard library modules
# ─────────────────────────────────────────────────────────────
from typing import Dict

# Title function to return title based on group language
# ─────────────────────────────────────────────────────────────
def get_title(chat: str, title: str) -> str:
    titles: Dict[Dict[str]] = {
        "PrivilegeError": {
            "EN": "✘ You Can't do this operation on this user",
            "RU": "✘ Вы не можете выполнить эту операцию для этого пользователя",
            "FA": "✘ شما اجازه انجام این عملیات را برای این کاربر ندارید",
        },

        "ForceJoin": {
            "EN": "⋇ Hi admin {}\.\n\n‣ Sorry but you need to join the channel before using bot commands",
            "RU": "⋇ Привет\, администратор {}\.\n\n‣ Извините\, но вам необходимо присоединиться к каналу\, прежде чем использовать команды бота",
            "FA": "⋇ سلام ادمین {}\.\n\n‣ باید قبل از استفاده از دستورات ربات به کانال بپیوندید"
        },

        "WarnNormal": {
            "EN": "⋇ Dear {}\, Do not repeat this action\. once you reach limit\, you will be muted\!\n\n‣ **Warns**: {}/5",
            "RU": "⋇ Дорогой {}\, не повторяйте это действие\. как только вы достигнете лимита\, ваш звук будет отключен\!\n\n‣ **Предупреждения**: {}/5",
            "FA": "⋇ کاربر {}، این عمل را تکرار نکنید\. هنگامی که به حد مجاز رسیدید، بی صدا خواهید شد\!\n\n‣ **اخطار ها**: {}/5"
        },

        "WarnLimit": {
            "EN": "⋇ Dear {}\, You have reached the warn limits\! You are muted for 1 day",
            "RU": "⋇ Дорогой {}\, Вы достигли пределов предупреждений\! Ваш звук отключен на 1 день",
            "FA": "⋇ کاربر {}، شما به محدودیت های اخطار رسیده اید\! شما به مدت 1 روز بی صدا هستید"
        },

        "WarnEmpty": {
            "EN": "⋇ User {} have no warns",
            "RU": "⋇ У пользователя {} нет предупреждений",
            "FA": "⋇ کاربر {} هیچ اخطاری ندارد"
        }, 

        "WarnDelete": {
            "EN": "⋇ 1 warn deleted for {}\n‣ **Warns**: {}/5",
            "RU": "⋇ 1 предупреждение удалено для {}\n‣ **Предупреждения**: {}/5",
            "FA": "⋇ 1 اخطار برای {} حذف شد\n‣ **اخطار ها**: {}/5"
        },

        "MuteUser": {
            "EN": "⋇ User {} muted for {} minutes",
            "RU": "⋇ Пользователь {} отключил звук на {} минуту",
            "FA": "⋇ کاربر {} به مدت {} دقیقه سکوت شد"
        },

        "MuteAlready": {
            "EN": "✘ User {} is already muted",
            "RU": "✘ У пользователя {} уже отключен звук",
            "FA": "✘ کاربر {} قبلاً سکوت شده است"
        },

        "UnmuteUser": {
            "EN": "⋇ User {} unmuted",
            "RU": "⋇ Пользователь {} включил звук",
            "FA": "⋇ کاربر {} لغو سکوت شد"
        },

        "UnmuteAlready": {
            "EN": "✘ User {} is not muted",
            "RU": "✘ У пользователя {} не отключен звук",
            "FA": "✘ کاربر {} بی صدا نیست"
        },

        "BanUser": {
            "EN": "⋇ User {} banned",
            "RU": "⋇ Пользователь {} забанен",
            "FA": "⋇ کاربر {} مسدود شد"
        },

        "BanAlready": {
            "EN": "✘ User is banned already",
            "RU": "✘ Пользователь уже заблокирован",
            "FA": "✘ کاربر از قبل مسدود شده است"
        },

        "UnbanUser": {
            "EN": "⋇ User {} unbanned",
            "RU": "⋇ Пользователь {} разблокирован",
            "FA": "⋇ کاربر {} توسط مدیران آزاد شد"
        },

        "UserInfo": {
            "EN": "👤 User Info\n\n‣ First name: {}\n‣ Last name: {}\n‣ Username: {}\n‣ User ID: {}\n\n‣ Total Messages: {}\n‣ Privilege: {}",
            "RU": "👤 Информация о пользователе\n\n‣ Имя: {}\n‣ Фамилия: {}\n‣ Имя пользователя: {}\n‣ Идентификатор пользователя: {}\n\n‣ Общее количество сообщений: {}\n‣ Привилегия: {}",
            "FA": "👤 اطلاعات کاربر\n\n‣ نام: {}\n‣ نام خانوادگی: {}\n‣ نام کاربری: {}\n‣ شناسه کاربر: {}\n\n‣ مجموع پیام ها: {}\n‣ دسترسی ها: {}"
        },

        "Language": {
            "EN": "⋇ Please select language for your group!\n\n‣ Current language: 🇺🇸 {}",
            "RU": "⋇ Пожалуйста, выберите язык для вашей группы!\n\n‣ Текущий язык: 🇷🇺 {}",
            "FA": "⋇ لطفاً زبان گروه خود را انتخاب کنید!\n\n‣ زبان فعلی: 🇮🇷 {}"
        },

        "CloseLangMenu": {
            "EN": "✘ Panel has been closed",
            "RU": "✘ Панель закрыта",
            "FA": "✘ پنل بسته شده است"
        },

        "CallBackError": {
            "EN": "☹ You didn't request this action",
            "RU": "☹ Вы не запрашивали это действие",
            "FA": "☹ شما این عمل را درخواست نکرده اید"
        },

        "SetLangauge": {
            "EN": "🇺🇸 Language Set to {}\n‣ Previous Language: {}",
            "RU": "🇷🇺 Язык установлен на {}\n‣ Предыдущий язык: {}",
            "FA": "🇮🇷 زبان تنظیم شد به {}\n‣ زبان قبلی: {}"
        },

        "StatWait": {
            "EN": "⚙️ Getting Stats\! Please wait\.\.\.",
            "RU": "⚙️ Получение статистики\! Пожалуйста\, подождите\.\.\.",
            "FA": "⚙️ در حال دریافت آمار\! لطفاً منتظر بمانید\.\.\."
        },

        "MemberStat": {
            "EN": "{}\. User {} with {} messages\n",
            "RU": "{}\. Пользователь {} с {} сообщениями\n",
            "FA": "{}\. کاربر {} با {} پیام\n"
        },

        "HistoryStat": {
            "EN": "👥 Groups Activity\n\n‣ Messages: {}\n‣ Audios: {}\n‣ Documents: {}\n‣ Gifs: {}\n‣ Photos: {}\n‣ Sticker: {}\n‣ Videoe: {}\n‣ Video notes: {}\n‣ Voices: {}\n\n🏆 Top 5 members\n\n",
            "RU": "👥 Активность группы\n\n‣ Сообщения: {}\n‣ Аудио: {}\n‣ Документы: {}\n‣ Гифы: {}\n‣ Фото: {}\n‣ Стикеры: {}\n‣ Видео: {}\n‣ Видео\-заметки: {}\n‣ Голосовые: {}\n\n🏆 Топ\-5 участников\n\n",
            "FA": "👥 فعالیت‌های گروه\n\n‣ پیام‌ها: {}\n‣ صداها: {}\n‣ اسناد: {}\n‣ گیف‌ها: {}\n‣ عکس‌ها: {}\n‣ استیکر: {}\n‣ ویدیوها: {}\n‣ ویدیو مسیج ها: {}\n‣ ویس مسیج ها: {}\n\n🏆 پنج عضو برتر\n\n"
        },

        "Ping": {
            "EN": "🔒 Group is secure",
            "RU": "🔒 Группа в безопасности",
            "FA": "🔒 گروه ایمن است"
        },

        "UserInfoFail": {
            "EN": "✘ Failed to retrieve user's info",
            "RU": "✘ Не удалось получить информацию о пользователе",
            "FA": "✘ دریافت اطلاعات کاربر ناموفق بود"
        },

        "PinMessage": {
            "EN": "📌 Message has been pinned",
            "RU": "📌 Сообщение закреплено",
            "FA": "📌 پیام مورد نظر سنجاق شد"
        },

        "UnpinMessage": {
            "EN": "✂️ Message has been unpinned",
            "RU": "✂️ Сообщение откреплено",
            "FA": "✂️ پیام مورد نظر از سنجاق خارج شد",
        },

        "DeleteMessageFail": {
            "EN": "✘ Failed to delete message",
            "RU": "✘ Не удалось удалить сообщение",
            "FA": "✘ حذف پیام ناموفق بود"
        },

        "LockFail": {
            "EN": "✘ Failed to lock content type",
            "RU": "✘ Не удалось заблокировать тип контента",
            "FA": "✘ قفل نوع محتوا ناموفق بود"
        },

        "LockAlert": {
            "EN": "✘ dear {}\nSending \(**{}**\) is not allowed in this group",
            "RU": "✘ Дорогой {}\nОтправка \(**{}**\) в этой группе не разрешена",
            "FA": "✘ کاربر {}\nارسال \(**{}**\) در این گروه مجاز نمی باشد"
        },

        "LOCKaudio": {
            "EN": "🔒 Audio locked",
            "RU": "🔒 Аудио заблокировано",
            "FA": "🔒 صدا قفل شده"
        },
        "UNLOCKaudio": {
            "EN": "🔓 Audio unlocked",
            "RU": "🔓 Аудио разблокировано",
            "FA": "🔓 صدا باز شده"
        },
        "LOCKEDALREADYaudio": {
            "EN": "☻ Audio is already locked",
            "RU": "☻ Аудио уже заблокировано",
            "FA": "☻ صدا در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYaudio": {
            "EN": "☻ Audio is already unlocked",
            "RU": "☻ Аудио уже разблокировано",
            "FA": "☻ صدا در حال حاضر باز شده است"
        },

        "LOCKdocument": {
            "EN": "🔒 Document locked",
            "RU": "🔒 Документ заблокирован",
            "FA": "🔒 فایل قفل شده"
        },
        "UNLOCKdocument": {
            "EN": "🔓 Document unlocked",
            "RU": "🔓 Документ разблокирован",
            "FA": "🔓 فایل باز شده"
        },
        "LOCKEDALREADYdocument": {
            "EN": "☻ Document is already locked",
            "RU": "☻ Документ уже заблокирован",
            "FA": "☻ فایل در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYdocument": {
            "EN": "☻ Document is already unlocked",
            "RU": "☻ Документ уже разблокирован",
            "FA": "☻ فایل در حال حاضر باز شده است"
        },

        "LOCKanimation": {
            "EN": "🔒 Animation locked",
            "RU": "🔒 Анимация заблокирована",
            "FA": "🔒 انیمیشن قفل شده"
        },
        "UNLOCKanimation": {
            "EN": "🔓 Animation unlocked",
            "RU": "🔓 Анимация разблокирована",
            "FA": "🔓 انیمیشن باز شده"
        },
        "LOCKEDALREADYanimation": {
            "EN": "☻ Animation is already locked",
            "RU": "☻ Анимация уже заблокирована",
            "FA": "☻ انیمیشن در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYanimation": {
            "EN": "☻ Animation is already unlocked",
            "RU": "☻ Анимация уже разблокирована",
            "FA": "☻ انیمیشن در حال حاضر باز شده است"
        },

        "LOCKgame": {
            "EN": "🔒 Game locked",
            "RU": "🔒 Игра заблокирована",
            "FA": "🔒 بازی قفل شده"
        },
        "UNLOCKgame": {
            "EN": "🔓 Game unlocked",
            "RU": "🔓 Игра разблокирована",
            "FA": "🔓 بازی باز شده"
        },
        "LOCKEDALREADYgame": {
            "EN": "☻ Game is already locked",
            "RU": "☻ Игра уже заблокирована",
            "FA": "☻ بازی در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYgame": {
            "EN": "☻ Game is already unlocked",
            "RU": "☻ Игра уже разблокирована",
            "FA": "☻ بازی در حال حاضر باز شده است"
        },

        "LOCKphoto": {
            "EN": "🔒 Photo locked",
            "RU": "🔒 Фотография заблокирована",
            "FA": "🔒 عکس قفل شده"
        },
        "UNLOCKphoto": {
            "EN": "🔓 Photo unlocked",
            "RU": "🔓 Фотография разблокирована",
            "FA": "🔓 عکس باز شده"
        },
        "LOCKEDALREADYphoto": {
            "EN": "☻ Photo is already locked",
            "RU": "☻ Фотография уже заблокирована",
            "FA": "☻ عکس در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYphoto": {
            "EN": "☻ Photo is already unlocked",
            "RU": "☻ Фотография уже разблокирована",
            "FA": "☻ عکس در حال حاضر باز شده است"
        },

        "LOCKsticker": {
            "EN": "🔒 Sticker locked",
            "RU": "🔒 Стикер заблокирован",
            "FA": "🔒 استیکر قفل شده"
        },
        "UNLOCKsticker": {
            "EN": "🔓 Sticker unlocked",
            "RU": "🔓 Стикер разблокирован",
            "FA": "🔓 استیکر باز شده"
        },
        "LOCKEDALREADYsticker": {
            "EN": "☻ Sticker is already locked",
            "RU": "☻ Стикер уже заблокирован",
            "FA": "☻ استیکر در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYsticker": {
            "EN": "☻ Sticker is already unlocked",
            "RU": "☻ Стикер уже разблокирован",
            "FA": "☻ استیکر در حال حاضر باز شده است"
        },

        "LOCKvideo": {
            "EN": "🔒 Video locked",
            "RU": "🔒 Видео заблокировано",
            "FA": "🔒 ویدیو قفل شده"
        },
        "UNLOCKvideo": {
            "EN": "🔓 Video unlocked",
            "RU": "🔓 Видео разблокировано",
            "FA": "🔓 ویدیو باز شده"
        },
        "LOCKEDALREADYvideo": {
            "EN": "☻ Video is already locked",
            "RU": "☻ Видео уже заблокировано",
            "FA": "☻ ویدیو در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYvideo": {
            "EN": "☻ Video is already unlocked",
            "RU": "☻ Видео уже разблокировано",
            "FA": "☻ ویدیو در حال حاضر باز شده است"
        },

        "LOCKvideo_note": {
            "EN": "🔒 Video note locked",
            "RU": "🔒 Видео-заметка заблокирована",
            "FA": "🔒 یادداشت ویدیو قفل شده"
        },
        "UNLOCKvideo_note": {
            "EN": "🔓 Video note unlocked",
            "RU": "🔓 Видео-заметка разблокирована",
            "FA": "🔓 یادداشت ویدیو باز شده"
        },
        "LOCKEDALREADYvideo_note": {
            "EN": "☻ Video note is already locked",
            "RU": "☻ Видео-заметка уже заблокирована",
            "FA": "☻ یادداشت ویدیو در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYvideo_note": {
            "EN": "☻ Video note is already unlocked",
            "RU": "☻ Видео-заметка уже разблокирована",
            "FA": "☻ یادداشت ویدیو در حال حاضر باز شده است"
        },

        "LOCKvoice": {
            "EN": "🔒 Voice message locked",
            "RU": "🔒 Голосовое сообщение заблокировано",
            "FA": "🔒 پیام صوتی قفل شده"
        },
        "UNLOCKvoice": {
            "EN": "🔓 Voice message unlocked",
            "RU": "🔓 Голосовое сообщение разблокировано",
            "FA": "🔓 پیام صوتی باز شده"
        },
        "LOCKEDALREADYvoice": {
            "EN": "☻ Voice message is already locked",
            "RU": "☻ Голосовое сообщение уже заблокировано",
            "FA": "☻ پیام صوتی در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYvoice": {
            "EN": "☻ Voice message is already unlocked",
            "RU": "☻ Голосовое сообщение уже разблокировано",
            "FA": "☻ پیام صوتی در حال حاضر باز شده است"
        },

        "LOCKcontact": {
            "EN": "🔒 Contact locked",
            "RU": "🔒 Контакт заблокирован",
            "FA": "🔒 مخاطب قفل شده"
        },
        "UNLOCKcontact": {
            "EN": "🔓 Contact unlocked",
            "RU": "🔓 Контакт разблокирован",
            "FA": "🔓 مخاطب باز شده"
        },
        "LOCKEDALREADYcontact": {
            "EN": "☻ Contact is already locked",
            "RU": "☻ Контакт уже заблокирован",
            "FA": "☻ مخاطب در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYcontact": {
            "EN": "☻ Contact is already unlocked",
            "RU": "☻ Контакт уже разблокирован",
            "FA": "☻ مخاطب در حال حاضر باز شده است"
        },

        "LOCKlocation": {
            "EN": "🔒 Location locked",
            "RU": "🔒 Местоположение заблокировано",
            "FA": "🔒 موقعیت مکانی قفل شده"
        },
        "UNLOCKlocation": {
            "EN": "🔓 Location unlocked",
            "RU": "🔓 Местоположение разблокировано",
            "FA": "🔓 موقعیت مکانی باز شده"
        },
        "LOCKEDALREADYlocation": {
            "EN": "☻ Location is already locked",
            "RU": "☻ Местоположение уже заблокировано",
            "FA": "☻ موقعیت مکانی در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYlocation": {
            "EN": "☻ Location is already unlocked",
            "RU": "☻ Местоположение уже разблокировано",
            "FA": "☻ موقعیت مکانی در حال حاضر باز شده است"
        },

        "LOCKvenue": {
            "EN": "🔒 Venue locked",
            "RU": "🔒 Место проведения заблокировано",
            "FA": "🔒 مکان رویداد قفل شده"
        },
        "UNLOCKvenue": {
            "EN": "🔓 Venue unlocked",
            "RU": "🔓 Место проведения разблокировано",
            "FA": "🔓 مکان رویداد باز شده"
        },
        "LOCKEDALREADYvenue": {
            "EN": "☻ Venue is already locked",
            "RU": "☻ Место проведения уже заблокировано",
            "FA": "☻ مکان رویداد در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYvenue": {
            "EN": "☻ Venue is already unlocked",
            "RU": "☻ Место проведения уже разблокировано",
            "FA": "☻ مکان رویداد در حال حاضر باز شده است"
        },

        "LOCKdice": {
            "EN": "🔒 Dice locked",
            "RU": "🔒 Кости заблокированы",
            "FA": "🔒 تاس قفل شده"
        },
        "UNLOCKdice": {
            "EN": "🔓 Dice unlocked",
            "RU": "🔓 Кости разблокированы",
            "FA": "🔓 تاس باز شده"
        },
        "LOCKEDALREADYdice": {
            "EN": "☻ Dice are already locked",
            "RU": "☻ Кости уже заблокированы",
            "FA": "☻ تاس در حال حاضر قفل شده‌اند"
        },
        "UNLOCKEDALREADYdice": {
            "EN": "☻ Dice are already unlocked",
            "RU": "☻ Кости уже разблокированы",
            "FA": "☻ تاس در حال حاضر باز شده‌اند"
        },

        "LOCKinvoice": {
            "EN": "🔒 Invoice locked",
            "RU": "🔒 Счет заблокирован",
            "FA": "🔒 فاکتور قفل شده"
        },
        "UNLOCKinvoice": {
            "EN": "🔓 Invoice unlocked",
            "RU": "🔓 Счет разблокирован",
            "FA": "🔓 فاکتور باز شده"
        },
        "LOCKEDALREADYinvoice": {
            "EN": "☻ Invoice is already locked",
            "RU": "☻ Счет уже заблокирован",
            "FA": "☻ فاکتور در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYinvoice": {
            "EN": "☻ Invoice is already unlocked",
            "RU": "☻ Счет уже разблокирован",
            "FA": "☻ فاکتور در حال حاضر باز شده است"
        },

        "LOCKsuccessful_payment": {
            "EN": "🔒 Successful payment locked",
            "RU": "🔒 Успешный платеж заблокирован",
            "FA": "🔒 پرداخت موفق قفل شده"
        },
        "UNLOCKsuccessful_payment": {
            "EN": "🔓 Successful payment unlocked",
            "RU": "🔓 Успешный платеж разблокирован",
            "FA": "🔓 پرداخت موفق باز شده"
        },
        "LOCKEDALREADYsuccessful_payment": {
            "EN": "☻ Successful payment is already locked",
            "RU": "☻ Успешный платеж уже заблокирован",
            "FA": "☻ پرداخت موفق در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYsuccessful_payment": {
            "EN": "☻ Successful payment is already unlocked",
            "RU": "☻ Успешный платеж уже разблокирован",
            "FA": "☻ پرداخت موفق در حال حاضر باز شده است"
        },

        "LOCKconnected_website": {
            "EN": "🔒 Connected website locked",
            "RU": "🔒 Подключенный веб-сайт заблокирован",
            "FA": "🔒 وب‌سایت متصل قفل شده"
        },
        "UNLOCKconnected_website": {
            "EN": "🔓 Connected website unlocked",
            "RU": "🔓 Подключенный веб-сайт разблокирован",
            "FA": "🔓 وب‌سایت متصل باز شده"
        },
        "LOCKEDALREADYconnected_website": {
            "EN": "☻ Connected website is already locked",
            "RU": "☻ Подключенный веб-сайт уже заблокирован",
            "FA": "☻ وب‌سایت متصل در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYconnected_website": {
            "EN": "☻ Connected website is already unlocked",
            "RU": "☻ Подключенный веб-сайт уже разблокирован",
            "FA": "☻ وب‌سایت متصل در حال حاضر باز شده است"
        },

        "LOCKpoll": {
            "EN": "🔒 Poll locked",
            "RU": "🔒 Опрос заблокирован",
            "FA": "🔒 نظرسنجی قفل شده"
        },
        "UNLOCKpoll": {
            "EN": "🔓 Poll unlocked",
            "RU": "🔓 Опрос разблокирован",
            "FA": "🔓 نظرسنجی باز شده"
        },
        "LOCKEDALREADYpoll": {
            "EN": "☻ Poll is already locked",
            "RU": "☻ Опрос уже заблокирован",
            "FA": "☻ نظرسنجی در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYpoll": {
            "EN": "☻ Poll is already unlocked",
            "RU": "☻ Опрос уже разблокирован",
            "FA": "☻ نظرسنجی در حال حاضر باز شده است"
        },

        "LOCKpassport_data": {
            "EN": "🔒 Passport data locked",
            "RU": "🔒 Данные паспорта заблокированы",
            "FA": "🔒 اطلاعات گذرنامه قفل شده"
        },
        "UNLOCKpassport_data": {
            "EN": "🔓 Passport data unlocked",
            "RU": "🔓 Данные паспорта разблокированы",
            "FA": "🔓 اطلاعات گذرنامه باز شده"
        },
        "LOCKEDALREADYpassport_data": {
            "EN": "☻ Passport data is already locked",
            "RU": "☻ Данные паспорта уже заблокированы",
            "FA": "☻ اطلاعات گذرنامه در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYpassport_data": {
            "EN": "☻ Passport data is already unlocked",
            "RU": "☻ Данные паспорта уже разблокированы",
            "FA": "☻ اطلاعات گذرنامه در حال حاضر باز شده است"
        },

        "LOCKweb_app_data": {
            "EN": "🔒 Web App data locked",
            "RU": "🔒 Данные веб-приложения заблокированы",
            "FA": "🔒 اطلاعات وب‌اپلیکیشن قفل شده"
        },
        "UNLOCKweb_app_data": {
            "EN": "🔓 Web App data unlocked",
            "RU": "🔓 Данные веб-приложения разблокированы",
            "FA": "🔓 اطلاعات وب‌اپلیکیشن باز شده"
        },
        "LOCKEDALREADYweb_app_data": {
            "EN": "☻ Web App data is already locked",
            "RU": "☻ Данные веб-приложения уже заблокированы",
            "FA": "☻ اطلاعات وب‌اپلیکیشن در حال حاضر قفل شده است"
        },
        "UNLOCKEDALREADYweb_app_data": {
            "EN": "☻ Web App data is already unlocked",
            "RU": "☻ Данные веб-приложения уже разблокированы",
            "FA": "☻ اطلاعات وب‌اپلیکیشن در حال حاضر باز شده است"
        },

        "LOCKforward": {
            "EN": "🔒 Forward locked",
            "RU": "🔒 ",
            "FA": "🔒 "
        },
        "UNLOCKforward": {
            "EN": "🔓 Forward unlocked",
            "RU": "🔓 ",
            "FA": "🔓 "
        },
        "LOCKEDALREADYforward": {
            "EN": "☻ Forward is already locked",
            "RU": " ",
            "FA": " "
        },
        "UNLOCKEDALREADYforward": {
            "EN": "☻ Forward is already unlocked",
            "RU": " ",
            "FA": " "
        },

       "VIPadded": {
            "EN": "⋇ User {} added to VIP",
            "RU": "⋇ Пользователь {} добавлен в VIP",
            "FA": "⋇ کاربر {} به VIP اضافه شد"
        },
        "VIPexist": {
            "EN": "✘ User {} is already VIP",
            "RU": "✘ Пользователь {} уже VIP",
            "FA": "✘ کاربر {} از قبل VIP است"
        },
        "VIPdeleted": {
            "EN": "⋇ User {} removed from VIP",
            "RU": "⋇ Пользователь {} удален из VIP",
            "FA": "⋇ کاربر {} از VIP حذف شد"
        },
        "VIPnotexist": {
            "EN": "✘ User {} is not VIP",
            "RU": "✘ Пользователь {} не является VIP",
            "FA": "✘ کاربر {} VIP نیست"
        },

        "CoAadded": {
            "EN": "⋇ User {} promoted to bot admin",
            "RU": "⋇ Пользователь {} повышен до администратора бота",
            "FA": "⋇ کاربر {} به عنوان مدیر ربات منصوب شد"
        },
        "CoAexist": {
            "EN": "✘ User {} is already bot admin",
            "RU": "✘ Пользователь {} уже является администратором бота",
            "FA": "✘ کاربر {} از پیش مدیر ربات است"
        },
        "CoAdeleted": {
            "EN": "⋇ User {} demoted from bot admin",
            "RU": "⋇ Пользователь {} понижен до обычного пользователя",
            "FA": "⋇ کاربر {} از مدیریت ربات خلع شد"
        },
        "CoAnotexist": {
            "EN": "✘ User {} is not bot admin",
            "RU": "✘ Пользователь {} не является администратором бота",
            "FA": "✘ کاربر {} مدیر ربات نیست"
        },

        "NotChatID": {
            "EN": "✘ Invalid Chat-ID entered",
            "RU": "✘ Неверный идентификатор чата",
            "FA": "✘ شناسه‌ی گفتگو نامعتبر"
        },

        "HelpCommand": {
            "EN": "✘ Select command to get its usage",
            "RU": "✘ Выберите команду, чтобы узнать ее использование",
            "FA": "✘ انتخاب دستور برای دریافت راهنما"
        },

        "BotNotStarted": {
            "EN": "✘ You need to start the bot first",
            "RU": "✘ Сначала вам нужно запустить бота",
            "FA": "✘ باید ابتدا ربات را راه‌اندازی کنید"
        },

        "BotBlocked": {
            "EN": "✘ You have blocked the bot!",
            "RU": "✘ Вы заблокировали бота!",
            "FA": "✘ شما ربات را مسدود کرده‌اید!"
        },

        "PromptSent": {
            "EN": "⋇ Prompt sent to your private",
            "RU": "⋇ Подсказка отправлена в ваше личное сообщение",
            "FA": "⋇ پیام ارسال شده به پیام خصوصی شما"
        }
    }

    # Get group language
    try:
        with open(f"Accounts/{chat}/language", "r") as file:
            return titles[title][file.read().strip()]
    
    # Return default English title if no language found
    except FileNotFoundError:
        # Make new file for group
        with open(f"Accounts/{chat}/language", "w") as file:
            file.write("EN")
            
        return titles[title]["EN"]