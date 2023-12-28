<!DOCTYPE html>
<html>
<head>
    <title>Security System Control</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <?php 
    include('backend.php')
    

    /// Endpoint pour mettre à jour l'état du système
    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['status'])) {
        $status = $_POST['status'];
    
        // Assurez-vous que le statut est 'on' ou 'off'
        if ($status === 'on' || $status === 'off') {
            $sql = "INSERT INTO system_status (Status) VALUES ('$status')";
            if ($conn->query($sql) === TRUE) {
                echo "Status saved successfully";
            } else {
                echo "Error saving status: " . $conn->error;
            }
        } else {
            echo "Invalid status value";
        }
    }
    
    
// Endpoint pour mettre à jour le port
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['port'])) {
    $port = $_POST['port'];

    // Enregistrez le numéro de port dans la base de données ou faites ce que vous souhaitez
    // Par exemple, vous pouvez l'enregistrer dans une table spécifique
    $sql = "INSERT INTO ports (2003) VALUES ($port)";
    if ($conn->query($sql) === TRUE) {
        echo "Port number saved successfully";
    } else {
        echo "Error saving port number: " . $conn->error;
    }
}
?>
</body>
</html>