// Inheritance in OOP is used to inherit the feature
//and method of parent class.

class animal{
    constructor(name,speed){
        this.name = name
        this.speed = speed
    }
    getspeed(){
        return console.log(this.name+' runs with a speed of '
        +this.speed)
    }
}
class lion extends animal{
    roar(){
        return console.log(this.name+' can roar up to many distance. ')
    }
}
class monkey extends animal{
    jump(){
        return console.log(this.name+'can jumps a trees.')
    }
}

const cheetah = new animal('Cheetah',100)
const l = new lion('King of jungle',30)
console.log(l)
console.log(cheetah)
const m = new monkey('chomu',25)
console.log(m)