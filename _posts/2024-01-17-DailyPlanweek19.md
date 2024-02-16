---
toc: true
comments: true
layout: post
title: Daily Plans
description: Daily Plans for week 19
type: plans
courses: { compsci: {week: 19} }
---
<html>
    <h2>Sign in</h2>
    <body>
        <form action="javascript:login_user()">
            <p><label>
                User ID:
                <input type="text" name="uid" id="uid" required>
            </label></p>
            <p><label>
                Password:
                <input type="password" name="password" id="password" required>
            </label></p>
            <p>
                <button>Login</button>
            </p>
        </form>
        <script>
        </script>
    </body>
</html>
<script>
    // const src="{% raw %}{{site.baseurl}}{% endraw %}";
    const url = 'http://127.0.0.1:8086/api/user/authenticate'
    window.login_user = function(){
        var uid = document.getElementById('uid').value;
        var password = document.getElementById('password').value;
       // var name = document.getElementById('name').value
        var data = {
            uid: uid,
            password: password,
           // name: name
        };
        var json = JSON.stringify(data);
        console.log('uid:', uid);
        console.log('password:', password);
        //console.log('name:', name);
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: json
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            var users = document.getElementById('users');
            if(users) {
                users.innerHTML = JSON.stringify(data);
            }
            alert("Wrong username/password or such user does not exist")
            window.location.href = "http://127.0.0.1:8086/register"
        })
        .catch((error) => {
            console.error('Error:', error);
            alert("Successfuly logged in!")
            window.location.href = "http://127.0.0.1:8086/display/";
        });      
    }
</script>