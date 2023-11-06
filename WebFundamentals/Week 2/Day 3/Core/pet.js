function removeMe(element){
    element.remove();

}
var message=document.querySelector("input");
function alertMe(e){

    alert("you are looking for a : "+ e.value)
        console.log(e);
}


var count = 0;
var p2=document.querySelector("#like")

function increase(){
    count++;
    p2.innerText=count2;

}