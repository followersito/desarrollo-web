<?php

/* Sacar todos los números pares del 1 al 100
 
 */

/*  SOLUCIÓN 1
$numero=0;
while($numero<=100){
if(($numero%2)==0){
    echo $numero.'<br>';
}
$numero++;
}
*/

//SOLUCIÓN 2
for($numero=1;$numero<=100;$numero++){
    if(($numero%2)==0){
    echo $numero.'<br>';
    }
}