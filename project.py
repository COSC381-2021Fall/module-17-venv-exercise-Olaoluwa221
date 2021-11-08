import emoji
import art
from art import *
import pyjokes

My_joke = pyjokes.get_joke(language="en", category="neutral")
print(My_joke)
Art = text2art("Jokes", font='block', chr_ignore=True)
print(Art)
print(emoji.emojize(":grinning_face_with_big_eyes:"))