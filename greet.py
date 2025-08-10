from datetime import datetime

now = datetime.now()
print(f"Привет! Сегодня {now.strftime('%d.%m.%Y')} и время {now.strftime('%H:%M:%S')}")
