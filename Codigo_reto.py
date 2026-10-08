# Reto #2 PROGRAMACION (ALEJANDRO ARCILA RUA / GABRIELA GALINDO HERRERA)

# Sistema de mantenimiento de aeronaves - Aerolínea regional

# Aclaraciones previas:
# Lista de aeronaves (cada aeronave es un diccionario) - Cada componente es un diccionario - Se parte de unas listas con misma cantidad de elementos para
# realizar los diccionarios posteriores.
#Conceptos nuevos usados para explicación a Henry: "Key": int() para que sea un entero el valor adjuntado -------
# "variable".isdigit() Evalua si es un digito y arroja booleano

aeronaves = []

# Nombres y límites de los 5 componentes de cada aeronave
nombres_componentes = ["Motor izquierdo", "Motor derecho", "Flaps",
                       "Turbina de alta presión", "filtros de aceite"]
limites_componentes = [5000, 5000, 3000, 8000, 500]

# Datos de las 3 aeronaves iniciales
matriculas_iniciales = ["HK-4532", "HK-1180", "HK-7721"]
modelos_iniciales = ["A320", "ATR72", "B747"]

# Modulo de creación de componentes y aeronaves en base a las listas anteriores
for i in range(3):
    lista_componentes = []
    for j in range(5):
        componente = {
            "nombre": nombres_componentes[j],
            "horas_uso": 0,
            "limite": limites_componentes[j]
        }
        lista_componentes.append(componente)

    aeronave = {
        "matricula": matriculas_iniciales[i],
        "modelo": modelos_iniciales[i],
        "horas_vuelo": 0,
        "componentes": lista_componentes
    }
    aeronaves.append(aeronave)

# MENÚ PRINCIPAL (Lo que se vera para el "user")

opcion = ""

