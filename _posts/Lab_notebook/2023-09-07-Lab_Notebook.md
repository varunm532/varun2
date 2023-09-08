---
toc: true
comments: true
layout: post
title: Lab Notebook Week 3
description: Lab Notebook Week 3
type: tangibles
courses: { compsci: {week: 3} }
---

### What I learned

#### Vscode

> - To easly organize your files in _posts , make a folder and drag and drop files. DO NOT drag and drop dimed files.
>
> - To open the teacher's repo in Vs in Wsl, in Vscode:
>>
>> - go to files and open a new window
>>
>> - go to explorer, open files, and open teacher
>>
>> - open terminal in vs and type wsl, then code. This connects to remote and then open teacher in expolrer

#### Jupyter notebook
> - in powershell cd to _notebooks and then type juypter notebook to open juypter in a browser

#### HTML
> - th: table header
>
> - td: table data
>
> - tr: table row
>
> - img src="image address" : to add image from google

#### Crypto price search using api endpoint with the help of Chat GPT
> - API: An application programming interface is a way for two or more computer programs to communicate with each other.
code:
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

> -  " <title>Crypto Price Search</title> " title using HTML
>
> -  How 'searchCryptoPrice; works:
>> - gets inputed data and saves it under 'symbol' variable
>>
>> - 'symbol' gets appended into the base API url
>>
>> - 'fetch' makes a get requestion to API url ( in this case I am using https://api.coincap.io/v2/assets/)
>>
>> -  The the input exits in coincap.io, it returns the price of the crypto, if not it returns an error