import random
import string
def generatePassword(stringLength=16):
    """Generar una contraseña aleatoria de entre 4 y 16 caracteres con minúsculas, mayúsculas, números y caracteres especiales """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))
print("Generar una contraseña aleatoria de entre 4 y 16 caracteres con minúsculas, mayúsculas, números y caracteres especiales ")
print ("Password aleatorio: ", generatePassword() )
print ("Password maximo 16:", generatePassword(16) )
print ("Password minimo 4:", generatePassword(4) )

