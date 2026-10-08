sensores = ["temperatura", "presion", "luz", "humedad"]

print(sensores)
print(sensores[1])
sensores.append("perro")
print(sensores)
sensores.remove("temperatura")
print(sensores)
sensores[3] = "gato"
print(sensores)
sensores.insert(2,25)
print(sensores)

pines = (17,22,35,23,18)
print(pines)
#pines[0] = 21
print(pines[3])

juan = ("pedro",25.5,False)
print(juan)

sensor = {
    "nombre": "DHT11",
    "pin":4,
    "temperatura":25.5,
    "humedad":60
}

sensor["estado"] = "ok"
print(sensor)
print(sensor["nombre"])
print(sensor["pin"])
print(sensor["temperatura"])
print(sensor["humedad"])

for clave,valor in sensor.items():
    print(clave,":",valor)
