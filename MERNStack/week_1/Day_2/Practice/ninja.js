class ninja{
constructor  (name ,health, speed ,strength){
    this.name = name;
    this.health = 90;
    this.speed = 3 ;
    this.strength = 3 ;
}
sayName() {
    console.log(`My name is ${this.name}`);
}

showStats() {
    console.log(`Name: ${this.name}, Strength: ${this.strength}, Speed: ${this.speed}, Health: ${this.health}`);
}

drinkSake() {
    this.health += 10;
    console.log(`${this.name} drank sake and gained 10 health. Health is now ${this.health}.`);
}
}
