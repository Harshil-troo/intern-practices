//Class is a special Constructor
//Function used to create Objects.

//Class syntax

//class User{
//    constructor(firstname,lastname,age){
//        this.firstname = firstname
//        this.lastname = lastname
//        this.age = age
//    }
//}

//object create using class
//const user1 = new User('Harshil','Sidapara',22)
//console.log(user1)


//getter,setter
class Products{
    constructor(itemName,price,discount)
    {
        console.log("this is "+itemName)
        this.itemName = itemName
        this.price = price
        this.discount = discount
    }
    get discountprice(){
        return this.discount*"% discount is available."
    };
    set setdiscount(value){
        this.discount = value
    }
    //function create
    discountedprice(){
        return this.price-this.
        discount*this.price/100;
    }
}
class Furniture extends Products{
    constructor(itemName,price,discount,type){
        // Super method call Parent class constructor
        super(itemName,price,discount)
        this.type = type
    }
}
const laptop = new Products("MacBook Air",100000,40)
console.log(laptop)

const chair = new Furniture("Chair","1500",20,"wooden")
console.log(chair)