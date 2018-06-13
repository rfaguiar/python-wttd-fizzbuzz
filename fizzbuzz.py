"""

Jogo FizzBuzz

Quando o número for multiplo de 3, fala fizz;
Quando o número for multiplo de 5, fala buzz;
Quando o número for multiplo de 3 e 5, fala fizzbuzz;
Para os demais diga o próprio número;

"""
from functools import partial

multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)


def robot(pos):
    say = str(pos)

    if multiple_of_3(pos) and multiple_of_5(pos):
        say = 'fizzbuzz'
    elif multiple_of_5(pos):
        say = 'buzz'
    elif multiple_of_3(pos):
        say = 'fizz'

    return say
