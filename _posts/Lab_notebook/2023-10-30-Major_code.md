---
toc: true
comments: true
layout: post
title: Passion Project code snippet
description: Lab Notebook Week 11
type: tangibles
courses: { compsci: {week: 11 } }
---
```
<html>
<head>
    <!-- load jQuery and DataTables output style and scripts -->
    <!-- The line below styles the table -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <!-- Brings out a tool from jQuery to help change the way the table looks -->
    <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>var define = null;</script>
    <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
</head>
<body>
    <table id="demo" class="table">
        <thead>
            <tr>
                <th>Book Author</th>
                <th>Book Title</th>
                <th>Cover</th>
                <th>Blurb</th>
            </tr>
        </thead>
        <tbody id="tabledata">

        </tbody>
    </table>

    <script>
        var api = 'https://bookbattles.stu.nighthawkcodingsociety.com/api/books/';
        var tableBody = document.getElementById("tabledata");

        function fillTable() {
            fetch(api)
                .then(response => response.json())
                .then(data => {
                    data.forEach(function(book) {
                        if (book.genres.includes("action and adventure")) {
                            var table_row = document.createElement("tr");
                            var author = document.createElement("td");
                            var title = document.createElement("td");
                            var coverCell = document.createElement("td");
                            var blurb = document.createElement("td");

                            author.innerHTML = book.book_author;
                            title.innerHTML = book.book_title;
                            coverCell.innerHTML = '<img src="' + book.cover_url + '" alt="Book Cover" style="width:50px;height:50px;">';
                            blurb.innerHTML = book.blurb;

                            table_row.appendChild(author);
                            table_row.appendChild(title);
                            table_row.appendChild(coverCell);
                            table_row.appendChild(blurb);

                            tableBody.appendChild(table_row);
                        }
                    });

                    $('#demo').DataTable();
                })
                .catch(error => console.error('Error fetching data:', error));
        }

        fillTable();
    </script>
</body>
</html>
```

---
```
<head>
    <!-- load jQuery and DataTables output style and scripts -->
    <!-- The line below styles the table -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <!-- Brings out a tool from jQuery to help change the way the table looks -->
    <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>var define = null;</script>
    <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
</head>
<body>
    <table id="demo" class="table">
        <thead>
            <tr>
                <th>Book Author</th>
                <th>Book Title</th>
                <th>Cover</th>
                <th>Blurb</th>
            </tr>
        </thead>
        <tbody id="tabledata">

        </tbody>
    </table>
```
- this HTML code is the basic structure of the table
- it has an id which is used in javascipt to create table rows and insert table data

---
```
<script>
        var api = 'https://bookbattles.stu.nighthawkcodingsociety.com/api/books/';
        var tableBody = document.getElementById("tabledata");

        function fillTable() {
            fetch(api)
                .then(response => response.json())
                .then(data => {
                    data.forEach(function(book) {
                        if (book.genres.includes("action and adventure")) {
                            var table_row = document.createElement("tr");
                            var author = document.createElement("td");
                            var title = document.createElement("td");
                            var coverCell = document.createElement("td");
                            var blurb = document.createElement("td");

                            author.innerHTML = book.book_author;
                            title.innerHTML = book.book_title;
                            coverCell.innerHTML = '<img src="' + book.cover_url + '" alt="Book Cover" style="width:50px;height:50px;">';
                            blurb.innerHTML = book.blurb;

                            table_row.appendChild(author);
                            table_row.appendChild(title);
                            table_row.appendChild(coverCell);
                            table_row.appendChild(blurb);

                            tableBody.appendChild(table_row);
                        }
                    });

                    $('#demo').DataTable();
                })
                .catch(error => console.error('Error fetching data:', error));
        }

        fillTable();
    </script>
```
- first it fetches the api then converts it to json.
- then that data is used to populate the table
- then it check in the api if a book has a spefic genera
- the id used in the HTML table struct is used to create new table rows and populate it with data.
```
 var table_row = document.createElement("tr");
```
- this creates a table row 


```
 document.createElement("td");
```
- this creates table data inside the table row


```
author.innerHTML = book.book_author;
                            title.innerHTML = book.book_title;
                            coverCell.innerHTML = '<img src="' + book.cover_url + '" alt="Book Cover" style="width:50px;height:50px;">';
                            blurb.innerHTML = book.blurb;
```
- this inserts the data from the api to the table data


```
 table_row.appendChild(author);
                            table_row.appendChild(title);
                            table_row.appendChild(coverCell);
                            table_row.appendChild(blurb);

                            tableBody.appendChild(table_row);
```
- this appends the data to html