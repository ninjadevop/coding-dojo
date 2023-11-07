//Print odds 1-20
for(var i=0;i<21;i++){
    if( i % 2 !== 0){
        console.log(i,"is an odd number")
    }
}
//Decreasing Multiples of 3
for(var i=1;i<101;i++){
    if(i%3==0){
        console.log(i)
    }
}
//Print the sequence
for (var i = 4; i >= -3.5; i -= 1.5) {
    console.log(i);
}
//Sigma
var sum = 0;

for (var i = 1; i <= 100; i++) {
    sum += i;
}

console.log(sum);
//factorielle
var product = 1;

for (var i = 1; i <= 12; i++) {
    product *= i;
}
console.log(product); 