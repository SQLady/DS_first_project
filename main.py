import os

def print_author():
    author = os.getenv("AUTHOR")
    if author:
        print(f"Автор проекта: {author}")
    else:
        print("Автор проекта не указан")