while opcion != "0":
    print("\n===== MANTENIMIENTO DE AERONAVES =====")
    print("1. Registrar aeronave")
    print("2. Registrar componente")
    print("3. Registrar horas de vuelo")
    print("4. Cambiar componente (reiniciar acumulador)")
    print("5. Reporte de mantenimiento")
    print("6. Ver aeronaves inscritas")
    print("7. Ver listas (print directo)")
    print("0. Salir")
    opcion = input("Elija una opción: ")

    # Registro de aeronave (Opcion 1.)
    if opcion == "1":
        print("\n--- Registrar aeronave ---")
        matricula = input("Matrícula: ").upper()

        #En caso de que el avion no exista
        existe = False
        for aeronave in aeronaves:
            if aeronave["matricula"] == matricula:
                existe = True

        if existe == True:
            print("Esa matrícula ya está registrada.")
        else:
            modelo = input("Modelo: ").upper()
            horas = input("Horas de vuelo acumuladas: ")

            if horas.isdigit():
                nueva = {
                    "matricula": matricula,
                    "modelo": modelo,
                    "horas_vuelo": int(horas),
                    "componentes": []
                }
                aeronaves.append(nueva)
                print("Aeronave registrada.")
            else:
                print("Las horas deben ser un número entero.")

    # Registro de componente (Opción 2.)
    elif opcion == "2":
        print("\n--- Registrar componente ---")
        matricula = input("Matrícula de la aeronave: ").upper()

        encontrada = None
        for aeronave in aeronaves:
            if aeronave["matricula"] == matricula:
                encontrada = aeronave

        if encontrada == None:
            print("No existe esa aeronave.")
        else:
            nombre = input("Nombre del componente: ")
            horas_uso = input("Horas de uso actuales: ")
            limite = input("Límite de horas antes del mantenimiento: ")

            if horas_uso.isdigit() and limite.isdigit():
                componente = {
                    "nombre": nombre,
                    "horas_uso": int(horas_uso),
                    "limite": int(limite)
                }
                encontrada["componentes"].append(componente)
                print("Componente registrado.")
            else:
                print("Las horas y el límite deben ser números enteros.")

    # Registro de horas de vuelo (Opción 3.)
    elif opcion == "3":
        print("\n--- Registrar horas de vuelo ---")
        matricula = input("Matrícula de la aeronave: ").upper()

        encontrada = None
        for aeronave in aeronaves:
            if aeronave["matricula"] == matricula:
                encontrada = aeronave

        if encontrada == None:
            print("No existe esa aeronave.")
        else:
            #Se revisa si algún componente ya superó su límite para no permitir el vuelo del avion
            puede_volar = True
            for componente in encontrada["componentes"]:
                if componente["horas_uso"] >= componente["limite"]:
                    puede_volar = False
                    print("Componente vencido:", componente["nombre"])

            if puede_volar == False:
                print("VUELO NO PERMITIDO. Cambie los componentes vencidos.")
            else:
                horas = input("Horas del vuelo a registrar: ")

                if horas.isdigit():
                    horas = int(horas)
                    encontrada["horas_vuelo"] = encontrada["horas_vuelo"] + horas

                    # Se suman las horas a cada componente (acumulador)
                    for componente in encontrada["componentes"]:
                        componente["horas_uso"] = componente["horas_uso"] + horas

                    print("Vuelo registrado.")

                    #En caso de que el avión quede en tierra posterior al vuelo registrado
                    for componente in encontrada["componentes"]:
                        if componente["horas_uso"] >= componente["limite"]:
                            print("ATENCIÓN:", componente["nombre"], "superó su límite.")
                else:
                    print("Las horas deben ser un número entero.")

    # Cambiar componente (opcion 4.)
    elif opcion == "4":
        print("\n--- Cambiar componente ---")
        matricula = input("Matrícula de la aeronave: ").upper()

        encontrada = None
        for aeronave in aeronaves:
            if aeronave["matricula"] == matricula:
                encontrada = aeronave

        if encontrada == None:
            print("No existe esa aeronave.")
        else:
            # Mostramos los componentes numerados
            numero = 1
            for componente in encontrada["componentes"]:
                print(numero, "-", componente["nombre"])
                numero = numero + 1

            eleccion = input("Número del componente a cambiar: ")

            if eleccion.isdigit() and int(eleccion) >= 1 and int(eleccion) <= len(encontrada["componentes"]):
                posicion = int(eleccion) - 1
                encontrada["componentes"][posicion]["horas_uso"] = 0
                print("Componente cambiado. el valor de sus horas de vuelo se ha reiniciado a 0.")
            else:
                print("Número de componente no válido.")

    # Reporte de mantenimiento (Opcion 5.)
    elif opcion == "5":
        print("\n--- Reporte de mantenimiento inmediato ---")
        hay_pendientes = False

        for aeronave in aeronaves:
            titulo_impreso = False
            for componente in aeronave["componentes"]:
                if componente["horas_uso"] >= componente["limite"]:
                    hay_pendientes = True
                    if titulo_impreso == False:
                        print("Aeronave", aeronave["matricula"], "(" + aeronave["modelo"] + ")")
                        titulo_impreso = True
                    print("  -", componente["nombre"], ":",
                          componente["horas_uso"], "h de", componente["limite"], "h")

        if hay_pendientes == False:
            print("Ningún componente ha superado su límite.")

    # Listado de aeronaves inscritas (Opción 6.)
    elif opcion == "6":
        print("\n" + "=" * 60)
        print("            AERONAVES INSCRITAS EN EL SISTEMA")
        print("=" * 60)

        if len(aeronaves) == 0:
            print("No hay aeronaves registradas.")

        for aeronave in aeronaves:
            print("\n" + "-" * 60)
            print("  Matrícula:", aeronave["matricula"])
            print("  Modelo:   ", aeronave["modelo"])
            print("  Horas de vuelo:", aeronave["horas_vuelo"], "h")

            # Estado general de la aeronave
            estado = "OPERATIVA"
            for componente in aeronave["componentes"]:
                if componente["horas_uso"] >= componente["limite"]:
                    estado = "EN TIERRA (mantenimiento)"
            print("  Estado:   ", estado)
            print("-" * 60)

            if len(aeronave["componentes"]) == 0:
                print("  (Sin componentes registrados)")
            else:
                print("  " + "Componente".ljust(24) + "Uso".rjust(8) + "Límite".rjust(9) + "  Estado")
                for componente in aeronave["componentes"]:
                    if componente["horas_uso"] >= componente["limite"]:
                        estado_comp = "VENCIDO"
                    else:
                        estado_comp = "OK"
                    print("  " + componente["nombre"].ljust(24) +
                          str(componente["horas_uso"]).rjust(8) +
                          str(componente["limite"]).rjust(9) +
                          "  " + estado_comp)

        print("\n" + "=" * 60)
        print("Total de aeronaves:", len(aeronaves))

    # visualización de la lista de manera "fea" (Opcion .7)
    elif opcion == "7":
        print("\n--- Lista de aeronaves (datos crudos) ---")
        print(aeronaves)

    # Para salir del sistema (Opcion .0)
    elif opcion == "0":
        print("Saliendo del sistema.")

    else:
        print("Opción no válida.")