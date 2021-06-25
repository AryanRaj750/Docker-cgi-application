function request(){
   var cmd = document.getElementByID("uinput").value;
   var xhr = new XMLHttpRequest();
   
   xhr.open("GET", "http://192.168.43.219/cgi-bin/dock.py", false);
   xhr.send();
   // for output from url
   xhr.onload= function(){
   var output = xhr.responseText;
   document.getElementByID("textfield").innerHTML = output;
   }
}
