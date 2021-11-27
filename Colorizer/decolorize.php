<?php
    echo("decolorize.php called");
// call file
    $output = shell_exec("python decolorizer.py");
    header("Location: results.html");
    exit;
?>