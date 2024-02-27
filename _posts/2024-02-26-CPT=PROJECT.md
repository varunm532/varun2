---
toc: true
comments: true
layout: post
title: CPT prroject indiv review
description: Daily Plans for week 16
type: plans
courses: { compsci: {week: 20} }
---

### Project Overview:
The theme of our project sourrounded around money.It teaches the values of how to manage and grow money thorugh various means, such as stocks, crypto, and realestate. My team built features that shows information about stocks and realestate, and offers an interative experience to simulate real life crypto and stock trading
### My feature:
In my feature, a user has the ability to buy and sell the top 25 stocks in the S&P 500. The user has the ability to simulate actual stock trading without the risk of using actual money.The prices of all 25 stocks track the actual price of the stock throught the help of a 3rd party api. Each user starts out with $10,000 and the goal is it stratigically buy and sell stocks so that you can build up your wealth. Each transaction the user makes is logged and is visiable to user when the user clicks on "transaction log". The user can also see which stocks is currently own and its current price along with a graph that shows the user's money per each transaction in the "portfolio" page.
### Component A:

<html>
    <table>
        <thead>
            <tr> 
                <td>Requirements</td>
                <td> Mine</td>
            </tr>
        </thead>
        <tr>
            <td> Instructions for input from one of the following: the user, a device, an online data stream, a file.	</td>
            <td> <img src="{{site.baseurl}}/images/cptinput.png" width="400" hight="400"/> <img src="{{site.baseurl}}/images/cptinput2.png" width="400" hight="400"/> The user can press either the "buy" or "sell" button and it results in a prompt that asks you how much you want it buy/sell. takes buy/sell stock input converts it json and sends to backend</td>
        </tr>
        <tr>
            <td>Use of at least one list (or other collection type) to represent a collection of data that is stored and used to manage program complexity and help fulfill the user’s purpose.</td>
            <td> The collected in the frontend is sent to the backend by json and after calculations are done with the reseved data, the new data is stock in specific tables in a sql database<img src="{{site.baseurl}}/images/stock_transactiondb.png" width="400" hight="400"/> collects data about user's transaction history 
            !<img src="{{site.baseurl}}/images/stockmoney.png" width="400" hight="400"/> collects data about how much each user has
            </td>
        </tr>
        <tr>
            <td>At least one procedure that contributes to the program’s intended purpose,where you have defined:</td>
            <td><img src="{{site.baseurl}}/images/buystock.png" width="400" hight="400"/> This code deals with buying the stocks. It updates how much money the user has after buying the stock, it creates a log in the log table in the database, it calculates the remaining market cap.This procedure has a name(post), a return(response), and parameters(self) <img src="{{site.baseurl}}/images/sellstock.png" width="400" hight="400"/> This post function deals with selling stocks. It checks if you have enough stocks to sell, it updates the marketcap, it updates how much money the user has, it creates a log in the transaction table.This procedure has a name(post), a return(response), and parameters(self)</td>
        </tr>
        <tr>
            <td>An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure.	</td>
            <td><img src="{{site.baseurl}}/images/itteration1.png" width="400" hight="400"/> This code it uses itteration to display each stock, quantity, and price <img src="{{site.baseurl}}/images/itteration2.png" width="400" hight="400"/>This code it uses itteration to display the values in the transaction table in the sql database. <img src="{{site.baseurl}}/images/algorithm.png" width="400" hight="400"/> This function has steps(check) through the use of if/else to make sure you actually have an input, and enough stocks. If the checks pass, then it sends a post request to the buy apiendpoint </td>
        </tr>
        <tr>
            <td>Calls to your student-developed prodcedure:</td>
            <td> <img src="{{site.baseurl}}/images/apicall.png" width="400" hight="400"/> This code call the specific api endpoint through a post request <img src="{{site.baseurl}}/images/jscall.png" width="400" hight="400"/>this code calls 2 js functions</td>
        </tr>
        <tr>
            <td>Instructions for output (tactile, visual, or) based on input and program functionality</td>
            <td><img src="{{site.baseurl}}/images/transactionlog.png" width="400" hight="400"/> this shows all the transactions(inputs) the user made<img src="{{site.baseurl}}/images/portfoliodisplay.png" width="400" hight="400"/> This code uses all the transaction(input) and displays a graph that shows the history of the amount of money the user has. It also display how many stock owned + price</td>
        </tr>
    </table>
</html>

### Componant B:
All requiremnt met. The video shows input( buying and selling stock). It shows the buy/sell feature, transaction log feature, and profolio ( graph + how much stocks the person has). The output inclues the graph, transaction log, and how much stocks a person owns.It is also 1 min long and also doesn't have voice in it.

### Major commits:
https://github.com/TDWolff/cpt/commit/e71933890a9110f33d4d55a55752118de51ebdcf: in this commit, I finished the sell feature, added the graph feature, and made major edits in the feature that shows how many stocks you own
https://github.com/varunm532/atlasbackendfinal/commit/5b856c4b5c59a4c9716218c4f83d37b2dcc1b002: set up model/users.py for all the tables I was going to use and created almost completed buy feature 