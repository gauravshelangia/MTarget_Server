<?php
  require 'db_conn.php';
  session_start();

  $json = $_POST["data"];
  $jsondata = json_decode($json,True);

  $graphnode = $jsondata['graphnode'];
  $detail = $jsondata['detail'];
  $adjacentnode = $jsondata['adjacentnode'];

  //echo sizeof($rssi2);
  $adjacent = to_pg_array($adjacentnode);

  $query = "SET search_path TO MTarget;
            insert into graph values ('$graphnode','$detail','$adjacent');";
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
