//const prompt=require("prompt-sync")({sigint:true})

//Synchronous Javascript

//let a = prompt("What is your Name: ")
//let b = prompt("What is your age: ")
//let c = prompt("What is your favourite color ")
//console.log("My name is "+a+". I am "+b+" years old and my favourite color is "+c)

//Asynchronous Javascript

//console.log("start");
//setTimeout(()=>{
//    console.log("Hello Folks")
//},3000)
//setTimeout(()=>{
//    console.log("Hello Bro")
//},2000)
//setTimeout(()=>{
//    console.log("Hello Suckers")
//},4000)
//console.log("End")


// CallBack Functions

function setstyle(href,callback){
    let link = document.createElement('link')
    link.rel="stylesheet";
    link.href = href;
    link.onload = ()=>{
        console.log("Link Created "+href);
        callback();
    }
    link.onerror = ()=>{
        console.log("Error occurred  "+href);
        callback(new Error("Error in Link "));
    }
    document.head.appendChild(link)
}
function donehogya(error){
    if(error){
        console.log(error)
        return
    }
    console.log("Link added")
}
setstyle("https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css",donehogya)