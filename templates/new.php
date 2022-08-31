<?php 
	session_start();
	if(!isset($_SESSION['di'])){
		Header('location:login.php');
		exit();
	}
	
?>
<!Doctype html>
<html>
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta charset="utf-8">
		<link href="index.css" rel="stylesheet" type="text/css">
		<link href="assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">
		<link href="assets/css/font-awesome.min.css" rel="stylesheet" type="text/css">
		<link rel="icon" href="assets/images/key.jpg" type="image/x-icon">
		<script src="assets/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
		<script src="assets/js/vendor/bootstrap.min.js"></script>
		<script src="js/plugins.js"></script>
		<title>Safe Haven</title>
	</head>
	<body class="container-fluid backimage">
		<div class='row'>
			<div class='col-xs-12 col-lg-offset-3 col-lg-6'>
				<div id="home">
					<img id="img" src="assets/images/key.jpg" width="50" height="50" class="img-responsive img-circle">
					<h2 class="h2" id="tit">&nbsp&nbsp<a href="index.php">SAFE HAVEN</a></h2>
					<div class="row">
						<div class="col-xs-12 col-md-offset-3 col-md-6">
							<form method="post">
								<div class="col-xs-12 form-group">
									<label>URL</label>
									<input type="text" name="url" class="form-control" required>
								</div>
								<div class="col-xs-12 form-group">
									<label>Username/Email</label>
									<input type="text" name="username" class="form-control" required>
								</div>
								<div class="col-xs-12 form-group">
									<label>Password</label>
									<input type="password" name="password" class="form-control" required>
								</div>
								<div class="col-xs-12 form-group">
									<input type="submit" name="submit" class="btn btn-default" value="Add">
								</div>
								
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>
<?php
include "conn.php";

	if(isset($_POST['submit'])){
		$password = uniqid().$_POST['password'];
		$password = convert_uuencode($password);
		$url = $_POST['url'];
		$username = $_POST['username'];
		$user = $_SESSION['di'];
		$sql = "insert into platforms (username,url,password,user)values(?,?,?,?)";
		$stmt = $conn->prepare($sql);
		$stmt->bind_param('sssi',$username, $url, $password, $user);
		if ($stmt->execute()){
			echo "<script>location.assign('index.php')</script>";
		}else{
			echo $conn->error;
		}
		$stmt->close();
	}
?>