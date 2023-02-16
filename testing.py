#NO MODIFICAR ESTE ARCHIVO

import Practica01;
import pytest;

    
def test_presupuestoEvento_1():
    assert Practica01.presupuestoEvento(20) == 150000
    
def test_presupuestoEvento_2():
    assert Practica01.presupuestoEvento(5) == 47500
    
def test_presupuestoEvento_3():
    assert Practica01.presupuestoEvento(2) == 19000
    
def test_presupuestoEvento_1():
    assert isinstance(Practica01.presupuestoEvento(-10), str) == isinstance("Error: El número debe ser mayor a CERO", str)    
