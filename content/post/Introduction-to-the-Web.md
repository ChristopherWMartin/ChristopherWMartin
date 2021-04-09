---
title: "Introduction to the Web"
date: 2020-08-25T15:25:09-04:00
draft: false
---

![header image](/media/header.png)

## Overview

Throughout this course you will learn how to build a website from scratch using standard web frameworks including HTML, CSS, and Javascript. To create content for your website we will add text, images, and other assets though HTML and an interactive program (for example, a game, drawing program, weather forecaster, neural network bot) using the P5.js Javascript framework.

## Tools

- A text editor (e.g. [Atom](https://atom.io)) and any web browser (recommended) or a [Glitch.com](https://glitch.com) account (optional)
- A [P5.js editor](https://editor.p5js.org) account (optional)

----

## Chapter One

### The structure of a webpage 
In its most basic form a website is just a folder with an `index.html` file, a `styles.css` file and a `script.js` file.

The `index.html` file contains all of the __content__ of a website - the words, pictures, links, and basic formatting. It is written in Hypertext Markup Language (HTML) which consists of tags that allow a web browser (like Google Chrome or Safari) to interpret the words you write as specific elements on a web page (like links, buttons, and input forms).

The `styles.css` (Cascading Style Sheet) file is where you define the __appearance__ of your website like what colors the background and text should be, where elements should be positioned on the page, and how the webpage should react to different screen sizes (for example, you would typically like your website to look different when viewed on a smartphone than when it is viewed on a laptop). 

The `script.js` file is where you can add more __interactivity__ and complex animations to your website. It is written in the Javascript programming language which gives you the ability to add powerful features to your website. Almost all web games (like slither.io) and web applications (like google drive) are created using Javascript.

To bring this all together: if, for example, you would like to create a website that display images of your artwork you could add a list of images to your `index.html` file then resize and arrange the images in a grid in your `styles.css` file and, finally, using your `script.js` file you could add an animation to zoom in and center each image when its clicked on.

----

## Chapter Two

### Creating a basic webpage

Create a folder on your computer and name it `my-website`. Inside of this folder create a file named `index.html`.

{{< rawhtml >}}
<video preload muted playsinline controls poster="/media/create-my-website-folder.png" src="/media/create-my-website-folder.mp4"></video>
{{< /rawhtml >}}


{{< rawhtml >}}
<video preload muted playsinline controls poster="/media/create-index-html.png" src="/media/create-index-html.mp4"></video>
{{< / rawhtml >}}

Your `index.html` file is the centerpiece of your website. It is where you link your `styles.css` and `script.js` files together with the main content of your website.

The `index.html` file contains two main sections: the __head__ where we store metadata about our website like it’s title and the location of our .css and .js files and the __body__ where all of the website’s main content lives (the text, images, buttons, navigation bars, etc.)

To get started open your blank `index.html` file and type the following.

{{< highlight HTML >}}
<html>
  
  <head>

  </head>

  <body>

  </body>

</html>
{{< / highlight >}}

You will notice that each tag (`<html>`) has a corresponding closing tag with a backslash at the beginning (`</html>`). This is important to remember as that is how your web browser will know where one tag ends and another starts.

If you save this file and drag it into your browser you will see a blank webpage. You can keep this page open and any changes you make to your `index.html` file will automatically appear as soon as you refresh the page.

{{< rawhtml >}}
<video muted playsinline controls poster="/media/drag-index-to-browser.png" src="/media/drag-index-to-browser.mp4"></video>
{{< / rawhtml >}}

Now lets add a couple more elements to our `index.html` file

{{< highlight HTML>}}
<html>

  <head>
    <title>My new website</title>
  </head>

  <body>
    <h1>Welcome to my website!</h1>
  </body>
  
</html>
{{< / highlight >}}

You should notice that the text that you added to the body of your file showed up on the webpage! We put this text inside of `<h1>` tags. The `<h1>` tag is the largest of the heading tags but there are also `<h2>`, `<h3>`, `<h4>`, `<h5>`, and `<h6>` tags which all decrease in size as the numbers get larger. These tags should be used to create titles and other important text on your webpage. 

You might have also noticed that the browser tab your website is opened in now displays “_My new website_”. You can change this by changing the text inside of the `<title>` tags.

![new website preview](/media/my-new-website.png)

----

## Chapter Three

### Make it stylish

Now that you have a simple website started lets add a `styles.css` file so that we can start tweaking the design of the site.

In your `my-website` folder create a new blank file named `styles.css` and open it up in your text editor.

{{< rawhtml >}}
<video muted playsinline controls poster="/media/create-styles-css.png" src="/media/create-styles-css.mp4"></video>
{{< / rawhtml >}}

To tweak the design of a specific element of your web page using CSS you can select it using the tag name without angle brackets ( `< >` ).

{{< highlight CSS >}}
body {
  background-color: black;
  color: white; 
}

h1 {
  color: green;
}
{{< / highlight >}}

Here we are making the background color of the entire web page black, setting the default text color to white and setting the text color of `<h1>` tags to green. Feel free to experiment and change these colors to anything you like.

The attributes that you would like to apply to each element should be placed between an opening and closing curly bracket ( { } ) and each line should end with a semicolon ( ; ).


CSS has a bunch of built in properties aside from color and background-color that we will cover later on but for now save your `styles.css` file and open your `index.html` file again.


Before we can see these colors on our web page we need to link this `styles.css` file to our `index.html` file from earlier by adding a new line telling the HTML file where it can find our CSS file. 

{{< highlight HTML >}}
<html>

  <head>
    <link href="styles.css" rel="stylesheet" type="text/css">
    <title>My new website</title>
  </head>

  <body>
    <h1>Welcome to my website!</h1>
  </body>

</html>
{{< / highlight >}}

Once you’ve added this new line save the file and refresh your web page in the browser. You should see that your website has updated to use your new color scheme!

{{< rawhtml >}}
<video muted playsinline controls poster="/media/link-styles.png" src="/media/link-styles.mp4"></video>
{{< / rawhtml >}}

----

## Chapter Four

### Give it some class


At this point you have your own website that uses the `<h1>` HTML tag for a page title but what if you want to add more?


Let's add two new lines to our HTML file. This time we’ll use the `<p>` (paragraph) tag. The paragraph tag is the standard tag for most text on a website. In general, all text other than titles and subtitles should be placed inside of a `<p>` tag.

{{< highlight HTML >}}
<html>

  <head>
    <link href="styles.css" rel="stylesheet" type="text/css">
    <title>My new website</title>
  </head>

  <body>
    <h1>Welcome to my website!</h1>
    <p class="warning">Warning: this page is under construction!</p>
    <p>This is where you can write about all of your favorite things</p>
  </body>

</html>
{{< / highlight >}}

You will notice that we’ve added something else new to one of these paragraph tags - a __class__. All HTML elements can be given a class attribute. On its own a class won’t do anything special but it allows us to target a specific section of our web page in CSS so that we can style it differently than other elements that are using the same tag.


Save your `index.html` file and open up your `styles.css` file.


To target a specific class in CSS write the class name with a period ( `.` ) in front of it. Then you can apply styles to it the same way you would for a tag.

{{< highlight CSS >}}
body {
  background-color: black;
  color: white;
}

h1 {
  color: green;
}

.warning {
  background-color: red;
  color: white;
  border: 1px solid yellow;
}	
{{< / highlight >}}

While we have the `styles.css` file open we can add a few more CSS attributes to make our page look a bit nicer.

{{< highlight CSS>}}
body {
  background-color: black;
  color: white;
  margin-left: 10%;
  margin-right: 10%;
  margin-top: 2%;
  margin-bottom: 2%;
}

h1 {
  color: green;
  text-align: center;
}

.warning {
  background-color: red;
  color: white;
  border: 1px solid yellow;
  text-align: center;
  padding: 1%;
}
{{< / highlight >}}

The `margin` attributes add __space between__ HTML elements and the edges of the web page. Moving web page content away from the far edges of the screen typically makes your site easier to read. The `text-align` attribute can be set to either left, right, or center and this determines where __text is placed__ on the web page. Lastly, the `padding` attribute is very similar to margin except that this adds __space inside__ of an HTML element. In this case this makes the background section of our `warning` element larger.

Save your files and refresh your web page to see all of the changes!

![html web page preview](/media/added-class.png)

----

## Chapter Five
### Hypertext

The H in HTML stands for hypertext (dynamic, interactive text). This is one of the most important innovations of the internet - it's what sets a web page apart from a book! Let's take advantage of this feature and add some links and images to our website.


To add a link to our web page we can use the `<a>` tag. The `<a>` tag takes an `href` attribute where you can specify the URL (link) you would like to attach. Any text that you add before the closing `</a>` tag will turn into a hyperlinked text. Try adding this new line to your `index.html` file.

{{< highlight HTML>}}
<html>

  <head>
    <link href="styles.css" rel="stylesheet" type="text/css">
    <title>My new website</title>
  </head>

  <body>
    <h1>Welcome to my website!</h1>
    <p class="warning">Warning: this page is under construction!</p>
    <p>This is where you can write about all of your favorite things</p>
    <p>Click <a href="https://textfile.io">here</a> to visit my favorite website</p>
  </body>

</html>
{{< / highlight >}}

To add an image to your website first create a new folder named `images` inside of your `my-website` folder. Any image that you would like to add to your website should be downloaded and placed in this folder. Once you’ve found an image you like you can add it to your website using the `<img>` tag.

{{< rawhtml >}}
<video muted playsinline controls poster="/media/create-images-folder.png" src="/media/create-images-folder.mp4"></video>
{{< / rawhtml >}}

_Note: make sure your image’s filename doesn’t contain a space. If it does, web browsers will not be able to load your image correctly._

{{< highlight HTML >}}
<html>

  <head>
    <link href="styles.css" rel="stylesheet" type="text/css">
    <title>My new website</title>
  </head>

  <body>
    <h1>Welcome to my website!</h1>
    <p class="warning">Warning: this page is under construction!</p>
    <p>This is where you can write about all of your favorite things</p>
    <p>Click <a href="https://textfile.io">here</a> to visit my favorite website</p>
    <img src="images/grumpy-cat.jpg" alt="a picture of a frowning cat">
  </body>

</html>
{{< / highlight >}}

The `<img>` tag takes two attributes. The first is `src` which is the location of your image in relation to your `index.html` file. The second attribute is `alt` which is a description of your image that will be shown in the event your image can’t be loaded. The `alt` attribute also allows those that are blind or that have impaired vision to effectively navigate your website using a screen reader! {{<sidenote>}} As long as you follow all of the best practices when creating your website (like adding `alt` attributes to your images) [screen readers](https://en.wikipedia.org/wiki/Screen_reader) can even turn your website into braille! {{</sidenote>}}

To wrap things up let's add a new section to our `styles.css` file to resize and center our image on the page.

{{< highlight CSS >}}
body {
  background-color: black;
  color: white;
  margin-left: 10%;
  margin-right: 10%;
  margin-top: 2%;
  margin-bottom: 2%;
}

h1 {
  color: green;
  text-align: center;
}

img {
  display: block;
  margin: auto;
  width: 50%;
}

.warning {
  background-color: red;
  color: white;
  border: 1px solid yellow;
  text-align: center;
  padding: 1%;
}
{{< / highlight >}}

The `width` attribute allows us to resize the image to a specific percentage of our screen size. In this case we are resizing our image to fill up half of the screen. Displaying the image as a `block` element gives us the ability to align it horizontally. Finally, setting the image’s `margin` to `auto` will position the image in the center of the screen horizontally. 

{{< rawhtml >}}
<video muted playsinline controls poster="/media/add-image.png" src="/media/add-image.mp4"></video>
{{< / rawhtml >}}

----

## Chapter Six

### Introduction to Javascript Programming


Up until now we’ve been writing HTML and CSS code which are both __markup languages__. From this point forward we will be learning Javascript which is a full blown __programming language__. This will increase the complexity of the code slightly as we now have access to variables, loops, conditional statements, and more but this also means that we will have the power to create much more powerful programs.


To write Javascript for our website we will be using the P5.js framework. This allows us to easily create animations and interactive games.

To get started with P5.js we need to import the framework from our `index.html` file just like we did with our CSS file. Create a new file named `script.js` in your `my-website` folder and then add these two new lines to the `head` of your HTML file.

{{< rawhtml >}}
<video muted playsinline controls poster="/media/add-script-js.png" src="/media/add-script-js.mp4"></video>
{{< / rawhtml >}}

{{< highlight HTML>}}
<html>

  <head>
    <link href="styles.css" rel="stylesheet" type="text/css">
    <script src="https://cdn.jsdelivr.net/npm/p5@1.0.0/lib/p5.js"></script>
    <script src="script.js"></script>
    <title>My new website</title>
  </head>

  <body>
    <h1>Welcome to my website!</h1>
    <p class="warning">Warning: this page is under construction!</p>
    <p>This is where you can write about all of your favorite things</p>
    <p>Click <a href="https://textfile.io">here</a> to visit my favorite website</p>
    <img src="images/grumpy-cat.jpg" alt="a picture of a frowning cat">
  </body>

</html>
{{< / highlight >}}

Additionally, let’s add a new section to our `styles.css` file to center our javascript canvas on the web page just like we did for our image.

{{< highlight CSS >}}
body {
  background-color: black;
  color: white;
  margin-left: 10%;
  margin-right: 10%;
  margin-top: 2%;
  margin-bottom: 2%;
}

h1 {
  color: green;
  text-align: center;
}

img {
  display: block;
  margin: auto;
  width: 50%;
}

canvas {
  display: block;
  margin: auto;
  margin-top: 2%;
  border: 1px solid grey;
}

.warning {
  background-color: red;
  color: white;
  border: 1px solid yellow;
  text-align: center;
  padding: 1%;
}
{{< / highlight >}}

Now that we have everything set up we can open our `script.js` file and get started.


P5.js programs are primarily written inside of two important, built in functions. The `setup()` function is only run __once__ when the program first starts. The `draw()` function runs continuously in a __loop__ for the entire time the program is running. Open up your `script.js` file and add these two functions.

{{< highlight javascript >}}
function setup() {

}

function draw() {

}	
{{< / highlight >}}

The first thing we need to do is create a canvas that will store and display our project. This is done using the `createCanvas()` function which takes `width` and `height` arguments. For these arguments we can use a built in variable from the P5.js framework - `windowWidth` which is automatically set to the current width of your browser window. While we’re at it, let’s add a new function to resize our canvas whenever the browser window is resized.

{{< highlight javascript >}}
function setup() {
  createcanvas(windowWidth/2, windowWidth/2);
}

function draw() {

}

function windowResized() {
  resizeCanvas(windowWidth/2, windowWidth/2);
}
{{< / highlight >}}

Now we have a Javascript canvas using P5.js that is automatically resized to a square that is half the width of our browser window and is automatically centered on our screen using CSS.

![added javascript canvas to website](/media/add-canvas.png)

----

## Chapter Seven

### Interactivity


First, let's set the background color of our javascript canvas so that we can see it more clearly. To do this we can use the built-in function `background()`. The background function takes an __RGB__ color which is made up of three numbers, each between 0 and 255. The first number determines how much __red__ is in the color, the second number determines how much __green__ is in the color, and the third number determines how much __blue__ is in the color. For example  0, 0, 0 is black, 255, 255, 255 is white, 0, 0, 255 is blue, and  238, 130, 238 is a nice shade of purple. {{<sidenote>}}Google has an interactive color picker that allows you to copy the RGB value of any color you choose. You can access it by googling "[Color Picker](https://www.google.com/search?q=color+picker)".
{{</sidenote>}}


Choose your favorite color and set the background to it.

{{< highlight js >}}
function setup() {
  createCanvas(windowWidth/2, windowWidth/2);
}

function draw() {
  background(238, 130, 238);
}

function windowResized() {
  resizeCanvas(windowWidth/2, windowWidth/2);
  background(238, 130, 238);
}
{{< / highlight >}}

We can use a few built in functions to draw shapes on the canvas. Two of the most useful shape functions are `rect()` and `ellipse()` which both take four arguments - `X position`, `Y position`, `width`, and `height`.
Before we can use these functions it helps to understand the coordinates system of the canvas.

{{< highlight text >}}
    +-------------->  X increases
            
+   +---------------------------+
|   | X = 0           Y = 0     |
|   | Y = 0           X = width |
|   |                           |
|   |                           |
|   |                           |
|   |                           |
|   |                           |
|   |                           |
|   | X = 0          X = width  |
|   | Y = height     Y = height |
v   +---------------------------+
    
Y increases
{{< / highlight >}}

In P5.js, coordinate (0, 0) is the top left corner of the canvas and the bottom right corner of the canvas is the full width and full height value (in our case this would be `windowWidth/2` for both X and Y).

In your `script.js` file add the following two lines to draw a rectangle and an ellipse on your screen.

{{< highlight javascript >}}
function setup() {
  createCanvas(windowWidth/2, windowWidth/2);
}

function draw() {
  background(238, 130, 238);

  rect(10, 10, 100, 100);
  ellipse(width/2, height/2, 20, 20);
}

function windowResized() {
  resizeCanvas(windowWidth/2, windowWidth/2);
  background(238, 130, 238);
}
{{< / highlight >}}

You should see a square in the upper left of your canvas and a circle in the center of your canvas. You might also have noticed that when drawing the ellipse we used `width/2` and `height/2` for the X and Y position values. These variables are automatically set to the current width and height of your canvas and are updated when the browser window changes size. Try resizing your window and you’ll notice that the circle always stays in the center. Similarly, if you were to change the ellipse function to

{{< highlight javascript >}}
ellipse(width/2, height/2, width/15, height/15);
{{< / highlight >}}

The ellipse will stay the same size relative to the canvas whenever it is resized.

To change the fill and outline color of shapes we can use the functions `fill()` and `stroke()` which both take RGB color values.

{{< highlight javascript >}}
function setup() {
  createCanvas(windowWidth/2, windowWidth/2);
}

function draw() {
  background(238, 130, 238);

  stroke(100, 50, 75);
  fill(75, 180, 90);
  rect(10, 10, 100, 100);

  stroke(120, 220, 100);
  fill(50, 150, 200);
  ellipse(width/2, height/2, width/15, height/15);
}

function windowResized() {
  resizeCanvas(windowWidth/2, windowWidth/2);
  background(238, 130, 238);
}
{{< / highlight >}}

What if we wanted to be able to interact with the shapes we drew? That is totally possible and it’s one of the things that makes P5.js exciting to use. Try changing your `ellipse()` line to

{{< highlight javascript >}}
ellipse(mouseX, mouseY, width/15, height/15);
{{< / highlight >}}

The ellipse should now follow your mouse as you move it around the canvas!

{{< rawhtml >}}
<video muted playsinline controls poster="/media/interactive.png" src="/media/interactive.mp4"></video>
{{< / rawhtml >}}

----

## Chapter Eight

### Draw!

Currently, the background color of the canvas is redrawn every frame before we draw our shapes. Can you guess what would happen if we only drew the background once? Move your `background()` call out of the `draw()` function and into the `setup()` function then refresh your page.

<!--<video controls loop src="media/draw.mp4"></video>-->

Congratulations, you’ve just made your own simple drawing program! This opens up a whole new world of possibilities. For example, what if you wanted to change your pen color to a new, random, color every time we pressed the spacebar key.

To do this we are going to need to learn a little bit about __variables__, __arrays__, and __if statements__. Let’s make some changes to our `script.js` file.

{{< highlight javascript >}}
let penColor;
let allColors;

function setup() {
  createCanvas(windowWidth/2, windowWidth/2);
  background(238, 130, 238);

  allColors = [color(42, 163, 250), color(180, 59, 245),
              color(255, 79, 111), color(92, 255, 133)];

  penColor = color(50, 150, 200);
}

function draw() {
  noStroke();
  fill(penColor);
  ellipse(mouseX, mouseY, width/15, height/15);
}

function windowResized() {
  resizeCanvas(windowWidth/2, windowWidth/2);
  background(238, 130, 238);
}

function keyPressed() {
  if (keyCode === 32) {
    penColor = random(allColors);
  }
}
{{< / highlight >}}

On the first two lines, before our `setup()` function, we are defining some __global variables__ - `penColor` and `allColors`. Inside of our `setup()` function we assigned `penColor` to the initial color we want to draw with and we assigned `allColors` to an __array__ of all of the colors we want to randomly pick from later on. An array can be thought of as a __list of values or variables__. At the end of our script we added a new function that is called every time you press any key on your keyboard. Since we would only like to change the pen’s color when the spacebar key is pressed we need to use an __if statement__. `KeyCode 32` is the signal your computer sends to the web browser when you press the spacebar key on your keyboard{{<sidenote>}}You can use [keycode.info](https://keycode.info) to check what value is sent for each key on your keyboard.{{</sidenote>}} so inside of the if statement we can check if the spacebar key is pressed and, if so, we’ll set the pen color to a random color chosen from our `allColors` array.

{{< rawhtml >}}
<video muted playsinline controls poster="/media/random-color.png" src="/media/random-color.mp4"></video>
{{< / rawhtml >}}



----

## Chapter Nine

### Animate it

In P5.js you have a lot of power and flexibility to program your own animations. In this script we will use the `sin()` function with a constantly increasing variable (`frameCount`) in order to make an animation that loops fluidly.

Additionally, we can use the `mouseX` and `mouseY` variables with the `map()` function to change the background color of our canvas depending on where our mouse is positioned inside of the canvas. The `map()` function takes five arguments: an input variable, the current minimum and maximum value for the input, and a new minimum and maximum value that you would like to translate your variable to.

{{< highlight text >}}
  input var   input max   new max
          ^        ^      ^
          |        |      |
          |        |      |
          +        +      +
    map(input, 0, 20, 0, 10);
               +      +
               |      |
               |      |
               v      v
       input min.     new min.
{{< / highlight >}}

For example, if you have a variable `input` that has the value of __5__ `map(input, 0, 10, 0, 20)` would output the number __10__. This is especially useful for keeping variables constrained to specific ranges like `0-255` for RGB colors and `0-width` or `0-height` in order to keep shapes contained inside of the canvas. In this case we will be using the `map()` function to translate the variables `mouseX` and `mouseY`, which originally can be any number from `0-width` and `0-height`, to a number between `0-255` so that it can be used as an RGB color.

In a new `script.js` file we can try all of this out.

{{< highlight javascript >}}
function setup() {
  createCanvas(windowWidth/2, windowWidth/2);
}

function draw() {
  let redValue = map(mouseX, 0, width, 0, 255);
  let blueValue = map(mouseY, 0, height, 0, 255);
  let greenValue = map(mouseX + mouseY, 0, width+height, 0, 255);
  
  background(redValue, greenValue, blueValue);
  
  let myWidth = 300+(sin(frameCount/25)*70);
  let myHeight = 300+(sin(frameCount/15)*50);
  
  noStroke();
  fill(50, 150, 200);
  ellipse(width/2, height/2, myWidth, myHeight);
}

function windowResized() {
  resizeCanvas(windowWidth/2, windowWidth/2);
  background(238, 130, 238);
}
{{< / highlight >}}

Once you refresh your page you should see an ellipse in the center of the canvas that constantly warps and changes shape. As you move your mouse around the canvas you should also see that the background color changes accordingly.

{{< rawhtml >}}
<video muted playsinline controls poster="/media/change-color.png" src="/media/change-color.mp4"></video>
{{< / rawhtml >}}

To take this further you can even combine your shape-changing animation code with your mouse tracking code from earlier in order to have the ellipse both constantly animate while also changing shape based off of where your mouse is on the web page. If you want to try this out change your `myWidth` and `myHeight` variables to the following code.

{{< highlight javascript >}}
let myWidth = 100+(sin(frameCount/25)*70)+
              (map(mouseX, 0, width, width/4, width/2));
let myHeight = 100+(sin(frameCount/15)*50)+
              (map(mouseY, 0, height, height/4, height/2));
{{< / highlight >}}

You should also try changing the magic numbers{{<sidenote>}}In general, it isn't a great idea to use plain numbers that aren't assigned variable names in your code because it makes your code more difficult to understand when it's read by others. You can learn more about "magic numbers" [here](https://en.wikipedia.org/wiki/Magic_number_(programming)#Unnamed_numerical_constants).{{</sidenote>}} in these lines. For example the number we are adding to the entire result (100 in this case), the number we are dividing `frameCount` by, and the number that we are multiplying the result of the `sin()` function by. I only chose these specific numbers because I think it makes the result look interesting but that is totally subjective! Making changes to these values will drastically change the animation in a way that might be even more interesting.

{{< rawhtml >}}
<video muted playsinline controls poster="/media/change-shape.png" src="/media/change-shape.mp4"></video>
{{< / rawhtml >}}

----

## Chapter Ten

### Neural networks

P5.js becomes even more powerful when you start exploring the vast world of javascript libraries that are available. We can build our own instagram-style face tracking programs inside of our web page using the [Clmtrackr](https://github.com/auduno/clmtrackr) library. This library can take video from your computer's webcam which it compares to a pre-trained face model and then it output the location of various face features to javascript for you to use however you would like.

Before we can get started we need to import the library and a face tracking model in our `index.html` file.

{{< highlight HTML >}}
<html>

  <head>
    <link href="styles.css" rel="stylesheet" type="text/css">
    <script src="script.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/p5@1.0.0/lib/p5.js"></script>
    <script src="https://cdn.glitch.com/c97b301d-1a0f-4b50-b52f-d3b2c1209e4e%2Fclmtrackr.js?v=1587054210381"></script>
    <script src="https://cdn.glitch.com/c97b301d-1a0f-4b50-b52f-d3b2c1209e4e%2Fmodel_pca_20_svm.js?v=1587054236696"></script>
    <script src="https://cdn.glitch.com/c97b301d-1a0f-4b50-b52f-d3b2c1209e4e%2Fworkshop-utils.js?v=1587054509356"></script>
    <title>My new website</title>
  </head>

  <body>
    <h1>Welcome to my website!</h1>
    <p class="warning">Warning: this page is under construction!</p>
    <p>This is where you can write about all of your favorite things</p>
    <p>Click <a href="https://textfile.io">here</a> to visit my favorite website</p>
    <img src="images/grumpy-cat.jpg" alt="a picture of a frowning cat">
  </body>

</html>
{{< / highlight >}}

Once the library and model are imported we can start building our program in the `script.js` file. Firstly, we need to define two global variables: one to define a `button` element that will active the webcam when it is clicked and a __boolean__ variable (a boolean is a variable type that can have the value of either `true` or `false`) named `videoStarted` which will keep track of whether or not our button was pressed. 

{{< highlight JS >}}
let button;
let videoStarted = false;
{{< / highlight >}}


Next we can start writing our `setup()` function. Just like in our previous scripts we are going to create a canvas to display the output of our program. Additionally, we'll create an HTML button that is attached to our `button` variable and apply some CSS style options to it. On the last line we're going to define the name of a function we would like to call when this button is pressed.

{{< highlight JS >}}
function setup() {
  canvas = createCanvas(windowWidth/2, windowWidth/2);

  noStroke();
  background(255, 213, 135);

  button = createButton('start video');
  button.size(100, 50);
  button.style('background-color', color(0, 143, 51));
  button.style('color', color(255));
  button.style('border-style', "none");
  button.style('border-radius', "5px");
  button.style('font-size', "15px");

  button.mousePressed(startVideo);
}
{{< / highlight >}}

When the button is pressed it will call the `startVideo()` function which first sets the `videoStarted` variable to `true` then it hides the HTML button so that it can't be pressed again. Once this is complete we start capturing video from the webcam, hide it from the webpage, and connect it to our `clmtrackr` object. 

{{< highlight JS >}}
function startVideo(){
  videoStarted = true;

  button.remove();

  videoInput = createCapture(VIDEO);
  videoInput.size(400, 300);
  videoInput.position(0, 0);

  videoInput.id("v");
  var mv = document.getElementById("v");
  mv.muted = true;

  videoInput.hide();
  
  ctracker = new clm.tracker();
  ctracker.init(pModel);
  ctracker.start(videoInput.elt);
}
{{< / highlight >}}

Our `draw()` function is pretty simple. All we need to do is check if the `videoStarted` variable is `true` and, if so, clear the screen and re-draw the background. All of the face tracking logic is handled by the `getPositions()` function which is built into the `clmtrackr` library. All that's left for us to do is to draw with the data `clmtrackr` provides us which we'll do in the `drawElements()` function.

{{< highlight JS >}}
function draw() {
  if (videoStarted == true){
    clear();
    background(255, 213, 135);

    getPositions();
    drawElements();
  }
}
{{< / highlight >}}

The `drawElements()` is where we will do most of our work. After checking that `clmtrackr` has supplied its `positions` array with a list of points we can start creating __vector__ variable for different facial features. You can think of vectors as arrays that allow us to store both the X and Y positions of the features we would like to track. 

{{< highlight JS >}}
function drawElements() {
  if (positions.length > 0) {
    var eye1pos = createVector(positions[27][0], positions[27][1]);
    var eye2pos = createVector(positions[32][0], positions[32][1]);
    var nosepos = createVector(positions[41][0], positions[41][1]);
    var mouthpos = createVector(positions[57][0], positions[57][1]);
  }
{{< / highlight >}}

Once we have these variables defined it would be helpful to draw the basic shape of our face which we'll do in the `drawFaceOutline()` function. We can calculate the size, position, and rotation of our head using the list of positions `clmtrackr` gives us. 

{{< highlight JS >}}
function drawFaceOutline() {
  stroke(255, 0, 0);

  push();
  var p1 = createVector(positions[7][0], positions[7][1]);
  var p2 = createVector(positions[33][0], positions[33][1]);
  translate(positions[37][0], positions[37][1]);

  var angleRad = Math.atan2(p2.y - p1.y, p2.x - p1.x);
  rotate(angleRad + PI / 2);

  var mSize = p1.dist(p2);
  ellipse(0, -10, mSize * 1.3, mSize * 1.5);
  pop();
}
{{< / highlight >}}

Back in the `drawElements()` function all that's left to do is draw some interesting shapes for each feature we would like to represent.

{{< highlight JS >}}
// eyes
fill(0, 255, 0);
ellipse(eye1pos.x, eye1pos.y, 15, 20);
ellipse(eye2pos.x, eye2pos.y, 15, 20);
fill(0);
ellipse(eye1pos.x, eye1pos.y, 5, 5);
ellipse(eye2pos.x, eye2pos.y, 5, 5);

// nose
fill(0, 0, 255);
triangle(
  nosepos.x,
  nosepos.y,
  nosepos.x - (nosepos.x - eye1pos.x) / 2,
  nosepos.y + (nosepos.x - eye1pos.x),
  nosepos.x + (nosepos.x - eye1pos.x) / 2,
  nosepos.y + (nosepos.x - eye1pos.x)
);

// mouth
fill(255, 255, 0);
ellipse(mouthpos.x, mouthpos.y, 20, 10);
{{< / highlight >}}

We can even draw features that we don't have specific variables for by approximating their location based off of known points.

{{< highlight JS >}}
// hair
fill(255, 0, 0);
bezier(
  eye1pos.x - (eye2pos.x - eye1pos.x),
  eye1pos.y - (eye2pos.x - eye1pos.x) / 2,
  eye1pos.x - (eye2pos.x - eye1pos.x),
  eye2pos.y - (eye2pos.x - eye1pos.x) * 2,
  eye2pos.x + (eye2pos.x - eye1pos.x),
  eye2pos.y - (eye2pos.x - eye1pos.x) * 2,
  eye2pos.x + (eye2pos.x - eye1pos.x),
  eye2pos.y - (eye2pos.x - eye1pos.x) / 2
);
{{< / highlight >}}

All of this is just experimentation with a lot of trial and error but that is where a lot of the fun comes from! For an exercise try drawing really wacky hair with the [curve() function](https://p5js.org/reference/#/p5/curve) or try to draw ears. For an extra challenge you can even draw a mouth that changes its shape when you smile or frown.

Here is our complete `script.js` file.

{{< highlight JS >}}
let button;
let videoStarted = false;

function setup() {
  canvas = createCanvas(windowWidth/2, windowWidth/2);

  noStroke();
  background(255, 213, 135);

  button = createButton('start video');
  button.size(100, 50);
  button.style('background-color', color(0, 143, 51));
  button.style('color', color(255));
  button.style('border-style', "none");
  button.style('border-radius', "5px");
  button.style('font-size', "15px");

  button.mousePressed(startVideo);
}

function startVideo(){
  videoStarted = true;

  button.remove();

  videoInput = createCapture(VIDEO);
  videoInput.size(400, 300);
  videoInput.position(0, 0);

  videoInput.id("v");
  var mv = document.getElementById("v");
  mv.muted = true;

  videoInput.hide();

  ctracker = new clm.tracker();
  ctracker.init(pModel);
  ctracker.start(videoInput.elt);
}

function draw() {
  if (videoStarted == true){
    clear();
    background(255, 213, 135);

    getPositions();
    drawElements();
  }
}

function drawElements() {
  push();

  fill(0, 255, 255);

  if (positions.length > 0) {
    var eye1pos = createVector(positions[27][0], positions[27][1]);
    var eye2pos = createVector(positions[32][0], positions[32][1]);
    var nosepos = createVector(positions[41][0], positions[41][1]);
    var mouthpos = createVector(positions[57][0], positions[57][1]);

    // face outline
    drawFaceOutline();

    // hair
    fill(255, 0, 0);
    bezier(
      eye1pos.x - (eye2pos.x - eye1pos.x),
      eye1pos.y - (eye2pos.x - eye1pos.x) / 2,
      eye1pos.x - (eye2pos.x - eye1pos.x),
      eye2pos.y - (eye2pos.x - eye1pos.x) * 2,
      eye2pos.x + (eye2pos.x - eye1pos.x),
      eye2pos.y - (eye2pos.x - eye1pos.x) * 2,
      eye2pos.x + (eye2pos.x - eye1pos.x),
      eye2pos.y - (eye2pos.x - eye1pos.x) / 2
    );

    // eyes
    fill(0, 255, 0);
    ellipse(eye1pos.x, eye1pos.y, 15, 20);
    ellipse(eye2pos.x, eye2pos.y, 15, 20);
    fill(0);
    ellipse(eye1pos.x, eye1pos.y, 5, 5);
    ellipse(eye2pos.x, eye2pos.y, 5, 5);

    // nose
    fill(0, 0, 255);
    triangle(
      nosepos.x,
      nosepos.y,
      nosepos.x - (nosepos.x - eye1pos.x) / 2,
      nosepos.y + (nosepos.x - eye1pos.x),
      nosepos.x + (nosepos.x - eye1pos.x) / 2,
      nosepos.y + (nosepos.x - eye1pos.x)
    );

    // mouth
    fill(255, 255, 0);
    ellipse(mouthpos.x, mouthpos.y, 20, 10);
  }

  pop();
}

function drawFaceOutline() {
  stroke(255, 0, 0);

  push();
  var p1 = createVector(positions[7][0], positions[7][1]);
  var p2 = createVector(positions[33][0], positions[33][1]);

  translate(positions[37][0], positions[37][1]);

  var angleRad = Math.atan2(p2.y - p1.y, p2.x - p1.x);
  rotate(angleRad + PI / 2);

  var mSize = p1.dist(p2);
  ellipse(0, -10, mSize * 1.3, mSize * 1.5);
  pop();
}

function windowResized() {
  resizeCanvas(windowWidth/2, windowWidth/2);
  background(255, 213, 135);
}
{{< / highlight >}}


{{< rawhtml >}}
<video muted playsinline controls poster="/media/face-tracking.png" src="/media/face-tracking.mp4"></video>
{{< / rawhtml >}}

----

## Moving forward

Throughout course we covered the basics of building your own website from scratch and creating interactive programs using javascript but there is still so much more to learn if you are interested. In my opinion the most incredible thing about the internet is that everything is completely open to freely learn from. In any web browser all you need to do is right click on a web page and click `inspect` and then you can see all of the code that was written to create that website.

<!-- ![inspect](/media/inspect.png) -->




<!-- ![dev-tools](/media/dev-tools.png) -->

 This is an incredibly valuable resource because you can learn how __every website on the entire internet__ was put together. So go forward and learn from the billions of pages on the internet and then use that knowledge to make something even better.
