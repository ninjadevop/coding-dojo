/* 
Given an array of strings
return the number of times each string occurs (a frequency / hash table)
hasOwnProperty()
*/
var user = { username: "John", age: 35 }

// console.log(user.hasOwnProperty('age'));
// console.log(user.hasOwnProperty('email'));

const arr1 = ["a", "a", "a"];
const expected1 = {
    a: 3,
};
const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
    a: 2,
    b: 1,
    c: 3,
    B: 1,
    d: 1,
};

const arr3 = [];
const expected3 = {};

function makeFrequencyTable(arr) {
var freqTable ={};
for(var elem of arr){
    if(!freqTable.hasOwnProperty(elem)){
        freqTable[elem] = 1;
    } else {
        freqTable[elem] += 1;
    }
}
return freqTable ;
}
for(var key in freqTable){
    if(freqTable[key]%2!==0){
        return parseInt
    }
}