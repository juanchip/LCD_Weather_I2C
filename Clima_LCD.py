# -*- coding: utf-8 -*-
import time
import pyowm        #modulo utilizado para obtener el clima
from pyowm import OWM


try:
    while True:    
        #print("Obteniendo data")
       # display.lcd_display_string("Actualizando",1);
       # display.lcd_display_string("Informacion",2);
        owm_es = OWM(language='es')
        Pais = ',Arg'
        API_key = 'APIKEY_Aqui'
        owm = OWM(API_key)
        apikey = owm.get_API_key()
        #print 'Key Utilizada->' + owm.get_API_key()
       # display.lcd_clear()
        owm.set_API_key(API_key)
        observation = owm.weather_at_place('Buenos Aires' + Pais)
        w = observation.get_weather()
        presion = str(w.get_pressure())
        presionseparada = presion.split(':')
        presA = presionseparada[1]
        PresF = presA.split(',')
        temperatura = str(w.get_temperature('celsius'))
        temperaturaSeparada = temperatura.split(':')
        TempA = temperaturaSeparada[3]
        TempF = TempA.split(',')
        humedad = w.get_humidity()
        #FechaFormato = str(datetime.datetime.now().date())
        #Fecha = FechaFormato.split('-')
       # print TempF[0]
        #print PresF[0]
        display.lcd_display_string("Temp"+ TempF[0]+'C'+" Hum " + str(humedad)+ '%', 1)
        display.lcd_display_string('Pres ' + PresF[0] +' hPa',2)
        display.lcd_display_string('Fech  '+Fecha[2]+'-'+Fecha[1]+'-'+Fecha[0],3);
                           
        count = 0                
        while (count < 3125):  #espera 5 minutos
            display.lcd_display_string('Hora '+str(datetime.datetime.now().time()), 4)
            count = count + 1
            
        display.lcd_clear()    
except KeyboardInterrupt: 
    print("Vaciando")
    display.lcd_clear()
