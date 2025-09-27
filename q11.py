import os 
path = r"C:\Users\20251144030003\Desktop\ProgramacaoRedes"

arquivos = os.listdir(path)

for arquivo in arquivos:
  if arquivo[-4:] == ".txt":
   print(arquivo)
