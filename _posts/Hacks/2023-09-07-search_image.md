---
toc: true
comments: false
layout: post
title: Crypto Price Search
description: 
type: hacks
courses: { compsci: {week: 3} }
---


<html>
<head>
    <title>Crypto Price Search</title>
</head>
<body>
    <h1>Crypto Price Search</h1>
    <label for="symbol">Enter a cryptocurrency symbol (e.g., BTC):</label>
    <input type="text" id="symbol">
    <button onclick="searchCryptoPrice()">Search</button>
    <p id="result"></p>

    <script>
        function searchCryptoPrice() {
            const symbol = document.getElementById('symbol').value;
            const apiUrl = `https://api.coincap.io/v2/assets/${symbol}`;

            fetch(apiUrl)
                .then(response => response.json())
                .then(data => {
                    if (data.data) {
                        const price = data.data.priceUsd;
                        document.getElementById('result').textContent = `The price of ${symbol} is $${price}`;
                    } else {
                        document.getElementById('result').textContent = `Crypto symbol ${symbol} not found.`;
                    }
                })
                .catch(error => {
                    document.getElementById('result').textContent = "An error occurred while fetching data.";
                });
        }
    </script>
</body>
</html>