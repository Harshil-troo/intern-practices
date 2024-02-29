// Object is a collection of data with keys and values.
//object is a non-primitive datatype.

//const book1 = {
//    "bookName":"Ramayan",
//    "Author":"Valmiki",
//    "Description":"Victory of Ram over Ravan",
//}
//console.log(book1)
//console.log(book1.Author)

//const book2 = {
//    "bookName":"Mahabharat",
//    "Author":"Tulsidas",
//    "Description":"Talks between Lords Krishna and Arjun",
//}
//console.log(book2)
//console.log(book2.Author)

//function createBook(Title,Author,Description){
//    return {
//    "bookName":Title,
//        "Author":Author,
//        "Description":Description,
//    }
//}

//const book1 = createBook("Mahabharat","Tulsidas","Mahabharat yudh geeta gyan");
//console.log(book1);

//const book3 = createBook("Ramayan","valmiki","Ram Ravan Yudh")
//console.log(book3);

// constructor method

function bookConstructor(title){
    this.title = title
    this.available = function(){
        console.log("Book is Available")
    }
}

const book1 = new bookConstructor("Ramayan");
console.log(book1)
book1.author = "Valmiki";;
console.log(book1)
console.log(book1.available)