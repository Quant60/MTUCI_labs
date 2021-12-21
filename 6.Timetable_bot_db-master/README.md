# Timetable_bot_db
Task:Create a telegram bot for the schedule using the “telebot” library and link a database to it. The bot should be able to determine the number of the week, and be able to make a schedule both for a specific day and for the whole week. 

Progress:


1.We write "BotFather" in Telegram and create our own bot.

2.In the main.py file, import the libraries for creating the bot.

3.We take the token from the bot and insert it into our code.

4.We create the bot object in the code.

5.Create a decorator responsible for the /start command.

6.Create decorators that respond to commands (“Понедельник”, “Вторник”, “Среда”, “4етверг”, “Пятница”, “Расписание на текущую неделю”, “Расписание на следующую неделю”).

7.Create a database and connect to it.

8.Create schemas "subject", "timetable", "teachers".

9.Create a table in the database, fill them in, and create a link between them. 
