import random 
import string

class GeradorDeSenha: 
    
    @staticmethod
    def AllCar(tam = 12):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for i in range (tam))
        return senha
    
    @staticmethod
    def OnlyNum(tam = 12):
        caracteres = string.digits
        senha = ''.join(random.choice(caracteres) for i in range (tam))
        return senha
    
    @staticmethod
    def OnlyLetters(tam = 12):
        caracteres = string.ascii_letters
        senha = ''.join(random.choice(caracteres) for i in range (tam))
        return senha
    
    @staticmethod
    def NumAndLetters(tam = 12):
        caracteres = string.ascii_letters + string.digits
        senha = ''.join(random.choice(caracteres) for i in range (tam))
        return senha

TypePass = str(input('''
Escolha o tipo de senha que deseja gerar:
    Qualquer Caractere
    Somente Numeros
    Somente Letras
    Numeros e Letras
                     ''')).strip().lower()

TamanhoSenha = int(input('Digite o tamanho que deseja de sua senha:'))

if TypePass == 'qualquer caractere':
    senha = GeradorDeSenha.AllCar(TamanhoSenha)
elif TypePass == 'somente numeros':
    senha = GeradorDeSenha.OnlyNum(TamanhoSenha)
elif TypePass == 'somente letras':
    senha = GeradorDeSenha.OnlyLetters(TamanhoSenha)
elif TypePass == 'numeros e letras':
    senha = GeradorDeSenha.NumAndLetters(TamanhoSenha)
else:
    senha = "Tipo de senha inválido."

print('Sua nova senha é: ', senha)
