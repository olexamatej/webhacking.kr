Website has only one input field.

![alt text](image.png)

Inspection of source code shows us this:
```Javascript
<script>
function ck(){
  var ul=document.URL;
  ul=ul.indexOf(".kr");
  ul=ul*30;
  if(ul==pw.input_pwd.value) { location.href="?"+ul*pw.input_pwd.value; }
  else { alert("Wrong"); }
  return false;
}
```

The function `ck()` will get a document URL, find the index of `.kr`, multiply it by 30, and check if the input matches this number.

Since the URL is `https://webhacking.kr/challenge/js-1/?291600`, we can see that `.kr` is at index `18`. Multiplying it by 30 gives us 540, which is the correct solution.