<?php
if (file_exists("contador.txt") !== false) {
	$letra = 'r';
}else{
	$letra = 'w';
}
$arquivo = 'contador.txt';
$handle = fopen($arquivo,"$letra+");

$data = fread($handle, 512);
$contador = $data + 1;

echo $contador;

fseek($handle, 0);

fwrite($handle, $contador);

fclose($handle);