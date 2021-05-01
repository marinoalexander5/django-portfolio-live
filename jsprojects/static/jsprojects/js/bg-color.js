  
const hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'];

const btn = document.getElementById("btn");
let color = document.getElementById("color");

btn.addEventListener("click", function () {
    let hexColor = '#';
    for (let index = 0; index <= 6; index++) {
        hexColor += hex[Math.floor(Math.random() * hex.length)];
        // change background color
        document.body.style.backgroundColor = hexColor;
        // change displayed text
        color.textContent=hexColor;
    };
});