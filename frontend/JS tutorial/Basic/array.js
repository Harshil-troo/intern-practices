//Array Declare method 1

//let myarray = ['harshil',12,15,1,96,'sidapara']
//
////length
//console.log(myarray.length)
//console.log(myarray[myarray.length-1])

//Array Declare method 2

//let myarray = new Array ('harshil',12,15,1,96,'sidapara')

//push
//console.log(myarray.push('hello'))
//console.log(myarray)

//pop
//console.log(myarray.pop(1))

//shift
//console.log(myarray.shift(1))

//unshift

//console.log(myarray.unshift("hello"))

//indexof

//console.log(myarray.indexOf(15))

let newarray = [{
    name:"Harshil",
    age:22
},{
    name:"Shubhika",
    age:19
},{
    name:"Jay",
    age:23
},]
//console.log(newarray[1].name)

//Find method
//console.log(newarray.find(function(element) {
//    return element.age >= 20
//}))
//
//Arrow function
//console.log(newarray.find(function(element) >= {
//    return element.age === 20
//}))

let name1 = ['harshil']
let name2 = ['shubhika','diya','dhrumi']
//concat function

//console.log(name1.concat(name2))

//slice
//console.log(name1.concat(name2).slice(0,2))

//split
//console.log(name2[0].split(''))

//join
//console.log(name1[0].split('').join('-'))

//loop
// method 1

//for(let i in name1){
//    console.log(name[i])
//}

// method 2

//for (let i of name1){
//    console.log(i)
//}

//Advance *****

let cities = [{
    city:"Mumbai",
    population : 30000000
}, {
    city:"Ney York",
    population : 16800000
},{
    city:"London",
    population : 8000000
}]

//filter *****

//console.log(cities.filter(city => city.population >= 10000000))

//map

let population = cities.map(city => city.population * 2)
console.log(population)