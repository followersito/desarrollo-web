<?php

/** BUCLE FOR
    for(variable contador, condicion, modificacion contador){
       BLOQUE DE INSTRUCCIONES
     }
 */
$resultado=0;
for($i=0;$i<=100;$i++){
    //$resultado=$resultado+$i;
    $resultado+=$i;
    echo 'El resultado es: '.$resultado.'<br>';
}

//Ejemplo de tabla de multiplicar
if(isset($_GET['numero'])){
    //Casteo de la variable (Cambio de tipo)
    $numero= (int)$_GET['numero'];     
}else{
    $numero=1;
}

echo "<h1>Tabla de multiplicar del número $numero</h1>";
for($contador=1;$contador<=10;$contador++){
    if($numero==45){
        echo "No se pueden mostrar estas operaciones";
        break;
    }
    echo "$numero x $contador = ".($numero*$contador)."<br/>";
}
