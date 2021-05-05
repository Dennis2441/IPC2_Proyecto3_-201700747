<?php
//Creamos el archivo datos.txt
//ponemos tipo 'a' para añadir lineas sin borrar
$file=fopen("output.txt","a") or die("Problemas");
  //vamos añadiendo el contenido

  $asu=$_REQUEST['lol'];

  fputs($file,$asu);
  
  fclose($file);
  ?>