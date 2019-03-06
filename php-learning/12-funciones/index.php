<?php

/* 
FUNCIÓN:
 * function nombreDeLaFuncion($parametro){
 *      //BLOQUE DE INSTRUCCIONES
 * }
 * PARA LLAMARLA:
 * nombreDeLaFuncion($parametro);
 */
//Ejemplo 1

function muestraNombres(){
    echo "Hector<br>";
    echo "David<br>";
    echo "Katherine<br>";
    echo "Josh<br>";
}

//muestraNombres();

//Ejemplo 2
$numero;
function tabla($numero){
    for($contador=0;$contador<=10;$contador++){
        echo "$numero x $contador = ".($contador*$numero)."<br>";
    }
}
tabla(5);