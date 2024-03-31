import random
import time

import telebot
from telebot import types
import requests

bot = telebot.TeleBot('6995455008:AAFs5JpTob1Xg7LBWRjh6g8fyu6VfytzIMA')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Приветствую тебя в самом случшем онлайн казино, <b>{message.from_user.first_name} </b>! Основные команды: /help'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['help'])
def start(message):
    mess = (f'Команды для запуска игр: /cube_val - угадать значение кубика. значение указыввать через пробел. /cube_parity'
            f' - угадать четность кубика, значения указывать через пробел(чет/нечет). /target - мишень. /football - '
            f'футбольный мячик. /basketball - баскетбольный мяч')
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['cube_val'])
def start(message):
    message1 = str(message.text).split()
    if len(message1) != 1 and len(message1) <= 2:
        if message1[1].isnumeric():
            if int(message1[1]) > 0 and int(message1[1]) <= 6:
                emoji = '🎲'
                a = bot.send_dice(message.chat.id, emoji)
                time.sleep(4)
                bot.send_message(message.chat.id, 'Вы победили!' if int(message1[1]) == int(a.dice.value) else 'ЛОХ')


@bot.message_handler(commands=['cube_parity'])
def start(message):
    message1 = str(message.text).split()
    if len(message1) != 1 and len(message1) <= 2:
        if message1[1].isalpha():
            if (message1[1].lower() == 'чёт' or message1[1].lower() == 'чет' or message1[1].lower() == 'четное' or message1[1].lower() == 'чётное'
                    or message1[1].lower() == 'нечёт' or message1[1].lower() == 'нечет' or message1[1].lower() == 'нечетное'
                    or message1[1].lower() == 'нечётное' or message1[1] == 'чет' or message1[1] == 'чёт' or message1[1] == 'чётное' or message1[1] == 'четное'
                    or message1[1] == 'нечет' or message1[1] == 'нечёт' or message1[1] == 'нечётное' or message1[1] == 'нечетное'):
                emoji = '🎲'
                a = bot.send_dice(message.chat.id, emoji)
                time.sleep(4)

                if (message1[1].lower() == 'нечёт' or message1[1].lower() == 'нечет' or message1[1].lower() == 'нечетное'
                      or message1[1].lower() == 'нечётное' and int(a.dice.value) % 2 != 1):
                    bot.send_message(message.chat.id, 'Вы проиграли!')

                elif (message1[1].lower() == 'чёт' or message1[1].lower() == 'чет' or message1[1].lower() == 'четное'
                        or message1[1].lower() == 'чётное' and int(a.dice.value) % 2 != 0):
                    bot.send_message(message.chat.id, "Вы проиграли!")

                else:
                    if (message1[1].lower() == 'чёт' or message1[1].lower() == 'чет' or message1[1].lower() == 'четное'
                            or message1[1].lower() == 'чётное' and int(a.dice.value) % 2 == 0):
                        bot.send_message(message.chat.id, 'Вы победили!')

                    elif (message1[1].lower() == 'нечёт' or message1[1].lower() == 'нечет' or message1[
                        1].lower() == 'нечетное'
                          or message1[1].lower() == 'нечётное' and int(a.dice.value) % 2 == 1):
                        bot.send_message(message.chat.id, 'Вы победили!')


@bot.message_handler(commands=['target'])
def start(message):
    message1 = str(message.text).split()
    emoji = '🎯'
    a = bot.send_dice(message.chat.id, emoji)
    time.sleep(4)
    bot.send_message(message.chat.id, a.dice.value)
    if int(a.dice.value) == 1:
        bot.send_message(message.chat.id, 'Вы проиграли!')
    elif int(a.dice.value) == 2:
        bot.send_message(message.chat.id, 'Вы победили! Коэффицент выигрыша равен 1.05')
    elif int(a.dice.value) == 3:
        bot.send_message(message.chat.id, 'Вы победили! Коэффицент выигрыша равен 1.1')
    elif int(a.dice.value) == 4:
        bot.send_message(message.chat.id, 'Вы победили! Коэффицент выигрыша равен 1.15')
    elif int(a.dice.value) == 5:
        bot.send_message(message.chat.id, 'Вы победили! Коэффицент выигрыша равен 1.2')
    elif int(a.dice.value) == 6:
        bot.send_message(message.chat.id, 'Вы победили! Коэффицент выигрыша равен 1.25')

    #bot.send_message(message.chat.id, 'Вы победили!' if int(message1[1]) == int(a.dice.value) else 'ЛОХ')

@bot.message_handler(commands=['football'])
def start(message):
    message1 = str(message.text).split()
    emoji = '⚽'
    a = bot.send_dice(message.chat.id, emoji)
    bot.send_message(message.chat.id, a.dice.value)
    time.sleep(2)
    bot.send_message(message.chat.id, 'Проверка...')
    time.sleep(3)
    if int(a.dice.value) == 1:
        bot.send_message(message.chat.id, 'Вы проиграли!')
    elif int(a.dice.value) == 2:
        bot.send_message(message.chat.id, 'Вы победили! Коэффицент выигрыша равен 1.2')
    elif int(a.dice.value) == 3:
        bot.send_message(message.chat.id, 'Вы победили! Коэффицент выигрыша равен 1.2')
    elif int(a.dice.value) == 4:
        bot.send_message(message.chat.id, 'Вы победили! Коэффицент выигрыша равен 1.2')
    elif int(a.dice.value) == 5:
        bot.send_message(message.chat.id, 'Вы победили! Коэффицент выигрыша равен 1.2')
    elif int(a.dice.value) == 6:
        bot.send_message(message.chat.id, 'Вы победили! Коэффицент выигрыша равен 1.2')

@bot.message_handler(commands=['basketball'])
def start(message):
    message1 = str(message.text).split()
    emoji = '🏀'
    a = bot.send_dice(message.chat.id, emoji)
    bot.send_message(message.chat.id, a.dice.value)
    time.sleep(2)
    bot.send_message(message.chat.id, 'Проверка...')
    time.sleep(3)
    if int(a.dice.value) == 1:
        bot.send_message(message.chat.id, 'Вы проиграли!')
    elif int(a.dice.value) == 2:
        bot.send_message(message.chat.id, 'Вы проиграли!')
    elif int(a.dice.value) == 3:
        bot.send_message(message.chat.id, 'Вы проиграли!')
    elif int(a.dice.value) == 4:
        bot.send_message(message.chat.id, 'Вы победили! Коэффицент выигрыша равен 1.3')
    elif int(a.dice.value) == 5:
        bot.send_message(message.chat.id, 'Вы победили! Коэффицент выигрыша равен 1.3')
    elif int(a.dice.value) == 6:
        bot.send_message(message.chat.id, 'Вы победили! Коэффицент выигрыша равен 1.3')

@bot.message_handler(commands=['ruletka'])
def start(message):
    message1 = str(message.text).split()
    emoji = '🎰'
    a = bot.send_dice(message.chat.id, emoji)
    bot.send_message(message.chat.id, 'В разработке...')


bot.polling(none_stop=True)