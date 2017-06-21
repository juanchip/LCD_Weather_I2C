#!/bin/bash

echo "Inicializando..."
while true
do
	sleep 5
	echo "matando proceso Run.py"
	pkill -9 python
	echo "Sistema Parado"
	./Ejecutar.sh
	echo "Servicio iniciado"
done
