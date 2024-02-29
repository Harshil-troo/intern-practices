// Polymorphism

// It have ability to create
//multiple instance of method and variables.
//method overriding
class animal{
    constructor(name){
        this.name = name
    }
    speak(){
        console.log(this.name+" Please specify Animal")
    }
}
class dog extends animal{
    speak(){
        console.log("Woof!Woof!")
        super.speak();
    }
}
const c = new dog("boobboo");
const d = new animal("bob");
c.speak()
d.speak()