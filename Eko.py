# PROBLEMA EKO - JAIRO ANDRE CALAGUA MALLQUI
# Para leer la entrada
print ('Ingresa tus datos de entrada')  # Los datos de entrada se deben colocar en el roden de los ejemplos del problema
N, M = map(int, input().split())        # N para el numero de arboles y M para los metros de madera
alturas_arboles = list(map(int, input().split()))

# Implemento una función para verificar si la hoja de la sierra a la altura H cumple con la cantidad de madera requerida
def cumple_madera(H):
    madera_cortada = 0
    for altura in alturas_arboles:
        if altura > H:
            madera_cortada += altura - H
    return madera_cortada >= M

# Se realiza una búsqueda binaria para encontrar la altura máxima de la hoja de sierra
izquierda, derecha = 0, max(alturas_arboles)
while izquierda < derecha:
    mitad = (izquierda + derecha + 1) // 2
    if cumple_madera(mitad):
        izquierda = mitad
    else:
        derecha = mitad - 1

# Finalmente se muestra la altura máxima de la hoja de sierra
print ('Resultado de la muestra')
print(izquierda)