<?php

function x($t, $k) {
    $c = strlen($k);
    $l = strlen($t);
    $o = "";
    for ($i = 0;$i < $l;) {
        for ($j = 0;($j < $c && $i < $l);$j++, $i++) {
            $o.= $t{$i} ^ $k{$j};
        }
    }
    return $o;
}

$k = "80e32263";
$user_input = file_get_contents("php://input");
$b64decode = base64_decode($user_input);
$gibbrish = x($b64decode, $k);
$result = gzuncompress($gibbrish);

echo("Result: ".$result);

?>