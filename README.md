# TFTP
Implementación de un cliente y un servidor TFTP en Python, haciendo uso de sockets.

## Cliente
Cliente TFTP parcial. Implementa la opción de bajar un fichero (RRQ).
### Uso
```bash
tftp_cli_rrq.py <server> <filename>
```

## Servidor
Servidor TFTP parcial. Implementa la opción de bajar un fichero (RRQ).
### Características
- Da posibilidad de transferir ficheros de cualquier tamaño, gestionando adecuadamente el
identificador de los bloques de datos.
- Da la posibilidad de atender concurrentemente a varios clientes, creando para ello un
proceso hijo para cada cliente.
- Gestiona la pérdida de paquetes, utilizando para ello un temporizador y, si es nececario,
volviendo a retransmitir el paquete perdido.
### Configuración
En las primeras lineas de código de debe indicar el puerto por el que estará disponible y la ruta de la carpeta donde se alojarán los ficheros para descargar.
```python
PORT = 69
BLOCK_SIZE = 512
FILES_PATH ='./data/'
```
### Uso
```bash
python3 tftp_ser_rrq_mejorado.py
```
