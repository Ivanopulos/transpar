import win32gui#pip install pywin32
import win32con


step = "корректировка"
def set_window_opacity(hwnd, opacity):
    """ Устанавливает прозрачность окна. """
    # Проверяем, что прозрачность в диапазоне от 0 до 1
    if opacity < 0 or opacity > 1:
        raise ValueError("Прозрачность должна быть в диапазоне от 0 до 1")

    # Преобразуем прозрачность в значение от 0 до 255
    opacity = int(opacity * 255)

    # Устанавливаем прозрачность окна
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, 0, opacity, win32con.LWA_ALPHA)
def hide_window_from_taskbar(hwnd):
    """ Скрывает окно с панели задач. """
    # Скрыть окно
    #win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    # Удалить уведомление о окне с панели задач
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_TOOLWINDOW)

if __name__ == "__main__":
    # Получаем HWND (дескриптор окна) для приложения
    имяокна = 'keylog – Keylog.py Administrator'#"Fallout II  @640x480x1   "
    hwnd = win32gui.FindWindow(None, имяокна)
    if hwnd:
        # Устанавливаем прозрачность
        set_window_opacity(hwnd, 0.2)
        hide_window_from_taskbar(hwnd)
    else:
        print("Окно не найдено")

step="поиск"
# def callback(hwnd, extra): # список окон
#     window_text = win32gui.GetWindowText(hwnd)
#     if window_text:
#         print(f"HWND: {hwnd}, Заголовок: {window_text}")
#
# win32gui.EnumWindows(callback, None)