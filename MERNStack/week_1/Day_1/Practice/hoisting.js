var hello = 'world';                                 
console.log(hello);                                   

var needle = 'haystack';
function test(){
    var needle = 'magnet';
    console.log(needle);
}
test();

var brendan = 'super cool';
function print(){
    brendan = 'only okay';
    console.log(brendan);
}
console.log(brendan);

var food = 'chicken';
console.log(food);
function eat(){
    var food = 'gone';
    food = 'half-chicken';
    console.log(food);
}
eat();

console.log(food);
var mean = function() {
    var food = "fish";
    console.log(food);
    food = "chicken";
    console.log(food);
}
mean();
console.log(food);


console.log(genre);
var genre = "disco";
function rewind() {
    var genre = "r&b";
        console.log(genre);
    genre = "rock";
    console.log(genre);
}
rewind();
console.log(genre);


dojo = "san jose";
console.log(dojo);
function learn() {
    var dojo = "burbank";
        console.log(dojo);
    dojo = "seattle";
    console.log(dojo);
}
learn();
console.log(dojo);


console.log(makeDojo("Chicago", 65));
console.log(makeDojo("Berkeley", 0));
function makeDojo(name, students){
    const dojo = {};
    dojo.name = name;
    dojo.students = students;
    if(dojo.students > 50){
        dojo.hiring = true;
    }
    else if(dojo.students <= 0){
        dojo = "closed for now";
    }
    return dojo;
}


