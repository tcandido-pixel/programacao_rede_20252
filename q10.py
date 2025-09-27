import os

patch = "c:\\temp\\"

nome_pasta = input("digite o nome da pasta: ")

os.mkdir(f"{patch}{nome_pasta}")
os.mkdir(patch + nome_pasta)