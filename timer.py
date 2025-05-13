import time


def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"\r⏳ Осталось: {timer}", end="")
        time.sleep(1)
        seconds -= 1
    print("\n⏰ Время вышло! Сделай перерыв.")


print("=== Pomodoro-таймер ===")

try:
    focus_minutes = int(
        input("На сколько минут установить таймер? (по умолчанию 25): ") or 25
    )
    countdown(focus_minutes)
except KeyboardInterrupt:
    print("\nТаймер остановлен вручную.")
