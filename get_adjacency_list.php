<?php
    require 'db_conn.php';
    $graphnode = $_POST['graphnode'];
    $qpath = "SET search_path TO MTarget";
    pg_query($qpath);
    $query = "select * from graph g where g.node_no = $graphnode";
    $result = pg_query($query);
    $row = pg_fetch_assoc($result);
    $adjacencylist = $row['adj_list'];
    
    echo json_encode(array("adjacencylist"=>$adjacencylist));
 ?>
