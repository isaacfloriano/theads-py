<?php
error_reporting(0);

if (isset($_POST['limpar'])) {
	# limpar o txt
	fopen('contador.txt', "w+");
}
if (file_exists("contador.txt") !== false) {
	$letra = 'r';
} else {
	$letra = 'w';
}

$arquivo = 'contador.txt';
$handle = fopen($arquivo, "$letra+");

$data = fread($handle, 512);
$contador = $data + 1;

echo "<center><h3>" . $contador . "</h3>";

fseek($handle, 0);

fwrite($handle, $contador);

fclose($handle);

# Index botões
echo "<form method='post'>
		<button type = 'submit'>Atualizar</button>
		<button type = 'submit' name = 'limpar'>Limpar</button>
	</form>";
