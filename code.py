import telebot
import random
import string

bot = telebot.TeleBot('6398417526:AAE180ZCkZdGLiu-nrxeyCEUJZo7KaIMcVw')

def generate_password(length):
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for i in range(length))
  return password


@bot.message_handler(commands=['start', 'hello', 'Привет'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, этот бот поможет тебе придумать надежный пароль!')
    bot.send_message(message.chat.id, f'Для начала введите количество символов в пароле.')

@bot.message_handler()
def info(message):
    try:
        password_length = int(message.text)
        password = generate_password(password_length)
        bot.send_message(message.chat.id,
                         f'Пароль сгенерирован: '
                         f'{password}'
                         )
        bot.send_message(message.chat.id,
                         f'Для генерации еще одного просто введите чило - длину пароля! Желаем вам всео самого лучшего, Дорогой пользователь'
                         )

    except ValueError:
        return bot.send_message(message.chat.id, f'Введите только число для генерации пароля!')

bot.polling(none_stop=True)
