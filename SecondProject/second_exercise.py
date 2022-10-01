# 2- Tomando como base la Ventana del ejercicio 2 del TP 1 diseñar lo siguiente
#   a. Apellido y Nombre
#   b. Tipo DNI (permitir seleccionar DNI LE LC CI PAS)
#   c. Nro Doc (Debe tener 8 digitos)
#   d. Fecha Nacimiento (Permitir seleccionar de un combobox mes (nombres) Día (1
#      a 31) el año se ingresa directamente.
#    e. Utilizar alguna ventana Modal si lo cree conveniente.

# this file only store functions for validations

def validate_docNumber (text1, newText1):
    '''
        Simply function for validate length of dni
    '''
    if len (newText1) > 8:
        return False
    return text1.isdecimal()

# function to validate only 4 characters and year less than 2022 in the year field
def validate_year (text2, newText2):
    '''
        Simply function for validate year format
    '''
    if len (newText2) > 4:
        return False
    elif (newText2) > "2022":
        return False
    return text2.isdecimal()