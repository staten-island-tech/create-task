/* 

THE PROGRAM CODE IS THE PYTHON FILE (because its too many parts to code this in js as opposed to the python modules)

input (probably from user);
use of at least one list
at least one procedure

algorithm:
- sequencing
- selection (conditional)
- iteration

output
*/

let operations = ['a', 's', 'm', 'd']
// addition, subtraction, mulitplication, division
let numbers = [4, 5, 9, 10, 14, 18, 20]

function randomInt(min, max) { // simpler syntax for the random
    let difference = max - min;
    return Math.round((Math.random()*difference))+min;
  }

function game() {
    let totalCorrect = 0;

}

function getUnitsDigit(num) {
    return Math.floor(num % 10)
}

function askQuestion() {
    let randomNum1 = numbers[randomInt(0, 6)]
    let randomNum2 = numbers[randomInt(0, 6)]

    let num1 = Math.max[randomNum1, randomNum2]
    let num2 = Math.min[randomNum1, randomNum2]
    // if we get subtraction, i do not want a negative number, ensures that num1 > num2

    if(operations[randomInt(0, 3)] === 0) {

    } else if(operations[randomInt(0, 3)] === 1) {

    } else if(operations[randomInt(0, 3)] === 2) {

    } else {

    }
}