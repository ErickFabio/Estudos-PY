# Você foi contratado por uma empresa de tecnologia 
# para desenvolver um programa em Python 
# que calcule o ano de nascimento de uma 
# pessoa com base na idade informada.

# O objetivo é saber a idade e também o ano de nascimento.

# A maquina trabalha da seguinte forma: 1-Entrada 2-Processamento 3-Saída

#Tipos de Variáveis

# a = 1 - número inteiro
# a1 = 4.5 número decímal
# b = "Erick" - texto strings
# c = True - falso ou verdadeiro boleano


ano_atual = 2025
nome = input ("Digite seu nome: ")
idade = int( input ("Digite sua idade: ") ) 

ano_nascimento = ano_atual - idade

print (f"{nome} vc nasceu em {ano_nascimento}")
