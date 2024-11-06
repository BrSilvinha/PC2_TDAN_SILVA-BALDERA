from productos import SBProductos
from Reporte import ReporteSB

def mainSB():
    productos = SBProductos()
    reporte = ReporteSB()

    while True:
        # Mostrar menú de productos con formato ASCII
        print("\nSeleccione un producto:")
        print("="*40)
        print(f"| {'#':<3} | {'Producto':<15} | {'Precio (S/)':<15} |")
        print("="*40)
        for i, producto in enumerate(productos.productos, start=1):
            print(f"| {i:<3} | {producto['nombre']:<15} | S/.{producto['precio']:<15} |")
        print("="*40)
        print("[4] Salir")

        # Solicitar selección de producto
        opcion = input("Ingrese el número de la opción: ")
        if opcion == "4":
            break

        # Validar la opción seleccionada
        try:
            opcion = int(opcion) - 1
            producto = productos.obtener_productoSB(opcion)
            if producto is None:
                print("Opción no válida. Intente nuevamente.")
                continue
        except ValueError:
            print("Opción no válida. Intente nuevamente.")
            continue

        # Solicitar el importe de pago
        try:
            importe = float(input("Ingrese el monto con el que pagará: S/."))
        except ValueError:
            print("Monto no válido. Intente nuevamente.")
            continue

        # Realizar el pago y procesar el resultado
        resultado, mensaje = productos.realizar_pagoSB(producto, importe)
        print(mensaje)

        if resultado in ["insuficiente", "exacto"]:
            reporte.registrar_movimientoSB(producto, importe, None)
            break
        elif resultado == "con_vuelto":
            reporte.registrar_movimientoSB(producto, importe, mensaje)
        elif resultado == "sin_monedas":
            reporte.registrar_movimientoSB(producto, importe, "No se pudo dar vuelto")

    # Mostrar reporte al final del programa
    reporte.mostrar_reporteSB()

if __name__ == "__main__":
    mainSB()
