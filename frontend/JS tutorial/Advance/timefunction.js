//Set timeout

//let a = setTimeout(()=>{
//    console.log("I am inside settimeout")
//},1000)
//let b = prompt("Do you  want to show settimeout  ")
//if (b == 'n'){
//    clearTimeout(a)
//}
//else if (b == 'y'){
//    console.log(a)
//}
//else{
//    console.log("Invalid")
//}

//How to pass parameter in settimeout

function sum(a,b){
    console.log("Sum: "+(a+b))
}
//setTimeout(sum,2000,1,2)

//set interval

//let x = setInterval(()=>{
//    console.log("Hi how are you brats...")
//},2000)
//
//setTimeout(()=>{
//    clearInterval(x)
//},10000)
setInterval(sum,2000,1,2)