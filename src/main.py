import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

def print_author():
    author = os.getenv("AUTHOR")
    if author:
        print(f"Автор проекта: {author}")
    else:
        print("Автор проекта не указан")
print_author() 
