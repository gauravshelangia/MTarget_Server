<?php
  require 'db_conn.php';
  session_start();

  $userid =  $_SESSION["userid"];
  $device_id = $_SESSION["macaddr"];
  $json = $_POST["data"];
  //echo "$json";

  $jsondata = json_decode($json,True);

  $graphnode = $jsondata['graphnode'];
  $rssi2ghz = $jsondata['rssi']['rssi2ghz'];
  $rssi5ghz = $jsondata['rssi']['rssi5ghz'];

  //echo sizeof($rssi2);
  $arr1 = to_pg_array($rssi2ghz);
  $arr2 = to_pg_array($rssi5ghz);

  //echo $rssi2ghz;
  //printf("\n");
  $tstampquery = "select(CURRENT_TIMESTAMP);";
  $result = pg_query($tstampquery);
  $timestamp = pg_fetch_row($result);
  echo $timestamp[0];
  echo "here is the new error ";
  $query = "SET search_path TO MTarget;
            insert into data values ('$userid','$device_id','$graphnode','$timestamp[0]','$arr1','$arr2');";
  $res = pg_query($query);
  if($res){
    echo "added Successfully";
  }else{
    echo "failed";
  }

  function to_pg_array($set) {
    settype($set, 'array'); // can be called with a scalar or array
    $result = array();
    foreach ($set as $t) {
        if (is_array($t)) {
            $result[] = to_pg_array($t);
        } else {
            $t = str_replace('"', '\\"', $t); // escape double quote
            if (! is_numeric($t)) // quote only non-numeric values
                $t = '"' . $t . '"';
            $result[] = $t;
        }
    }
    return '{' . implode(",", $result) . '}'; // format
  }

?>
