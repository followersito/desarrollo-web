<?php

/* 
 * EJERCICIO 3
 Escribir un programa que imprima por pantalla los cuadrados
 (numero multiplicado por sí mismo) de los 40 primeros números naturales.
    *PD: Utilizar bucle while
 */
//SOLUCIÓN 1
$num = 0;
while($num<=40){
    echo "El cuadrado de $num es ".($num*$num)."<br>";
    $num++;
}

/* SOLUCIÓN 2
for($num=0;$num<=40;$num++){
    $cuadrado=$num*$num;
    echo "El cuadrado de $num es ".$cuadrado."<br>";
}
*/