<?php
$dbconn=null;
global $dbconn;
$dbconn=pg_connect("host=localhost dbname=mtarget user=gaurav password=password") or die("could not connect!!!");
if($dbconn){
  //echo "connected to the server ";
}
?>
