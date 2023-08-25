from pyrogram import Client
from pyrogram.types import Poll
import os.path
import asyncio
import platform

GREEN = "\033[1;32m"
RED = "\033[1;31m"
RESET = "\033[0m"

def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')  # Для Windows
    else:
        os.system('clear')  # Для (Linux, macOS)

clear_terminal()

async def is_valid_channel(app, username):
    try:
        chat = await app.get_chat(username)
        return True
    except Exception as e:
        print(f"{RED}Произошла ошибка{RESET} при получении информации о канале {username}")
        return False

async def main():
    if os.path.isfile("my_session.session"):
        print(f"{GREEN}Файл сессии найден.{RESET}")
        app = Client("my_session")
    else:
        print(f"{RED}Файл сессии не найден.{RESET} Запрос API ID и Hash.")
        api_id = input("Введите ваш API ID: ")
        api_hash = input("Введите ваш API Hash: ")
        app = Client("my_session", api_id=api_id, api_hash=api_hash)


    async with app:
        username_from = input("Введите юзернейм исходного канала: ")
        username_to = input("Введите юзернейм целевого канала: ")

        if not await is_valid_channel(app, username_from) or not await is_valid_channel(app, username_to):
            return
        
        chat_from = await app.get_chat(username_from)
        chat_to = await app.get_chat(username_to)
        
        chat_id_from = chat_from.id
        chat_id_to = chat_to.id

        sent_messages = set()
        sent_polls = set()
        all_posts = []
            
        async for message in app.get_chat_history(chat_id_from):
            all_posts.append(message)
           
        for message in all_posts[::-1]:
            if message.text and message.text not in sent_messages:
                print(f"++ {GREEN}Пост{RESET}: \n- '{message.text}' \n== был добавлен\n\n")
                sent_messages.add(message.text)
                await app.send_message(chat_id_to, message.text)
            
            if message.photo and message.caption not in sent_messages:
                print(f"++ {RED}Фото{RESET}: \n- {message.photo.file_id} \n- {message.caption} \n== было добавлено\n\n")
                sent_messages.add(message.caption)
                await app.send_photo(chat_id_to, photo=message.photo.file_id, caption=message.caption)
                
            if message.video and message.caption not in sent_messages:
                print(f"++ {RED}Видео{RESET}: \n- {message.video.file_id} \n- {message.caption} \n== было добавлено\n\n")
                sent_messages.add(message.caption)
                await app.send_video(chat_id_to, video=message.video.file_id, caption=message.caption)
                
            if message.document and message.document.file_id not in sent_messages:
                print(f"++ Файл: \n- {message.document.file_id} \n- {message.caption} \n== был добавлен\n\n")
                sent_messages.add(message.document.file_id)
                await app.send_document(chat_id_to, document=message.document.file_id, caption=message.caption)
                
            if isinstance(message.poll, Poll) and message.poll.id not in sent_polls:
                sent_polls.add(message.poll.id)
    
                poll_question = message.poll.question
                poll_options = [option.text for option in message.poll.options]
                
                print(f"++ {RED}Голосование{RESET}: \n- {poll_options} \n== было добавлено\n\n")

                await app.send_poll(chat_id_to, question=poll_question, options=poll_options)

            await asyncio.sleep(5)

if __name__ == '__main__':
    asyncio.run(main())
