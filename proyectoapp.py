import requests
import json
import os

ARCHIVO = "historial.json"

# -------------------------
# Cargar o crear historial
# -------------------------
def cargar_historial():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w") as f:
            json.dump([], f, indent=4)
    with open(ARCHIVO, "r") as f:
        return json.load(f)

# -------------------------
# Guardar en historial
# -------------------------
def guardar_historial(registro):
    historial = cargar_historial()
    historial.append(registro)
    with open(ARCHIVO, "w") as f:
        json.dump(historial, f, indent=4)

# -------------------------
# Consultar IP en ip-api
# -------------------------
def consultar_ip(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,message,query,country,countryCode,continent,continentCode,as,asname"
    
    r = requests.get(url)
    data = r.json()

    if data.get("status") != "success":
        print("\nError:", data.get("message"))
        return None

    resultado = {
        "ip": data.get("query"),
        "asn": data.get("as"),
        "as_name": data.get("asname"),
        "country_code": data.get("countryCode"),
        "country": data.get("country"),
        "continent_code": data.get("continentCode"),
        "continent": data.get("continent")
    }

    return resultado

# -------------------------
# Mostrar historial
# -------------------------
def mostrar_historial():
    historial = cargar_historial()

    if not historial:
        print("\nNo hay IPs registradas.")
        return

    print("\nIPs registradas:")
    for item in historial:
        print(f"- {item['ip']} ({item['country']}, {item['asn']})")

# -------------------------
# Menú principal
# -------------------------
while True:
    print("\n==============================")
    print("      MENU DE GEO IP          ")
    print("==============================")
    print("1. Consultar una IP")
    print("2. Ver historial de IPs")
    print("3. Salir")
    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        ip = input("\nIngresa la IP a consultar: ")
        resultado = consultar_ip(ip)
        if resultado:
            print("\nResultado:")
            print(json.dumps(resultado, indent=4))
            guardar_historial(resultado)
            print("\nConsulta guardada en historial.json")

    elif opcion == "2":
        mostrar_historial()

    elif opcion == "3":
        print("\nFin del programa.")
        break

    else:
        print("\nOpción no válida. Intenta otra vez.")
