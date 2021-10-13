## Mice Ink
*Creates paper like drawing experience on computers*

## What is it?
Miceink is app created to create paper-like drawing experience on touchpads and mouses<br>
With Miceink you can draw on your touchpad with ease<br>

Create quick-notes, think and solve math problems with ease on your computer!<br>
It is very natural and experience is very simmilar to a paper-drawing experience :)

## MiceInk in action 
<p algin="center">
    <img src="./examples/figures.png" width="300" height="175">
    <img src="./examples/equantions.png" width="300" height="175">
    <img src="./examples/miceink_is_cool.png" width="300" height="175">
</p>

## What about Inklet?
With inklet you need to click every time if you want to turn off the pen<br>
in miceink you do not need any switching, just draw like on paper (but you can, if you want)

## How it works?

Miceink detects speed of your mouse movement.<br>
Then it provides process to check if the move is consitent, if it is MiceInk turns on the pen if not it turns it off.

## How to run?

It can be done in 4 steps

1. Launch terminal
2. Install GUI library `pip3 install pygame`
3. Clone the repository `git clone https://github.com/Mondonno/miceink.git`
4. Type `cd src`
5. Then run it via python `python3 main.py`

## Usage

It is very simple.<br>
After you ran app, click to enable the system (program needs to know when you started drawing).
If you drawing something it automatically turns on/off your pen.

### List of commands

**Left click** `->` Toogles the drawing system<br>
**"S" key** `->` Saves your current work into `miceink YY-MM-DD HH:M:S.` in `../out` dir.

## Can I contribute?

If you think that project can be improved you're welcome to create issues, and PR's

There is also list of things that we might do in the projects tab<br>
If you want, you can help us achiing something listed there,