# Usa una imagen base oficial de Python
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requisitos primero para aprovechar la caché de Docker
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de tu código de aplicación
COPY . .

# Comando para ejecutar tu aplicación
CMD ["python", "./app.py"]
