import yt_dlp
import os
import sys

def get_download_path():
    """
    Получаем путь для сохранения файлов.
    Папка video создаётся в той же директории, где находится запускаемый файл программы.
    """
    # Получаем путь к директории, где находится запускаемый файл
    if getattr(sys, 'frozen', False):  # Если программа собрана в exe (например, через PyInstaller)
        base_path = os.path.dirname(sys.executable)
    else:  # Если программа запускается как скрипт
        base_path = os.path.dirname(os.path.abspath(__file__))

    # Путь к папке video
    download_path = os.path.join(base_path, "video")

    # Создаем папку, если она не существует
    if not os.path.exists(download_path):
        os.makedirs(download_path)
        print(f"Папка {download_path} создана.")

    return download_path

def download_video(url, quality='best'):
    """
    Скачивание видео.
    """
    download_path = get_download_path()  # Получаем путь к папке video

    ydl_opts = {
        'format': quality,
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Сохраняем в папку video
        'quiet': False,  # Показывать прогресс скачивания
        'no_warnings': False,  # Показывать предупреждения
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Видео успешно скачано и сохранено в папку: {download_path}")
    except Exception as e:
        print(f"Ошибка при скачивании видео: {e}")

def download_audio(url, quality='bestaudio'):
    """
    Скачивание аудио.
    """
    download_path = get_download_path()  # Получаем путь к папке video

    ydl_opts = {
        'format': quality,
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Сохраняем в папку video
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,  # Показывать прогресс скачивания
        'no_warnings': False,  # Показывать предупреждения
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Аудио успешно скачано и сохранено в папку: {download_path}")
    except Exception as e:
        print(f"Ошибка при скачивании аудио: {e}")

def show_menu():
    """
    Отображает главное меню.
    """
    print("\n--- Меню ---")
    print("1. Скачать видео")
    print("2. Скачать аудио")
    print("3. Выйти")

def main():
    while True:
        show_menu()
        choice = input("Выберите опцию: ").strip()

        if choice == '1':
            url = input("Введите URL видео: ").strip()
            print("Выберите качество видео:")
            print("1. Лучшее качество")
            print("2. 1080p")
            print("3. 720p")
            print("4. 480p")
            quality_choice = input("Ваш выбор: ").strip()

            if quality_choice == '1':
                quality = 'best'
            elif quality_choice == '2':
                quality = 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'
            elif quality_choice == '3':
                quality = 'bestvideo[height<=720]+bestaudio/best[height<=720]'
            elif quality_choice == '4':
                quality = 'bestvideo[height<=480]+bestaudio/best[height<=480]'
            else:
                print("Неверный выбор, используется лучшее качество.")
                quality = 'best'

            download_video(url, quality)

        elif choice == '2':
            url = input("Введите URL видео: ").strip()
            download_audio(url)

        elif choice == '3':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()