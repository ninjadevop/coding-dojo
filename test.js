function findAverage(arr) {
    var currentSum = 0;
    for(var i=0;i<arr.length;i++){
      currentSum=currentSum+arr[i];
}
    return currentSum / arr.length;
}

findAverage([12, 21, 3.6, 9, 12, 8]);