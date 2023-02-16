#NO MODIFICAR ESTE ARCHIVO

import Practica01;
import pytest;

    
def test_compararNumeros_1():
    assert Practica01.compararNumeros(20, 10) == True
    
def test_compararNumeros_2():
    assert Practica01.compararNumeros(10, 10) == False
    
def test_compararNumeros_3():
    assert Practica01.compararNumeros(10, 100) == False
    
def test_compararNumeros_1():
    assert isinstance(Practica01.compararNumeros(-10, 10), str) == isinstance("Error: El número debe ser mayor a CERO", str)    
