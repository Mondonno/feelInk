let canvas = document.getElementById("main");
let ctx = canvas.getContext("2d");

canvas.width = innerWidth;
canvas.height = innerHeight;

let brushSize = 3;
let lastTime = Date.now();

let penOn = false;
let mouseState = false;

let currentX = null;
let currentY = null;

let lastSpeed = null;

ctx.fillText("Click to toggle pen lock      MiceInk Demo Version     github.com/Mondonno/miceInk", 0, 10);

canvas.addEventListener("click", (ev) => {
    console.log("[EVENT] toggled the pen lock whooo!");
    
    if(mouseState) mouseState = false;
    else mouseState= true;
});

canvas.addEventListener("mousemove", (ev) => {
    if(currentX == null || currentY == null)
        {
            currentX = ev.x;
            currentY = ev.y;
        }

    let dr = Math.sqrt(Math.pow(Math.abs(ev.x - currentX), 2) + Math.pow(Math.abs(ev.y - currentY), 2));
    let speed = dr / ((Date.now() - lastTime) / 1000);
    let consistency = null;

    if(lastSpeed != null)
        consistency = Math.abs(lastSpeed - speed);

    if(consistency != null
        && consistency <= speedsConsts.touchpadMacOSConsistency
        && !mouseState) {
        penOn = true;
    }
    else if(penOn) {
        penOn = false;
    }

    if(penOn) {
        ctx.beginPath();
        ctx.arc(ev.x, ev.y, brushSize, 0, 2 * Math.PI, false);
        ctx.closePath();

        ctx.fill();
        ctx.stroke();
    }

    lastTime = Date.now();

    currentX = ev.x;
    currentY = ev.y;

    lastSpeed = speed;
});