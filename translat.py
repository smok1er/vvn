from os import system

try:
    from selenium import webdriver
except:
    system('pip install selenium')
from selenium import webdriver
import telebot
from time import sleep
from telebot import types
from googletrans import Translator

translator = Translator()
idi = 209501902
bot = telebot.TeleBot("1215240244:AAEtopoZty7Y12O_-sf-JA-yLyOqRno-1oE")
driver = webdriver.Chrome('driver/chromedriver.exe')
open('tran.txt', 'a').write('')

@bot.message_handler(commands=['start'])
def key(msg):
    if msg.chat.id == idi:
        admin = types.ReplyKeyboardMarkup()
        akoky = types.KeyboardButton('الاذاعة')
        zkoky = types.KeyboardButton('الاعضاء')
        admin.add(akoky, zkoky)
        bot.reply_to(msg, 'اهلا و سهلا بك ايها المطور {}'.format(msg.from_user.first_name), reply_markup=admin)

    else:
        q = types.InlineKeyboardMarkup()
        q1 = types.InlineKeyboardButton('اضغط هنا \nاذا كان هنالك مصطلح طبي تريد ترجمته', callback_data='q1')
        q.add(q1)
        bot.send_message(msg.chat.id, 'اهلا و سهلا بك في بالبوت الترجمة 💚', reply_markup=q)
        if f'{msg.chat.id}\n' in open('tran.txt', 'r'):
            pass
        else:
            open('tran.txt', 'a').write(f'{msg.chat.id}\n')


@bot.message_handler(content_types='text')
def an(msg):
    try:
        if msg.text == 'الاعضاء' and msg.chat.id == idi:
            x = open('tran.txt', 'r').readlines()
            bot.reply_to(msg, '{}'.format(len(x)))
    except:
        pass
    try:
        if msg.text == 'الاذاعة' and msg.chat.id == idi:
            markup = types.ForceReply(selective=False)
            bot.send_message(msg.chat.id, "ارسل اذاعتك", reply_markup=markup)
    except:
        pass
    try:
        if msg.reply_to_message.text == "ارسل اذاعتك":
            s = msg.text
            x = open('tran.txt', 'r').readlines()
            z = 0
            try:
                while z < len(x):
                    if str(x[z]) == '\n':
                        pass
                    else:
                        bot.send_message(x[z], s)
                    z += 1
            except:
                pass
    except:
        pass
    try:
        bot.delete_message(msg.chat.id, msg.message_id - 1)
        bot.delete_message(msg.chat.id, msg.message_id - 2)
        bot.delete_message(msg.chat.id, msg.message_id - 3)
    except:
        pass
    w = (msg.text).lower()
    try:
        if msg.reply_to_message.text == "ارسل المصطلح الطبي المراد ترجمته":
            if w[0] == 'ا' or w[0] == 'أ' and w[1] == 'ل':
                driver.get(f'https://www.almaany.com/ar/dict/ar-en/{w}/')
                sleep(2)
                j = driver.find_element_by_xpath('//*[@id="meaning"]/div[2]/table[1]').text
                bot.send_message(msg.chat.id, j)

            else:
                try:
                    if f'{w[0]}' in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                                     'q',
                                     'r',
                                     's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                        driver.get(f'https://www.almaany.com/ar/dict/ar-en/{w}/')
                        sleep(2)
                        j = driver.find_element_by_xpath('//*[@id="meaning"]/div[2]/table[1]').text
                        bot.send_message(msg.chat.id, j)

                    else:
                        driver.get(f'https://www.almaany.com/ar/dict/ar-en/ال{w}/')
                        sleep(2)
                        j = driver.find_element_by_xpath('//*[@id="meaning"]/div[2]/table[1]').text
                        bot.send_message(msg.chat.id, j)
                except:
                    pass

    except:
        pass
    if msg.reply_to_message:
        pass
    else:
        try:
            q = types.InlineKeyboardMarkup()
            q1 = types.InlineKeyboardButton('اضغط هنا في حيال وجود مصطلح طبي 💟', callback_data='q1')
            q.add(q1)
            if f'{w[0]}' in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] or f'{w[1]}' in ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                                                                                      'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                                                                      'o', 'p', 'q', 'r', 's', 't', 'u',
                                                                                      'v', 'w', 'x', 'y',
                                                                                      'z'] or f'{w[2]}' in ['a', 'b',
                                                                                                            'c', 'd',
                                                                                                            'e', 'f',
                                                                                                            'g', 'h',
                                                                                                            'i', 'j',
                                                                                                            'k', 'l',
                                                                                                            'm', 'n',
                                                                                                            'o', 'p',
                                                                                                            'q', 'r',
                                                                                                            's', 't',
                                                                                                            'u', 'v',
                                                                                                            'w', 'x',
                                                                                                            'y', 'z']:
                t = str(translator.translate(w, dest='ar'))
                bot.send_message(msg.chat.id, t[t.find('text') + 5:t.find(', pronunciation')], reply_markup=q)
            else:
                t = str(translator.translate(w, dest='en'))
                bot.send_message(msg.chat.id, t[t.find('text') + 5:t.find(', pronunciation')], reply_markup=q)
        except:
            pass


@bot.callback_query_handler(lambda call: True)
def any(call):
    if call.data == 'q1':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.ForceReply(selective=False)
        bot.send_message(call.message.chat.id, "ارسل المصطلح الطبي المراد ترجمته", reply_markup=markup)


bot.polling()

