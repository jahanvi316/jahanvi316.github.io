<?php
    echo("colorize.php called");
// call file
    $output = shell_exec("python colorizer.py");
    header("Location: results.html");
    exit;
?>