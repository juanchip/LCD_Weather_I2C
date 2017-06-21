#!/bin/bash
if [ "$(id -u)" != "0" ]; then
        echo "Por favor, ejecutar con SUDO!."
	exit 1
fi

apt-get update
apt-get install python-smbus -y
echo "By TheRaspberryPiGuy & Collaborators"
echo "traducido y mejorado por Juanchip"
echo "Instalando SMBUS de Python"
revision=`python -c "import RPi.GPIO as GPIO; print GPIO.RPI_REVISION"`

if [ $revision = "1" ]
then
echo "I2C Pins detectectados como 0"
cp installConfigs/i2c_lib_0.py ./i2c_lib.py
else
echo "I2C Pins detectectados com 1"
cp installConfigs/i2c_lib_1.py ./i2c_lib.py
fi
echo "Configuración de biblioteca I2C para esta RPi, si cambia la revisión sería necesaria una modificación de i2c_lib.py"
echo "Ahora añadiendo módulos y sobrescribiendo la lista negra. Esto permitirá manejar el I2C"
cp installConfigs/modules /etc/
cp installConfigs/raspi-blacklist.conf /etc/modprobe.d/
printf "dtparam=i2c_arm=1\n" >> /boot/config.txt


echo "Ya debería estar todo,presioná una tecla para reiniciar, luego, ejecuta"
echo "'./ej2.sh' desde este directorio"
read -n1 -s
sudo reboot
