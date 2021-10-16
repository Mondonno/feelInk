let canvas = document.getElementById("main");
let ctx = canvas.getContext("2d");

canvas.width = innerWidth;
canvas.height = innerHeight;

let alfabeth = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

function getAvSpeed() {
    let speedSum = 0;
    let speedCount = 0;

    let lastTime = new Date();

    let currentX = null;
    let currentY = null;

    document.addEventListener("click", (ev) => {
        currentX = null;
        currentY = null;

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        console.log(speedSum, speedCount, (speedSum / speedCount));

        speedSum = 0;
        speedCount = 0;
    });

    document.addEventListener("mousemove", (ev) => {
        if (currentX == null || currentY == null) {
            currentX = ev.x;
            currentY = ev.y;
            return;
        }

        let street = Math.sqrt(Math.pow(Math.abs(ev.x - currentX), 2) + Math.pow(Math.abs(ev.y - currentY), 2));
        let speed = street / (lastTime.getMinutes());

        speedSum += speed;
        speedCount++;

        if (speed <= 0.97) {
            ctx.lineWidth = 6;
            ctx.lineJoin = "round";

            ctx.moveTo(currentX, currentY);
            ctx.lineTo(ev.x, ev.y);

            ctx.stroke();
        }

        lastTime = new Date();

        currentX = ev.x;
        currentY = ev.y;
    })
}

getAvSpeed();