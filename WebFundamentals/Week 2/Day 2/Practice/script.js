console.log("hello from script.js");

function myAlert(){
    alert('Im an alert in  a p tag');
}

function sayHello(){

    console.log("Hello");
    // return 5;
}
// console.log(sayHello());
function showValue(element){
    console.log(element.innerText);
    if(element.innerText=="ON"){
        element.innerText="Off";
        element.style.backgroundColor="red";
    }
    else
    {
        element.innerText="ON"
        element.style.backgroundColor="green";
    }
    

}
// removing the H1
function removeMe(element){
    element.remove();
}