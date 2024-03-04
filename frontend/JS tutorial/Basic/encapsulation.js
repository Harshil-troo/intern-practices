//Encapsulation

// It is the way of binding data and methods.
//It provides security
// It hides methods from third party hackers.

class Student{
    constructor(){
        var studentname;
        var studentmarks;
    }
    setname(studentname){
        this.studentname = studentname;
    }
     setmarks(studentmarks){
             if(studentmarks < 0 || studentmarks > 100){
                alert("Invalid Student Marks")
             }
             else {
                this.studentmarks = studentmarks;
             }
     }
     getname(){
        return this.studentname
    }
     getmarks(){
        return this.studentmarks
    }
}
const s1 = new Student();
console.log(s1.getmarks());