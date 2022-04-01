from pyrogram import Client


# Настройте библиотеку для работы с Telegram и напишите программу, которая выведет количество сообщений в каждом канале
# или супергруппе

client = Client("my_account", api_id=API_ID, api_hash="API_HASH")
client.start()
dialogs = client.get_dialogs()
for dialog in dialogs:
    if dialog.chat.type == "supergroup" or dialog.chat.type == "channel":
        count = client.get_history_count(str(dialog.chat.id))
        print("Кол-во сообщений в " + dialog.chat.type + " " + dialog.chat.title + " - " + str(count))