def mostrar_encabezado_escuela():
    print("INSTITUTO X")
print("REGISTRO DE CALIFICACIONES")

def obtener_nota_minima_aprobatoria():
    print("retorna la nota minima aprobatoria para pasar el curso")
    return 6.0

def evaluar_rendimiento(nota_final):
    if nota_final < 7.0:
        return(f"reprobado")
    elif nota_final <= 9.4:
        return(f"aprobado")
    else:

        return(f"excelente")
    
    
def calcular_promedio_ponderado(nota_examenes, nota_tareas):
        calificacion_final =(nota_examenes * 0.70) + (nota_tareas * 0.30)
        return round(calificacion_final, 1)


def generar_boleta(nombre_alumno, nota_examanes, nota_tareas):

 nota_final = calcular_promedio_ponderado(nota_examanes, nota_tareas)
 nota_minima = obtener_nota_minima_aprobatoria()
 estado = evaluar_rendimiento(nota_final)

 print("estudiante:", nombre_alumno)
 print("Calificacion:", nota_final)
 print("estado: ", estado)

 if nota_final < nota_minima:
     print("vas hacer examen extraordinario")
 else:
     print("te salvaste del examen extraordinario")
mostrar_encabezado_escuela()
generar_boleta("juan", 5.5, 6.0)
     