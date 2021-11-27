<?php 
echo "PHP RAN";

#change input image name to old
$info = pathinfo($_FILES['filename']['name']);
$ext = $info['extension']; // get the extension of the file
// $newname = "old.".$ext; 
// $newname = "old.png"; 

# Save to images folder
$target = 'Images/old.png';
move_uploaded_file( $_FILES['filename']['tmp_name'], $target);

echo "Input saved into Images folder";

#send to button-specific php
    if (isset($_POST['action1'])) {
      header('Location: /colorize.php');
      exit();
    } else {
      header('Location: /decolorize.php');
      exit();
    }
   
?>