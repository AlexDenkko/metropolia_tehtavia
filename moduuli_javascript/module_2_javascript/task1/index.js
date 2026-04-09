const numbers = [];

function askQuestion(question) {
    return Promise.resolve(prompt(question));
}

async function main() {
    for (let i = 1; i <= 5; i++) {
        const input = await askQuestion(`Enter number ${i}: `);
        if (input === null) {
            break;
        }
        numbers.push(input);
    }

    const output = document.getElementById('output');
    output.textContent = 'Numbers in reverse order:\n' + numbers.reverse().join('\n');
    console.log('Numbers in reverse order:');
    numbers.forEach(x => console.log(x));
}

main();