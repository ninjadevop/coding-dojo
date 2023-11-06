function isPresent2d(arr2d, value) {
    for (var i = 0; i < arr2d.length; i++) {
    for (var j = 0; j < arr2d[i].length; j++) {
        if (arr2d[i][j] === value) {
        return true; 
        }
    }
    }
    return false; 
}
var arr2d = [ [2, 5, 8],
            [3, 6, 1],
            [5, 7, 7] ];
            isPresent2d(arr2d);
