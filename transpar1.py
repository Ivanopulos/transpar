import win32gui#pip install pywin32# невидимка и контроль окон
import win32con
import tkinter as tk

step = "корректировка"
# def set_window_opacity(hwnd, opacity):
#     """ Устанавливает прозрачность окна. """
#     # Проверяем, что прозрачность в диапазоне от 0 до 1
#     if opacity < 0 or opacity > 1:
#         raise ValueError("Прозрачность должна быть в диапазоне от 0 до 1")
#
#     # Преобразуем прозрачность в значение от 0 до 255
#     opacity = int(opacity * 255)
#
#     # Устанавливаем прозрачность окна
#     win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
#                            win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
#     win32gui.SetLayeredWindowAttributes(hwnd, 0, opacity, win32con.LWA_ALPHA)
# def hide_window_from_taskbar(hwnd):
#     """ Скрывает окно с панели задач. """
#     # Скрыть окно
#     #win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
#     win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
#     # Удалить уведомление о окне с панели задач
#     win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
#                            win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_TOOLWINDOW)
#
# if __name__ == "__main__":
#     # Получаем HWND (дескриптор окна) для приложения
#     имяокна = 'keylog – Keylog.py Administrator'#"Fallout II  @640x480x1   "
#     hwnd = win32gui.FindWindow(None, имяокна)
#     if hwnd:
#         # Устанавливаем прозрачность
#         set_window_opacity(hwnd, 0.2)
#         hide_window_from_taskbar(hwnd)
#     else:
#         print("Окно не найдено")

step = "поиск"
def callback(hwnd, extra): # список окон
    window_text = win32gui.GetWindowText(hwnd)
    if window_text:
        print(f"HWND: {hwnd}, Заголовок: {window_text}")
#win32gui.EnumWindows(callback, None)  # полный список

step = "активное"
# hwnd = win32gui.GetForegroundWindow()
# window_text = win32gui.GetWindowText(hwnd)
# print(window_text)

step = "таймер"

import win32gui
import tkinter as tk
from screeninfo import get_monitors
# Функция для вычисления суммарной ширины всех экранов
def get_total_screen_width():
    monitors = get_monitors()
    total_width = sum([monitor.width for monitor in monitors])
    return total_width
# Функция для получения высоты основного экранаghjg
def get_screen_height():
    return root.winfo_screenheight()

def on_submit(razm):
    entered_text = entry.get()

    if entered_text == "свернуть":
        # Уменьшаем окно до минимального размера
        root.geometry("0x0")
        # Через некоторое время восстанавливаем размер
        mnt = 0.1  # в минутах
        root.after(int(mnt * 60000), lambda: restore_window(razm))
    else:
        print(f"Введенный текст: {entered_text}")
        # Окно остается без изменений

def restore_window(razm):
    # Восстанавливаем исходный размер окна
    root.geometry(razm)#root.geometry(f"{razm}+{root.winfo_screenwidth()//2 - 150}-100")

# Создаем главное окно
root = tk.Tk()
root.title("Ввод текста")
root.overrideredirect(True)  # Убираем заголовок окна
#root.attributes("-fullscreen", True)
# Получаем ширину всех экранов и высоту основного экрана
total_width = get_total_screen_width()
screen_height = get_screen_height()
razm = f"{total_width}x{screen_height}"

# Устанавливаем размеры окна
root.geometry(razm)

# Устанавливаем окно поверх всех окон
root.attributes("-topmost", True)
#root.geometry(f"{razm}+0-100")  # root.geometry(f"{razm}+{root.winfo_screenwidth()//2 - 150}-100")

# Создаем метку с инструкцией
label = tk.Label(root, text="Введите текст:")
label.pack(side="top", anchor="w", padx=10, pady=10)

# Создаем поле ввода
entry = tk.Entry(root, width=40)
entry.pack(side="top", anchor="w", padx=10, pady=5)

# Создаем кнопку для подтверждения
submit_button = tk.Button(root, text="Отправить", command=lambda: on_submit(razm))
submit_button.pack(side="top", anchor="w", padx=10, pady=5)

# Запускаем главный цикл обработки событий
root.mainloop()
