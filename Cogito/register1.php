<?php

session_start();
$temp1 = "";
$temp2 = "";

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

// connect to the database
$db = mysqli_connect('localhost', 'root', '', 'lang_first_db');

// REGISTER USER
if (isset($_POST['registerbtn'])) 
{
// receive all input values from the form
$name = mysqli_real_escape_string($db, $_POST['fname']);
$age = mysqli_real_escape_string($db, $_POST['age']);
$email = mysqli_real_escape_string($db, $_POST['email']);

foreach ($_POST['pro_language'] as $selectedOption)
  $temp1 .= $selectedOption . ",";
$temp1= substr($temp1, 0, -1);
$pro_language = mysqli_real_escape_string($db, $temp1);

foreach ($_POST['curr_language'] as $selectedOption1)
  $temp2 .= $selectedOption1 . ",";
$temp2= substr($temp1, 0, -1);
$curr_language = mysqli_real_escape_string($db, $temp1);
$username = mysqli_real_escape_string($db, $_POST['username']);
$psw = mysqli_real_escape_string($db, $_POST['psw']);
$cnfpsw = mysqli_real_escape_string($db, $_POST['psw-repeat']);
$errors= array();
}
// form validation: ensure that the form is correctly filled ...
// by adding (array_push()) corresponding error unto $errors array
if (empty($name)) { array_push($errors, "Name is required");}
if (empty($username)) { array_push($errors, "Username is required"); }
if (empty($email)) { array_push($errors, "Email is required"); }
if (empty($psw)) { array_push($errors, "Password is required"); }
if ($psw != $cnfpsw) {
array_push($errors, "The two passwords do not match");
}

// first check the database to make sure 
// a user does not already exist with the same username and/or email
$user_check_query = "SELECT * FROM lang_first_tb WHERE username='$username' OR email='$email' LIMIT 1";
$result = mysqli_query($db, $user_check_query);
$user = mysqli_fetch_assoc($result);

if ($user) { // if user exists
  /*if ($user['Username'] === $username) {
    array_push($errors, "Username already exists");
    echo "User already exists!";
  }

  if ($user['Email'] === $email) {
    array_push($errors, "email already exists");*/
    array_push($errors, "User already exists");
}

// Finally, register user if there are no errors in the form
if (count($errors) == 0) {
  $password = md5($psw);//encrypt the password before saving in the database
  //$password = string md5(string $psw [, bool $raw_output = false ]);

  $query = "INSERT INTO lang_first_tb(FullName, Age, Email, Proficient_Language, Current_Language, Username, Enc_Password) VALUES('$name', '$age', '$email', '$pro_language', '$curr_language', '$username', '$password')";
  mysqli_query($db, $query);
  $_SESSION['Username'] = $username;
  $_SESSION['success'] = "You are now registered";
  echo "Success";
  header('refresh:2; url=login.html');
}
else
{
  foreach($errors as $x)
  echo $x;
  header('refresh:2; url=register.html');
}

?>