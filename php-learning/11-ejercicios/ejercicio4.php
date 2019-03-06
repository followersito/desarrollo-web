<?php

/* EJERCICIO 4
  Recoger 2 números por URL (parámetro GET) y hacer operaciones básicas con esos
  2 números.
 */

    /*Forma de recibir los números 2
    $numero1=$_GET['numero1'];
    $numero2=$_GET['numero2'];
    */

//Forma de recibir los parámetros 1
if (isset($_GET['numero1']) && ($_GET['numero2'])) {
    $numero1 = (int) $_GET['numero1'];
    $numero2 = (int) $_GET['numero2'];
    echo "<h1>Calculadora</h1>";
    //Suma
    echo "<h3>Suma</h3>";
    echo "$numero1 + $numero2 = " . ($numero1 + $numero2) . "<br>";

//Resta
    echo "<h3>Resta</h3>";
    echo "$numero1 - $numero2 = " . ($numero1 - $numero2) . "<br>";

//Multiplicacion
    echo "<h3>Multiplicación</h3>";
    echo "$numero1 x $numero2 = " . ($numero1 * $numero2) . "<br>";

//División
    echo "<h3>División</h3>";
    echo "$numero1 / $numero2 = " . ($numero1 / $numero2) . "<br>";
} else {
    echo "<h1>Introduzca los valores por URL</h1>";
}
