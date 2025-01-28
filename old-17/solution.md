### Analysis

The initial website is a classic html with 1 input field.

![alt text](image.png)

If we try to write something and click check, we will get a `Wrong answer` alert. 

After inspecting the source code, we can find this:

```Javascript
<html>
    <head>
        <title>Challenge 17</title>
    </head>
    <body bgcolor=black>
        <font color=red size=10></font>
        <p>
        <form name=login>
            <input type=passwd name=pw>
            <input type=button onclick=sub() value="check">
        </form>
        <script>
            unlock = 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 * 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 * 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 * 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 / 100 * 10 * 10 + 1 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 * 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 + 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 - 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 / 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 / 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 / 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 / 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 / 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 / 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 / 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 / 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 / 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 * 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 * 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 * 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 * 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 * 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 * 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 * 100 * 10 * 10 + 100 / 10 - 10 + 10 + 50 - 9 * 8 + 7 - 6 + 5 - 4 * 3 - 2 * 1 * 10 + 9999999;
            function sub() {
                if (login.pw.value == unlock) {
                    location.href = "?" + unlock / 10;
                } else {
                    alert("Wrong");
                }
            }
        </script>
```

### Exploit 

Basically, the solution to this CTF is that long mathematical task - which looks scary at first but you can simply copy-paste it into python (or any other programming language of your choice) file and then print it. 

So the final solution is `7809297.1`.