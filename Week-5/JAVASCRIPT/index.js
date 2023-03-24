let age = 0
let msg = ""

document.getElementById("confirm_btn").onclick=function check_age(){
    console.log("Button clicked !")
    var age = document.getElementById("age").innerHTML.valueOf()
    if (age <= 18){
        msg = "You are not allowed"
        console.log("You are not allowed")
        document.getElementById("get_in").innerHTML.msg
    }else{
        msg = "Welcome to the club"
        console.log("Welcome to the club")
        document.getElementById("get_in").innerHTML.msg
}
}