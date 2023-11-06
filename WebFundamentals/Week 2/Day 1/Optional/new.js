// console.log("hello ")

// remove the Join button
function removeMe(element){
    element.remove();
}

var message=document.querySelector("input");
function alertMe(){

    alert("you have entered: "+ message.value)
}


var count2 = 17;
var p2=document.querySelector("#likes2")

function increase(){
    count2++;
    p2.innerText=count2;

}
function decrease(){
    count2--;
    p2.innerText=count2;

}