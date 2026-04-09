const countInput = prompt("Enter the number of participants:");
const participantCount = parseInt(countInput, 10);

if (isNaN(participantCount) || participantCount <= 0) {
    document.body.textContent = "Please reload and enter a valid number of participants.";
} else {
    const names = [];

    for (let i = 0; i < participantCount; i++) {
        let name = prompt(`Enter the name of participant ${i + 1}:`);

        if (name === null) {
            name = "";
        }

        name = name.trim();

        if (name === "") {
            i--;
            continue;
        }

        names.push(name);
    }

    names.sort((a, b) => a.localeCompare(b, undefined, { sensitivity: "base" }));

    const ol = document.createElement("ol");

    names.forEach((name) => {
        const li = document.createElement("li");
        li.textContent = name;
        ol.appendChild(li);
    });

    document.body.appendChild(ol);
}