<?php

/* BUCLE WHILE
        while(condicion){
 *          bloque de instrucciones
 *      }
 */
$numero=0;
while($numero <= 100){
    echo $numero.", ";
    $numero++;
}
//Tabla de multiplicar

if(isset($_GET['numero'])){
    //Casteo de la variable (Cambio de tipo)
    $numero= (int)$_GET['numero'];     
}else{
    $numero=1;
}
echo "<h1>Tabla de multiplicar del número $numero</h1>";
$contador=0;
while($contador<=10){
    echo "$numero x $contador = ".($numero*$contador)."<br/>";
    $contador++;
}
echo "<hr/>";
//Do while
/*
do{
    //Bloque de instrucciones
}while{condicion}
*/
$edad=18;
$counter=1;
do{
echo "Tienes acceso al local privado $counter <br>";
$counter++;
}while($edad >=18 && $counter <=10);