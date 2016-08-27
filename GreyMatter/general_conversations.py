import random
from SenseCells.tts import tts

def who_are_you():
    messages = ['I am Melissa, your lovely personal assistant.',
                'Melissa, didnt I tell you before?',
                'You ask that so many times! I am Melissa.']
    #messages = ['Soy Melissa, tu asistente personal, ya no te acuerdas?']
    tts(random.choice(messages))

def how_am_i():
    replies =['You are goddamn handsome!', 'My knees go weak when I see you.',
              'You are sexy!', 'You look like the kindest person that I have met.']
    tts(random.choice(replies))

def tell_joke():
    jokes = ['What happens to a frogs car when it breaks down? It gets toad away.',
             'Why was six scared of seven? Because seven ate nine.', 'No, I always forget the punch line.']
    tts(random.choice(jokes))

def who_am_i(name):
    tts('You are ' + name + ', a brilliant person. I love you!')

def where_born():
    tts('I was created by a magician named Manu, in Guadalix de la Sierra, the magical land of magic.')

def how_are_you():
    tts('I am fine, thank you.')

#def como_estas():
#    tts('Estoy muy bien, gracias por preguntar.')

#def quien_eres():
#    tts('Soy Melissa, tu asistente personal, ya no te acuerdas?')

def undefined():
    tts('I dont know what that means!')
    #tts('La verdad es que no se que me has preguntado.')
    #tts('Lo siento' + name + ', la verdad es que no tengo respuesta para tu pregunta.')

