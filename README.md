# Práctica Básicas en Python

## Descripción general

- Su objetivo está en la resolución de problemas y elementos básicos en Python:
- Uso del condicional IF
- Estructuras con WHILE y FOR
- Validación y restricciones en una función

##  Instrucciones

- El archivo **debe** llamarse **Practica01.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- Deben contruir las funciones con **Python**
- Uso de comentarios (Nombre, Entradas, Salidas y Restricciones)

## presupuestoEvento(numPersonas)
- Construir una función que retorne la cantidad de dígitos que compone el número de parámetro de entrada.
- El parámetro **numPersonas** debe ser entero y mayor a **CERO**
- En el caso que no se cumpla cualquiera de las restricciones, debe mostrar el mesaje de **Error** respectivo

### Explicación del problema
Este algoritmo de calcular el costo de los platillos dependiendo del número de personas a ingresar al restaurante 
- El costo normal del platillo por persona es de ¢9500.
- Si el número de personas es mayor a 5 pero menor o igual a 10, el costo sería ¢8500
- Para más de 11 personas el costo por platillo es de ¢7500. 

``` python
>>> presupuestoEvento(20)
150000
>>> presupuestoEvento(5)
47500
>>> presupuestoEvento(2)
19000
>>> presupuestoEvento(-10)
"Error: El número debe ser mayor a CERO"
```

