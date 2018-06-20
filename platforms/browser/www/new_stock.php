<?php
 //include "config.php";
 // $name=$_POST['name'];
 // $position=$_POST['position'];
 // $salary=$_POST['salary'];
 //$q=mysqli_query($con,"INSERT INTO `crud_demo` (`name`,`position`,`salary`) VALUES ('$name','$position','$salary')");
 //if($q)
 function debug_to_console( $data ) {
    $output = $data;
    if ( is_array( $output ) )
        $output = implode( ',', $output);

    echo "<script>console.log( 'Debug Objects: " . $output . "' );</script>";
}
debug_to_console( "Test" );
 ?>
