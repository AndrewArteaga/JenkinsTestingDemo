#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  File name  :  warmup.py
#  Purpose    :  Warming up to Python with a virtual environment
#  @author    :  Andrew Arteaga, Kevin Patterson, Jimmy Bynre
#  Date       :  2018-09-18
#  Description:  Homework 2 for CMSI-386
#  Notes      :  None
#  Warnings   :  None
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Revision History
#  ================
#     Ver      Date     Modified by:   Reason for change or modification
#    -----  ----------  ------------   ------------------------------------------
#    1.0.0  2018-09-06  Andrew Arteaga created program pushed it to github fixed
#                                      fixed most of the linter errors
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import math
import random
import requests
from cryptography.fernet import Fernet
#1
def change(cents):
    if cents < 0:
        raise ValueError('amount cannot be negative')
    cents_tuple = ()
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1
    quarter_amount = math.floor(cents / quarter)
    dime_amount = math.floor((cents % quarter) / dime)
    nickel_amount = math.floor(((cents % quarter) % dime) / nickel)
    penny_amount = math.floor(((((cents % quarter) % dime) % nickel) / penny))
    cents_tuple = cents_tuple + (quarter_amount, dime_amount, nickel_amount, penny_amount,)
    return cents_tuple
#2
def strip_quotes(quote):
    quote = quote.replace("'", "").replace('"', '')
    return quote
#3
def scramble(random_string):
    fys_string = ''.join(random.sample(random_string, len(random_string)))
    return fys_string
#4
def powers(base, limit):
    consecutive_gen_powers = 0
    i = 0
    while base ** i <= limit:
        consecutive_gen_powers = base ** i
        i += 1
        yield consecutive_gen_powers
#5
def triples(limit):
    py_triples_array = []
    for c_py in range(1, limit + 1):
        for b_py in range(1, c_py):
            for a_py in range(1, b_py):
                if a_py * a_py + b_py * b_py == c_py * c_py:
                    py_triples_array.append((a_py, b_py, c_py))
    return py_triples_array
#6
def say(string=None):
    if string is None:
        return ''
    def string_currier(val=None):
        if val is None:
            return string_currier.string
        string_currier.string += ' ' + val
        return string_currier
    string_currier.string = string
    return string_currier
#7
def interleave(array, *args):
    inter_leaven_array = []
    biggest_input_length = 0
    if len(array) >= len(args):
        biggest_input_length = len(array)
    else:
        biggest_input_length = len(args)
    for i in range(biggest_input_length):
        if i < len(array):
            inter_leaven_array.append(array[i])
        if i < len(args):
            inter_leaven_array.append(args[i])
    return inter_leaven_array
#8
class Cylinder:

    def __init__(self, radius=1, height=1):
        self.radius = radius
        self.height = height
    @property
    def volume(self):
        return math.pi * (self.radius ** 2) * self.height
    @property
    def surface_area(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius ** 2))

    def stretch(self, factor):
        self.height *= factor
        return self

    def widen(self, factor):
        self.radius *= factor
        return self

    def __repr__(self):
        return f'Cylinder with r={self.radius} and h={self.height}'
#9
def make_crypto_functions(fernet_key):
    fernet_key = Fernet.generate_key()
    cryption = Fernet(fernet_key)
    def encrypt(byte_object):
        encrypt_text = cryption.encrypt(byte_object)
        return encrypt_text

    def decrypt(byte_object):
        decrypt_text = cryption.decrypt(byte_object)
        return decrypt_text

    return (encrypt, decrypt)
#10
def random_name(**kwargs):
    param = {'gender': kwargs.get('gender'), 'region': kwargs.get('region'), 'amount':1}
    response = requests.get("http://api.uinames.com", params=param)
    name = response.json()
    if 200 <= response.status_code < 300:
        full_name = name['name'] + ', ' + name['surname']
    else:
        raise ValueError(response.text)
    return full_name
