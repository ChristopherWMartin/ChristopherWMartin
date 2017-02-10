---
layout: post
title: Machine Learning
description: research into GANs
img: /img/moving_InProgress1.png
---
The first GAN was trained for 5,000 epochs on two classes containing 100 images each.

Example of the 'Ohio' class:

![]({{site.baseurl}}/img/ohio1.jpg)

<hr>

Example of the 'Chicago' class:

![]({{site.baseurl}}/img/chicago1.jpg)

<hr>

After 1050 epochs I was able to generate an image that could be understood as a landscape. I then asked the net to extrapolate the image into a panorama -- the result is understandably repetitive.

![]({{site.baseurl}}/img/moving_InProgress1.png)

<hr>

3,950 epochs later the resulting images are less of a Chicago+Ohio hybrid than a blending together of the images of each descrete class.

![]({{site.baseurl}}/img/1_ne1x_ne4x.png)

<hr>

![]({{site.baseurl}}/img/2_ne1x_ne4x.png)

<hr>
<hr>

Next, I trained a GAN for 5,600 epochs on 4,000 screen recorded frames of four different 3D models:

1

![]({{site.baseurl}}/img/3d1.png)

<hr>

2

![]({{site.baseurl}}/img/3d2.png)

<hr>

3

![]({{site.baseurl}}/img/3d3.png)

<hr>

4

![]({{site.baseurl}}/img/3d4.png)

<hr>

After 500 epochs:

![]({{site.baseurl}}/img/3d_InProgress.png)

<hr>

The final result is much more clear than the landscape images:

![]({{site.baseurl}}/img/10_ne1x_ne4x.png)

<hr>
<hr>

Most recently, I trained on 1,000 photographs of light fixtures shot against either a static grey or white background.

<hr>

![]({{site.baseurl}}/img/lighting1.jpg)

<hr>

![]({{site.baseurl}}/img/lighting2.JPG)

<hr>

It seems to be clear that better results can be obtained when the subject is against an unchanging surface as the GAN is unable to differentiate between foreground v. background.

<hr>

166 epochs:

![]({{site.baseurl}}/img/lighting166.png)

<hr>

363 epochs:

![]({{site.baseurl}}/img/lighting363.png)

<hr>

781 epochs:

![]({{site.baseurl}}/img/lighting781.png)

<hr>

982 epochs:

![]({{site.baseurl}}/img/lighting982.png)

<hr>

I would like to explore this further as a tool for product design.