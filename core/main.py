import random

greeting = [
            "سلام",
            "سلااام",
            "سلام من قراره بهت کمک کنم",
            "درود",
]

feeling = [
   "حالت چطوره؟",
    "چه احساسی داری؟",
    "حال امروزت چطور هست؟"
]

event = [
    "متاسفم که می شنوم حال شما خوب نیست. آیا اتفاق خاصی رخ داده است که این احساس را در شما ایجاد کند؟",
    "آیا اتفاق خاصی افتاده که شما را غمگین کند؟ راحت به من بگویید.",
]

time = [
    "من می توانم با آن شناسایی کنم. حال آیا این احساسات حاصل اتفاقی است که اخیراً رخ داده یا مدت ها پیش؟",
    "آیا می توانید به من بگویید که آیا این احساسات خاص ناشی از رویدادی است که اخیراً رخ داده است یا مدت زمان طولانی تری؟",
]

protocol = [
    "1: یادآوری خاطرات دوران کودکی\nدر یک مکان آرام، به عکس های شاد و ناخوش خود نگاه کنید. خاطرات مثبت و منفی دوران کودکی و روابط اولیه در خانواده را به یاد آورید."
]
def information_retrieval_module(state):
    if state == 0: # Greeting
        return random.choice(greeting)
    elif state == 1: # Feeling
        return random.choice(feeling)
    elif state == 2:
        return random.choice(event)
    elif state == 3:
        return random.choice(time)
    elif state == 4:
        return random.choice(protocol)
    return

def user_input(state):
    if state == 0: # Greeting
        return input()
    elif state == 1: # Feeling
        return input()
    elif state == 2:
        return input()
    elif state == 3:
        print("۱. آره تازه بوده")
        print("۲. نه برای خیلی وقت پیشه.")
        return input("شماره ۱ یا ۲ رو وارد کنید.\n")
    elif state == 4:
        return
    return

