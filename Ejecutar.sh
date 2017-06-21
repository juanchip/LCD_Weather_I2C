#!/bin/bash

echo "Escribiendo LCD..."


while true
do
	sudo python Clima_LCD.py
	echo "El proceso ha sido interrumpido"
	sleep 2
	echo "Reinicializando"
done

