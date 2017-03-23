<?php
  require 'db_conn.php';

  // start session
  session_start();

  $userid = $_POST['userid'];
  $username = $_POST['username'];
  $macaddr = $_POST['macaddr'];
  $devtype =$_POST['dev_type'];
  if( pg_num_rows(pg_query("SET search_path TO MTarget;
        select * from users u where u.userid = '$userid';"))==0){
    $query = "SET search_path TO MTarget;
    insert into users values('$userid','$username');";
    $res1 = pg_query($query);

    // send it to the server if added Successfully or not
    if($res1){
      //echo "Successfully added ";
      //echo $macaddr;
      if(pg_num_rows(pg_query("SET search_path TO MTarget; select * from devices d where d.device_id = '$macaddr';"))==0){
        $query2 = "SET search_path TO MTarget;
        insert into devices values ('$macaddr','$devtype','$userid');";
        $res2 = pg_query($query2);
        if($res2){
          echo "device information added";
        }else{
          echo "failed to add device detail";
        }
      }else {
        echo "already exists in the database device details ";
      }
    }else{
      echo "user add query failed";
    }

  }else{
    if(pg_num_rows(pg_query("SET search_path TO MTarget; select * from devices d where d.device_id = '$macaddr';"))==0){
      $query2 = "SET search_path TO MTarget;
      insert into devices values ('$macaddr','$devtype','$userid');";
      $res2 = pg_query($query2);
      if($res2){
        echo "device information added";
      }else{
        echo "failed to add device detail";
      }
    }else {
      echo "already exists in the database device details ";
    }
  }

  $_SESSION["userid"] = $userid;
  $_SESSION["macaddr"] = $macaddr;


?>
