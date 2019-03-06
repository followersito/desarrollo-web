<?php

/* EJERCICIO 6
  Mostrar las tablas de multiplicar del 1 al 10 en tablas de HTML
 */
echo '<table border="1">';      //Creacion de tabla

echo '<tr>';                    
for ($num = 1; $num <= 10; $num++) {
    echo '<th>Tabla del ' . $num . '</th>';
}
echo '</tr>';
echo '<tr>';
for ($contador = 1; $contador <= 10; $contador++) {
    echo '<tr>';
    for ($mult = 1; $mult <= 10; $mult++) {

        echo "<td>$mult x $contador = " . ($mult * $contador) . '</td>';
    }
    echo '</tr>';
}
echo '</tr>';
echo '<table>';


