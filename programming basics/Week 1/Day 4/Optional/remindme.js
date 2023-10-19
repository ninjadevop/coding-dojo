function evenNumber() {
    //create an empty array
    var evenArray = [];

    // create a loop from 1-10
    for (var i = 1; i <= 10; i++) {
        // on every number check to see if that number is even
        if (i % 2 == 0) {
            // push the number that We found too  the empty array
            evenArray.push(i)

        }

    }

    // return the result of the function
    return evenArray


}
