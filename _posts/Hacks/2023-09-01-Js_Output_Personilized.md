---
toc: true
comments: false
layout: post
title:  Js Output/Personilized  
type: hacks
courses: { compsci: {week: 2} }
---



<!-- Head contains information to Support the Document -->
<head>
    <!-- load jQuery and DataTables output style and scripts -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>var define = null;</script>
    <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
</head>

<!-- Body contains the contents of the Document -->
<body>
    <table id="demo" class="table">
        <thead>
            <tr>
                <th>Driver</th>
                <th>Team</th>
                <th>Car</th>
                <th>Year</th>
                <th>Championship points</th>
                <th>Driver photo</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Sebastian Vettel</td>
                <td>Red Bull Racing Renault</td>
                <td>RB6</td>
                <td>2010</td>
                <td>256</td>
                <td><img src="https://storage.googleapis.com/wtf1-com.appspot.com/1/Vettel-2013-Brazil-1.jpg" ></td>
            </tr>
            <tr>
                <td>Sebastian Vettel</td>
                <td>Red Bull Racing Renault</td>
                <td>RB7</td>
                <td>2011</td>
                <td>392</td>
                <td><img src="https://storage.googleapis.com/wtf1-com.appspot.com/1/Vettel-2013-Brazil-1.jpg" ></td>
            </tr>
            <tr>
                <td>Sebastian Vettel</td>
                <td>Red Bull Racing Renault</td>
                <td>RB8</td>
                <td>2012</td>
                <td>281</td>
                <td><img src="https://storage.googleapis.com/wtf1-com.appspot.com/1/Vettel-2013-Brazil-1.jpg" ></td>
            </tr>
            <tr>
                <td>Sebastian Vettel</td>
                <td>Red Bull Racing Renault</td>
                <td>RB9</td>
                <td>2013</td>
                <td>397</td>
                <td><img src="https://storage.googleapis.com/wtf1-com.appspot.com/1/Vettel-2013-Brazil-1.jpg" ></td>
            </tr>
            <tr>
                <td>Lewis Hamilton</td>
                <td>Mercedes AMG Petronas</td>
                <td>F1 W05 Hybrid</td>
                <td>2014</td>
                <td>384</td>
                <td><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSf5g6CG79No9W9RM2WwNCu3LE6t_IoRKk0Q&usqp=CAU"></td>
            </tr>
            <tr>
                <td>Lewis Hamilton</td>
                <td>Mercedes AMG Petronas</td>
                <td>F1 W06 Hybrid</td>
                <td>2015</td>
                <td>381</td>
                <td><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSf5g6CG79No9W9RM2WwNCu3LE6t_IoRKk0Q&usqp=CAU"></td>
            </tr>
            <tr>
                <td>Nico Rosberg</td>
                <td>Mercedes Amg Petronas </td>
                <td>F1 W07 Hybrid</td>
                <td>2016</td>
                <td>385</td>
                <td><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTRxa7QfUTjNIDRogvL80fVo4Bl6o2SKNR4Q&usqp=CAU"></td>
            </tr>
            <tr>
                <td>Lewis Hamilton</td>
                <td>Mercedes Amg Petronas</td>
                <td>F1 W08 Eq Power+</td>
                <td>2017</td>
                <td>363</td>
                <td><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSf5g6CG79No9W9RM2WwNCu3LE6t_IoRKk0Q&usqp=CAU"></td>
            </tr>
            <tr>
                <td>Lewis Hamilton</td>
                <td> Mercedes Amg Petronas</td>
                <td>F1 W09 EQ Power+</td>
                <td>2018</td>
                <td>408</td>
                <td><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSf5g6CG79No9W9RM2WwNCu3LE6t_IoRKk0Q&usqp=CAU"></td>
            </tr>
            <tr>
                <td>Lewis Hamilton</td>
                <td>Mercedes Amg Petronas</td>
                <td>F1 W10 Eq Power+</td>
                <td>2019</td>
                <td>413</td>
                <td><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSf5g6CG79No9W9RM2WwNCu3LE6t_IoRKk0Q&usqp=CAU"></td>
            </tr>
            <tr>
                <td>Lewis Hamilton</td>
                <td>Mercedes Amg Petronas</td>
                <td>F1 W11</td>
                <td>2020</td>
                <td>347</td>
                <td><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSf5g6CG79No9W9RM2WwNCu3LE6t_IoRKk0Q&usqp=CAU"></td>
            </tr>
            <tr>
                <td>Max Verstappen</td>
                <td>Red Bull Racing Honda</td>
                <td>Rb16B</td>
                <td>2021</td>
                <td>395.5</td>
                <td><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOrMkyVA7evQBlXQ0mwSwPZwXyvI6m6j0EXg&usqp=CAU"></td>
            </tr>
            <tr>
                <td>Max Verstappen</td>
                <td>Oracle Red Bull Racing</td>
                <td>RB18</td>
                <td>2022</td>
                <td>454</td>
                <td><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOrMkyVA7evQBlXQ0mwSwPZwXyvI6m6j0EXg&usqp=CAU"></td>
            </tr>
        </tbody>
    </table>
</body>

<!-- Script is used to embed executable code -->
<script>
    $("#demo").DataTable();
</script>