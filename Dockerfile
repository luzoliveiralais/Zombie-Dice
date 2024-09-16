# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o conteúdo do diretório local para o diretório de trabalho no container
COPY . /app

# Instale as dependências do jogo (se houver um arquivo requirements.txt)
RUN pip install -r requirements.txt

# Defina o comando de entrada padrão para o container
CMD ["python", "jogo2.py"]

