#diccionario
traductor = {"casa":"house","perro":"dog"}
palabra = ""
while palabra != "0":
    palabra = input("Traducir al inglés: ")
    
    if palabra in traductor:
        print(f"(es) {palabra} : (en) {traductor[palabra]}")
    elif(palabra != "0" and palabra != ""):
        resp = input(f"{palabra} no existe en el diccionario. ¿Desea traducir s/n?")
        if(resp == "s"):
            traduccion = input(f"Ingrese la traduccion en ingles de {palabra}: ")
            if(traduccion != ""):
                traductor[palabra] = traduccion #cargar dict