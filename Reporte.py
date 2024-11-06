class ReporteSB:
    def __init__(self):
        self.movimientos = []
    def registrar_movimientoSB(self, producto, importe, vuelto):
        self.movimientos.append({
            "producto": producto["nombre"],
            "precio": producto["precio"],
            "importe": importe,
            "vuelto": vuelto
        })
    def mostrar_reporteSB(self):
        print("\n" + "="*60)
        print("||               Resumen de operaciones               ||")
        print("="*60)
        print("||   Producto   ||  Precio  ||  Importe  ||     Vuelto      ||")
        print("="*60)
        # Mostrar cada movimiento en formato de tabla
        for movimiento in self.movimientos:
            producto = movimiento["producto"]
            precio = f"S/. {movimiento['precio']:.2f}"
            importe = f"S/. {movimiento['importe']:.2f}"
            vuelto = movimiento["vuelto"] if movimiento["vuelto"] else "No hubo vuelto"
            print(f"||   {producto:<10} ||  {precio:<8} || {importe:<8} || {vuelto:<15} ||")
        print("="*60)
