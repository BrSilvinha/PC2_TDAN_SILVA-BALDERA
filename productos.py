class SBProductos:
    productos = [
        {"nombre": "Pepsi", "precio": 2.5},
        {"nombre": "Fanta", "precio": 2.8},
        {"nombre": "Coca-Cola", "precio": 3.2}
    ]
    # Configuración inicial de las monedas
    monedas_disponibles = {
        5.0: 2,
        2.0: 2,
        0.5: 3,
        0.2: 1,
        0.1: 1
    }

    def obtener_productoSB(self, idx):
        if 0 <= idx < len(self.productos):
            return self.productos[idx]
        return None

    def realizar_pagoSB(self, producto, importe):
        precio = producto["precio"]
        # Validación del importe ingresado
        if importe < precio:
            return "insuficiente", "Importe insuficiente. Gracias"
        elif importe == precio:
            return "exacto", "Despachando"
        else:
            vuelto = importe - precio
            detalle_vuelto, exito = self.calcular_vueltoSB(vuelto)
            if exito:
                # Construir el mensaje de vuelto con formato de tabla ASCII
                mensaje_vuelto = " Vuelto:\n"
                mensaje_vuelto += "="*30 + "\n"
                mensaje_vuelto += f"| {'Cantidad':<10} | {'Moneda (S/)':<12} |\n"
                mensaje_vuelto += "="*30 + "\n"
                total_vuelto = 0
                for moneda, cantidad in detalle_vuelto.items():
                    subtotal = moneda * cantidad
                    total_vuelto += subtotal
                    mensaje_vuelto += f"| {cantidad:<10} | S/.{moneda:<10} |\n"
                mensaje_vuelto += "="*30 + "\n"
                mensaje_vuelto += f"| {'Total':<10} | S/.{round(total_vuelto, 2):<10} |\n"
                mensaje_vuelto += "="*30
                return "con_vuelto", mensaje_vuelto
            else:
                # Mensaje cuando no hay suficientes monedas para el cambio
                return "sin_monedas", "Lo sentimos, no contamos con monedas para el vuelto."

    def calcular_vueltoSB(self, vuelto):
        vuelto_dict = {}
        # Intentar dar el vuelto con las monedas disponibles de mayor a menor valor
        for moneda, cantidad in sorted(self.monedas_disponibles.items(), reverse=True):
            while vuelto >= moneda and self.monedas_disponibles[moneda] > 0:
                vuelto = round(vuelto - moneda, 2)
                self.monedas_disponibles[moneda] -= 1
                vuelto_dict[moneda] = vuelto_dict.get(moneda, 0) + 1
        # Comprobar si se pudo dar el vuelto exacto
        if vuelto == 0:
            return vuelto_dict, True
        else:
            # Restablecer las monedas si no se pudo completar el vuelto
            for moneda, cantidad in vuelto_dict.items():
                self.monedas_disponibles[moneda] += cantidad
            return None, False
