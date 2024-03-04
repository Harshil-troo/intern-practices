$(document).ready(function(){
    console.log("This is a form event.")
    // Focus,Blur,Change,Select,Submit
    $('#exampleInputEmail1,#exampleInputEmail2').focus(function(){
        $(this).css('background-color','lightblue')
    })

    //blur event
     $('#exampleInputEmail1,#exampleInputEmail2').blur(function(){
        $(this).css('background-color','')
    })
    // change event
     $('#exampleFormControlSelect1,#exampleCheck1').change(function(){
        $(this).css('background-color','pink')
        $("#myp").html($(this).val())
        $("body").css('background-color','lightblue')

    })
    // Select event
     $('#myform').submit(function(){
        alert("The Form submit Successfully")
    })
})