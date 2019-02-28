<?php
/**
 * TIPOS DE DATOS EN PHP
 * Entero (int) = 99
 * Coma flotante (double) = 3.45
 * Cadena de carateres (string) = "Hola"
 * Valores booleanos (bool) = true
 * Coleccion de datos (array)
 * Objetos
 */
$numero = 100;
//echo gettype($numero).'<br>';
$decimal = 27.9;
//echo gettype($decimal).'<br>';
$texto = 'Hola soy un texto';
//echo gettype($texto);
$usuarios[]="Ivan";
$usuarios[]="Carlos";
echo "Soy un texto $numero <br>";       //Lento para navegador
echo 'Soy un texto $numero <br>';       //Con comillas simples no funciona así
echo 'Soy un texto '.$numero.'<br>';    //Recomendado concatenar con ''.''
echo 'El usuario 2 es: '.$usuarios[1].'<br>';
//Debugear
$mi_nombre="Carlos Melchor";
//var_dump($mi_nombre);       Muestra los detalles de la variable
//var_dump($usuarios);

?>