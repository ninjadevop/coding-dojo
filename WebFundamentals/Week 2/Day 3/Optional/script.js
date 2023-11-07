

console.log("Hello from script");

var tomato = document.querySelector("#myimg");
function switchImg(){
    // console.log("I am switching images");
    // console.log(tomato.src)
    if(tomato.src=="http://127.0.0.1:5501/W2D1/Query%20Selector/assets/1.jpg"){
        console.log(tomato.src)
        tomato.src="http://127.0.0.1:5501/W2D1/Query%20Selector/assets/2.jpg";
    }else{
        console.log(tomato.src)
        tomato.src="http://127.0.0.1:5501/W2D1/Query%20Selector/assets/1.jpg";
    }


    
}

var myColor=document.querySelector("h1");
function changeColor(){
    myColor.style.backgroundColor="black";
    myColor.style.color="white";
}



//Declare a variable count outside of my likes() function

var count=0;

var message=document.querySelector("p");

function likes(){
    
    count=count+1;
    if (count==1){
        message.innerText="I have "+count + "like"
    }else{message.innerText="I have "+ count + " likes";}
    
    // count++;

}

var myDivision = document.querySelector(".mydiv");
function showInnerText(){

    console.log("innertext: "+myDivision.innerText);
    console.log("innerHTML: " +myDivision.innerHTML);
    myDivision.style.backgroundColor="green";
}