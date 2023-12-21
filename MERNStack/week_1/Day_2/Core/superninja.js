class Ninja{
    constructor(name){
        this.name=name;
        this.health="90";
        this.speed="3";
        this.streangth="3";
    }
    sayName(){
            console.log(`${this.name}`);
            return this;
    }
    showStats(){
        console.log(`You drove your ${ this.name } and health ${this.health} and speed ${this.speed}`);
        return this;
}
    drinkSake(){
        this.health+=10;
        return this;
    }
}
class Sensei{
    constructor(){
        this.name=name;
        this.health="90";
        this.speed="3";
        this.streangth="3";
    }
    speakWisdom(){
        this.drinkSake();
        console.log("What one programmer can do in one month, two programmers can do in two months.");
        return this;
    }
}
const newninja = new Ninja("niinja");
newninja.showStats()