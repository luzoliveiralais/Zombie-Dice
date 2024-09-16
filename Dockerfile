# Use uma imagem base oficial do Python
FROM python:3

# Defina o diretório de trabalho
WORKDIR /Zombie-Dice

# Copie os arquivos necessários para o contêiner
COPY . .

# Comando para iniciar a aplicação
CMD ["python", "projeto_final.py"]
