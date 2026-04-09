function rollDice() {
    return Math.floor(Math.random() * 6) + 1;
}

let rolls = [];
let roll;
do {
    roll = rollDice();
    rolls.push(roll);
} while (roll !== 6);

document.write('<ul>');
rolls.forEach(r => document.write(`<li>${r}</li>`));
document.write('</ul>');