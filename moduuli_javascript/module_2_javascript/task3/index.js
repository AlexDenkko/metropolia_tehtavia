let dogs = [];
for (let i = 0; i < 6; i++) {
    let name = prompt("Enter dog name:");
    if (name) {
        dogs.push(name);
    }
}

// järjestää aakkosjärjestykseen käänteisesti
dogs.sort((a, b) => b.localeCompare(a));

document.write("<ul>");
dogs.forEach(name => {
    document.write(`<li>${name}</li>`);
});
document.write("</ul>");