let canvas = document.getElementById("main");
let ctx = canvas.getContext("2d");

canvas.width = innerWidth;
canvas.height = innerHeight;

let penOn = false;

let currentX = null;
let currentY = null;

canvas.addEventListener("click", (ev) => {
    if(penOn) penOn = false;
    else penOn = true;
})

canvas.addEventListener("mousemove", (ev) => {
    if(currentX == null || currentY == null) {
        currentX = ev.x;
        currentY = ev.y;
    }

    if(penOn) {
        ctx.lineWidth = 4;
        ctx.lineJoin = "round";

        ctx.moveTo(currentX, currentY);
        ctx.lineTo(ev.x, ev.y);
    
        ctx.stroke();
    }

    currentX = ev.x;
    currentY = ev.y;
})
