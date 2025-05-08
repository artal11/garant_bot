# Telegram Guarant Bot для Render

## Установка и запуск на Render.com

1. Залейте этот репозиторий на GitHub
2. Перейдите на https://render.com
3. Создайте новый Web Service, привязав репозиторий
4. Настройки:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python bot.py`
5. В файле `bot.py` замените `YOUR_BOT_TOKEN` на ваш токен от @BotFather