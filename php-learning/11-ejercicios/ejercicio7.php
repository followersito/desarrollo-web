<?php

/* EJERCICIO 5
  Hacer un programa que muestre todos los numeros IMPARES entre dos numeros que nos lleguen por la URL
 */
if (isset($_GET['numero1']) && isset($_GET['numero2'])) {
    $numero1 = $_GET['numero1'];
    $numero2 = $_GET['numero2'];
    if ($numero1 < $numero2) {
        echo "<table border='5'>";
        echo "<h1>Numeros impares</h1>";
         echo "<tr>";
        for ($num = $numero1; $num <= $numero2; $num++) {
             
            if ($num % 2 != 0) {
              
                echo "<td>";
                echo $num;
                echo "</td>";
                
            }
        }
        echo "</tr>";
        echo "</table>";
    } else {
        echo "<h1>El numero 1 debe ser menor al numero 2</h1>";
    }
} else {
    echo "<h1>Introduzca los parametros por la URL</h1>";
}