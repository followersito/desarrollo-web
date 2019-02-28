<?php
/**
 * CONDICIONALES 
 * IF:
    if(condicion){
        instrucciones
   }
    else{
        otras instrucciones
   }
 */
$color ="azul";
if($color=="rojo"){
    echo "El color es rojo";
}
else{
    echo "El color no es rojo, es ".$color.'<br>';
}

/**
 * OPERADORES DE CONDICION
   ==   igual
   ===  identico    (mismo tipo de dato)
   !=   distinto
   !==  no identico
 */

$year=2020;
if($year!=2019){
    echo 'Estamos en un año distinto a 2019'.'<br>';
}
else{
    echo 'Estamos en 2019'.'<br>';
}

$nombre = 'Ivan';
$edad=19;
$pais='Guatemala';
$continente='América';
define('mayoria_edad',18);

if($edad>=mayoria_edad){
    echo $nombre.' es mayor de edad <br>';
    echo 'Y es de '.$pais;
    if($continente=="América"){
        echo ' que está en '.$continente.'<br>';
    }
    else{
        echo $pais.' no está en América';
    }
}
else{
    echo $nombre.' no cumple la mayoría de edad, aún tiene '.$edad.' años. <br>'
;
    
}
?>