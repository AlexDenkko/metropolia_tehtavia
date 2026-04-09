const numbers = [];

function askNumber() {
    const input = prompt('Enter a number (0 to stop): ');
    if (input === null) {
        return;
    }
    const num = parseFloat(input);
    if (isNaN(num)) {
        alert('Please enter a valid number.');
        askNumber();
        return;
    }
    if (num === 0) {
        numbers.sort((a, b) => b - a);
        const output = document.getElementById('output');
        output.textContent = 'Numbers from largest to smallest:\n' + numbers.join('\n');
        return;
    }
    numbers.push(num);
    askNumber();
}

askNumber();