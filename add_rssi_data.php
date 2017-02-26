<?php
  require 'db_conn.php';
  $userid = $_POST['userid'];
  $device_id = $_POST['macaddr'];
  $graphnode = $_POST['graphnode'];
  $timestamp = $_POST['timestamp'];
  $rssivec = $_POST['rssivec'];


  $query = "SET search_path TO MTarget;
            insert into data values ('$userid','$device_id','$graphnode','$timestamp','$rssivec');";
  $res = pg_query($query);
  if($res){
    echo "added Successfully";
  }else{
    echo "failed";
  }
?>
