# sdn-projects

El script de python imprime la respuesta de la solicitud de la api de meraki donde presenta las organizaciones donde el usuario tiene privilegios
primero selecciona los dispositivos de tipo wireless y appliance y luego los imprime en un archivo csv de la forma por ejemplo:

name,Vegas Living Room MR84

serial,Q2EK-3UBE-RRUY

mac,e0:55:3d:10:5a:ca

model,MR84

lanIp,192.168.0.20

para eso hace una Request en HTTP y revisa el estado de raise_for_status() para manejo de errores.
luego que recibe la respuesta imprime en consola un arreglo de objeto con todas las organizaciones.
Finalmente hace otro request en HHTP a la organizacion DeLab donde filtra todos los dispositivos por el tipo "wireless" o "appliance" y los guarda en un arreglo de diccionarios en python. este arreglo se imprime en un archivo csv.
