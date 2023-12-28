<!DOCTYPE html>
<html>
<head>
    <title>Interface graphique</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
            border: 1px solid #ddd;
        }
        th, td {
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>

<h2>Données de la base de données</h2>

<table>
    <tr>
        <th>Id du système</th>
        <th>Statut du système</th>
        <th>Zone 1</th>
        <th>Zone 2</th>
        <th>Zone 3</th>
        <th>Zone 4</th>
        <th>Times</th>
    </tr>
    <?php
    include('backend.php');
    // Fetch data from the database
    $sql = "SELECT * FROM Security"; // Remplacez "your_table_name" par le nom de votre table
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            echo "<tr>";
            echo "<td>" . $row['Id_System'] . "</td>";
            echo "<td>" . $row['System_Status'] . "</td>";
            echo "<td>" . $row['Zone1'] . "</td>";
            echo "<td>" . $row['Zone2'] . "</td>";
            echo "<td>" . $row['Zone3'] . "</td>";
            echo "<td>" . $row['Zone4'] . "</td>";
            echo "<td>" . $row['TimeS'] . "</td>";
            echo "</tr>";
        }
    } else {
        echo "<tr><td colspan='7'>Aucune donnée disponible</td></tr>";
    }

    // Close the database connection
    $conn->close();
    ?>
</table>

</body>
</html>