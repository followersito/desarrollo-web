<?php

/**
 * OPERADORES DE CONDICION
 *  ==   igual
 *  ===  identico    (mismo tipo de dato)
 *  !=   distinto
 *  !==  no identico
 * OPERADORES LÓGICOS
 * && AND Y
 * || OR O
 * !  NOT NO
 * AND, OR
 */

$color ="azul";
if($color=="rojo"){
    echo "El color es rojo";
}
else{
    echo "El color no es rojo, es ".$color.'<br>';
}
echo '<hr/>';
$year=2020;
if($year!=2019){
    echo 'Estamos en un año distinto a 2019'.'<br>';
}
else{
    echo 'Estamos en 2019'.'<br>';
}
echo '<hr/>';
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
    echo $nombre.' no cumple la mayoría de edad, aún tiene '.$edad.' años. <br>';   
}
echo '<hr/>';
//Else if ejemplo
$dia=44;

if($dia==1){
    echo 'Es lunes';
}elseif($dia==2){
    echo 'Es martes';
}elseif($dia==3){
    echo 'Es miercoles';
}elseif($dia==4){
    echo 'Es jueves';
}elseif($dia==5){
    echo 'Es viernes';
}else{
    echo 'Es fin de semana'.'<br>';
}
echo '<hr/>';
//Condiciones múltiples
$edad1=18;
$edad2=67;
$edad_oficial=20;

if($edad_oficial>=$edad1  && $edad_oficial <=$edad2){
    echo 'Está en edad de trabajar'.'<br>';
}
else{
    echo 'No puede trabajar'.'<br>';
}
echo '<hr/>';

$pais='Mexico';

if($pais=='Mexico'||$pais=='Colombia'||$pais='España'){
    echo 'En '.$pais.' se habla español'.'<br>';
}else{
    echo 'En '.$pais.'NO se habla español'.'<br>';
}
echo '<hr/>';
switch ($dia){
    case 1:
        echo 'Lunes';
        break;
    case 2:
        echo 'Martes';
        break;
    case 3:
        echo 'Miercoles';
        break;
    case 4:
        echo 'Jueves';
        break;
    case 5:
        echo 'Viernes';
        break;
    default:
        echo 'Es fin de semana';
}

//GOTO
goto ejecuta_aqui;
echo '<h3>Instruccion 1</h3>';
echo '<h3>Instruccion 2</h3>';
echo '<h3>Instruccion 3</h3>';
echo '<h3>Instruccion 4</h3>';

ejecuta_aqui:
    echo '<h1>Me he saltado 4 marcas</h1>';

?>