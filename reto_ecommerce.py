productos = [
    {"id": 1, "nombre": "Laptop Pro 14", "categoria": "Computo", "precio": 25000, "descuento": 0.10, "stock": 5},
    {"id": 2, "nombre": "Mouse Gamer X", "categoria": "Accesorios", "precio": 1200, "descuento": 0.15, "stock": 20},
    {"id": 3, "nombre": "Teclado Mecánico K1", "categoria": "Accesorios", "precio": 2200, "descuento": 0.05, "stock": 10},
    {"id": 4, "nombre": "Monitor 27'' 4K", "categoria": "Computo", "precio": 8000, "descuento": 0.20, "stock": 7},
    {"id": 5, "nombre": "Audífonos Bluetooth Z", "categoria": "Audio", "precio": 1500, "descuento": 0.0, "stock": 15},
]

ventas = [
    {"venta_id": 101, "producto_id": 1, "cantidad": 1, "cliente": "Ana"},
    {"venta_id": 102, "producto_id": 2, "cantidad": 2, "cliente": "Luis"},
    {"venta_id": 103, "producto_id": 4, "cantidad": 1, "cliente": "Sofía"},
    {"venta_id": 104, "producto_id": 2, "cantidad": 1, "cliente": "Carlos"},
    {"venta_id": 105, "producto_id": 5, "cantidad": 3, "cliente": "Ana"},
]

tienda_info = ("TechieStore", "Santiago", 2025)


# 1. Mensaje de Bienvenida
print(f"Bienvenido a {tienda_info[0]} en {tienda_info[1]} ({tienda_info[1]})")

# 2. Cantidad de productos que existen
print(f"Total de productos: {len(productos)}")

# 3. precio final con descuentos
p1 = productos[0]["precio"] * (1 - productos[0]["descuento"])
p2 = productos[1]["precio"] * (1 - productos[1]["descuento"])
p3 = productos[2]["precio"] * (1 - productos[2]["descuento"])
p4 = productos[3]["precio"] * (1 - productos[3]["descuento"])
p5 = productos[4]["precio"] * (1 - productos[4]["descuento"])

print(f"{productos[0]['nombre']} → ${p1}")
print(f"{productos[1]['nombre']} → ${p2}")
print(f"{productos[2]['nombre']} → ${p3}")
print(f"{productos[3]['nombre']} → ${p4}")
print(f"{productos[4]['nombre']} → ${p5}")

#4 total de cada venta sin loops
v101 = p1 * ventas[0]["cantidad"]
v102 = p2 * ventas[1]["cantidad"]
v103 = p4 * ventas[2]["cantidad"]
v104 = p2 * ventas[3]["cantidad"]
v105 = p5 * ventas[4]["cantidad"]

print(f"Venta {ventas[0]['venta_id']}: {ventas[0]['cliente']} compró {ventas[0]['cantidad']} {productos[0]['nombre']} y pagó {v101}")
print(f"Venta {ventas[1]['venta_id']}: {ventas[1]['cliente']} compró {ventas[1]['cantidad']} {productos[1]['nombre']} y pagó {v102}")
print(f"Venta {ventas[2]['venta_id']}: {ventas[2]['cliente']} compró {ventas[2]['cantidad']} {productos[3]['nombre']} y pagó {v103}")
print(f"Venta {ventas[3]['venta_id']}: {ventas[3]['cliente']} compró {ventas[3]['cantidad']} {productos[1]['nombre']} y pagó {v104}")
print(f"Venta {ventas[4]['venta_id']}: {ventas[4]['cliente']} compró {ventas[4]['cantidad']} {productos[4]['nombre']} y pagó {v105}")

#5 ingreso total 
ingreso_total = v101 + v102 + v103 + v104 + v105
print(f"Ingreso total: {ingreso_total}")