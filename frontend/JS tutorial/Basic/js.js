var myBtn = document.querySelector("button");
myBtn.addEventListener('click',clck);

//   alert("Hello world")
//   var name = prompt("Hello");
//   alert("hello "+name+" Subscribe")
        function clck(){
//            alert("Hello Harshil")
//            console.log("Harshil")
            var name = prompt("Hello");
            myBtn.innerText = "Hello "+name
        }