<?php

/* EJERCICIO 5
  Hacer un programa que muestre todos los numeros entre dos numeros que nos lleguen por la URL
 */
if (isset($_GET['numero1']) && isset($_GET['numero2'])) {
    $numero1 = $_GET['numero1'];
    $numero2 = $_GET['numero2'];
    if ($numero1 < $numero2) {
        for ($contador = $numero1; $contador <= $numero2; $contador++) {
            echo "<h4>$contador</h4>";
        }
    } else {
        echo "<h1>El numero 1 debe ser menor al numero 2</h1>";
    }
} else {
    echo "<h1>Introduzca los parametros por la URL</h1>";
}