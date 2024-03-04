// How to get current time

let dt = new Date();
console.log(dt)

//let mydate = new Date(year,mont,date,hours,minutes,seconds,milliseconds)
let mydate = new Date(2029,05,14,05,12,03,2000)
console.log(mydate)

//get year
console.log(dt.getFullYear())
//get month
console.log(dt.getMonth())
//get date
console.log(dt.getDate())
//get hours
console.log(dt.getHours())
//get minute
console.log(dt.getMinutes())
//get second
console.log(dt.getSeconds())

setInterval(gettimenow,1000)
function gettimenow(){
    let dt = new Date()
    let spantime = document.querySelector('#time')
    spantime.textContent = dt
}


