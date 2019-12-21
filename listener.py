import time

import PyHook3
import pythoncom

log = ''


def onKeyboardEvent(event):
    global log
    # 监听键盘事件
    # print("MessageName:", event.MessageName)
    msg = f'{int(event.Time)}: "{event.Key}",\n'
    log += msg
    if str(event.Key) == 'Escape':
        with open(f'listener_{time.time()}.txt', 'w') as fout:
            fout.write(log)
        print(f'listener_{time.time()}.txt saved.\a')
        log = ''
    return True


def main():
    hm = PyHook3.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()


if __name__ == "__main__":
    main()
