  # colors intro
A repository to store color palettes for plots in all programming languages and programs. 
The focus is on schemes that are perceptually uniform and were designed with 
colorblindness in mind. This
repository is meant to be accessible on multiple levels, whether you are just starting out 
in a particular programming language or a seasoned veteran. Each program is divided into two
sections, the "copy paste" method and the "integrated" solution.  The "copy and paste" method 
will allow you to copy and paste a few lines of code to make your work colorblind friendly. 
The "integrated" solution will change the default plot options for a program so that it will 
always create material that is colorblind friendly.

The first step in implementing any of these is to first send an email to the provider of your 
software and request that they change the default sequence to be colorblind friendly. The 
majority of the population will only use them if they are the defaults, and only the software 
providers can accomplish this.  

# Sources
Credit should be given where it is due. I have not developed any of these color schemes, I am 
merely trying to organize them into a format that is easily accessible for all creators. The 
following is a list of sources where I got these palettes. They are organized roughly by when 
I became aware of them.

1. [http://mk.bcgsc.ca/colorblind/#10home](https://mk.bcgsc.ca/colorblind/#l0home) - Martin Krzywinski (also [http://mk.bcgsc.ca/brewer/](https://mk.bcgsc.ca/brewer/))
2. [http://colorbrewer2.org/](http://colorbrewer2.org/) - Cynthia Brewer and Mark Harrower
3. [https://sronpersonalpages.nl/~pault](https://sronpersonalpages.nl/~pault/) - Paul Tol
4. [https://github.com/mpetroff/accessible-color-cycles?tab=readme-ov-file](https://github.com/mpetroff/accessible-color-cycles?tab=readme-ov-file) - Matthew Pettroff

# Raw RGB Values
1. Okabe and Ito (https://jfly.uni-koeln.de/color/)

<img alt="ColorPalette" src="https://raw.githubusercontent.com/ahrendsen/colorblind/master/wong2011.png">

| Color name | R (dec) | G (dec) | B (dec) | R (hex) | G (hex) | B (hex) | RGB (hex) | RGBA (hex) | 
|   ---      |  ---    |   ---   |   ---   | --- |      --- |    ---      | --- | --- |
| Black      | 0       |  0      |   0     | 00  | 00 | 00 | 000000 | 000000ff | 
| Orange     | 230     | 159     | 0       |  e6 | 9f | 00 | e69f00 | e69f00ff | 
| Sky blue   | 86      | 180     | 233     |56   | b4 | e9 | 56b4e9 | 56b4e9ff | 
| Bluish green | 0 | 158 | 115 |              00 | 9e | 73 | 009e73 | 009e73ff |
| Yellow | 240 | 228 | 66 |                   f0 | e4 | 42 | f0e442 | f0e442ff |
| Blue | 0 | 114 | 178 |                      00 | 72 | b2 | 0072b2 | 0072b2ff | 
| Vermillion | 213 | 94 | 0 |                 d5 | 5e | 00 | d55e00 | d55e00ff |
| Reddish purple | 204 | 121 | 167 |          cc | 79 | a7 | cc79a7 | cc79a7ff |

2. Martin K. 12 Alt

<img width="1367" height="170" alt="image" src="https://github.com/user-attachments/assets/aa6f2198-de32-43d3-bd54-8c2d9c51ae68" />

|Name|R (dec)|G (dec)|B (dec)|R (hex)|G (hex)|B (hex)|RGB (hex)|RGBA (hex)|
|---|---|---|---|---|---|---|---|---|
|genoa|0.0|106.0|94.0|0|6A|5E|006A5E|006A5EFF|
|deeppink|237.0|13.0|136.0|ED|0D|88|ED0D88|ED0D88FF|
|tealish|0.0|189.0|169.0|0|BD|A9|00BDA9|00BDA9FF|
|palecrimson|255.0|196.0|212.0|FF|C4|D4|FFC4D4|FFC4D4FF|
|ceruleanblue|0.0|88.0|204.0|0|58|CC|0058CC|0058CCFF|
|hotpurple|210.0|8.0|251.0|D2|8|FB|D208FB|D208FBFF|
|pinkflamingo|255.0|102.0|253.0|FF|66|FD|FF66FD|FF66FDFF|
|turquoise|0.0|239.0|249.0|0|EF|F9|00EFF9|00EFF9FF|
|japaneselaurel|21.0|109.0|3.0|15|6D|3|156D03|156D03FF|
|islamicgreen|0.0|151.0|25.0|0|97|19|009719|009719FF|
|permanentgreen|0.0|198.0|27.0|0|C6|1B|00C61B|00C61BFF|
|luminous|0.0|251.0|29.0|0|FB|1D|00FB1D|00FB1DFF|

# Program Implementations
For all of these implementations, I will provide the text input for the Wong 2011 palette on
this page.
In the future, I hope to have a python script that will allow for generation of any of 
the palettes in any of the languages.
## matplotlib
There are so many ways to define colors in matplotlib, this will likely always be a work in progress. Pull requests with your favorite way to define colors are welcome.
### Copy and Paste (PyPlot)
Execute the following two commands before your plot statements, and the default color sequence will be set to Okabe and Ito.
```
ax = plt.axes()
ax.set_prop_cycle(color=['000000','e69f00','56b4e9','009e73','f0e442','0072b2','d55e00','cc79a7'])
```
### Integrated
We need to put a few lines of code into the [matplotlibrc file](https://matplotlib.org/stable/users/explain/customizing.html#the-matplotlibrc-file). This probably doesn't exist, so you'll need to make it in the proper directory. Consult the link above to be sure, but in your home directory, there should be a folder called ".matplotlib". It might be hidden so make sure to unhide files and folder in your folder view settings. Inside that folder, make a new file called "matplotlib.txt". Open that file and paste in the following text.
```
axes.prop_cycle: cycler('color', ['000000','e69f00','56b4e9','009e73','f0e442','0072b2','d55e00','cc79a7'])
```
Save the file, then change the name of the file, removing the ".txt" extension at the end. You'll get a warning message, say "Yes" you're sure you want to change it. If you need to edit the file later, you can just add the ".txt" extension back to the file to be able to open it in a text editor.

## Mathematica
Mathematica is where I do the majority of my work, so it will be the first program to be filled out.
### Copy and Paste

To any plot, add the paste in the following list of colors as the argument for `PlotStyle`
For example: `ListPlot[{{1,2,3},{4,5,6}},PlotStyle->{RGBColor[0/255,0/255,0/255],...}]`

```Mathematica
{RGBColor[0/255,0/255,0/255], (* Black *)
RGBColor[230/255,159/255,0], (* Orange *)
RGBColor[86/255,180/255,233/255], (* Light Blue *)
RGBColor[0/255,158/255,115/255], (* Teal *)
RGBColor[240/255,228/255,66/255], (* Yellow *)
RGBColor[0/255,114/255,178/255], (* Royal Blue *)
RGBColor[213/255,94/255,0/255], (* Vermillion *)
RGBColor[204/255,121/255,167/255] (* Pink *)
}
```
### Integrated
Every time the Mathematica Kernel starts, it runs the commands stored in an initialization file. We can store commands within this file and cause the default plot color sequence to be the colorblind palette. First, find the location of the Kernel folder on your installation. Regardless of the platform you're on, you can find this with `SystemOpen@FileNameJoin[{$UserBaseDirectory, "Kernel"}]`
Then place [this file](https://github.com/ahrendsen/colorblind/blob/master/init.m) in the directory you found. 

If Mathematica is currently running, either kill the Kernel or close out of Mathematica and open it back up and your default color sequence should be set. 

I think there has to be an easier way to do this, so if you know of one, please inform me!

## gnuplot

I do a small amount of auto-generation of plots in gnuplot. Since it's text based, the copy paste and integrated solutions are essentially the same.

### Copy and Paste

If you have a gnuplot script that is generating the plots, copy and paste these commands into the script above where the plot is generated.

Gnuplot version 5 introduced the `podo` color sequence, which is the Okabe and Ito color sequence. If you are in Gnuplot 5 you can simply set the color sequence to `podo` like this:

```gnuplot
set colorsequence podo
```

On older versions of Gnuplot specify the colors manually:

```gnuplot
set linetype 1 lc rgb 0x000000 lw 2
set linetype 2 lc rgb 0xe69f00 lw 2
set linetype 3 lc rgb 0x56b4e9 lw 2
set linetype 4 lc rgb 0x009e73 lw 2
set linetype 5 lc rgb 0xf0e442 lw 2
set linetype 6 lc rgb 0x0072b2 lw 2
set linetype 7 lc rgb 0xd55e00 lw 2
set linetype 8 lc rgb 0xcc79a7 lw 2
set linetype cycle 8
```

### Integrated

Copy and paste the following lines into the gnuplot configuration file, default location: "~/.gnuplot". This configuration file might also need to be copied to the root user's home directory "/root/.gnuplot", if you run scripts with root when you collect data. If you are on Gnuplot 5 use the `podo` color sequence:

```gnuplot
set colorsequence podo
```

Otherwise specify the colors manually:

```gnuplot
set linetype 1 lc rgb 0x000000 lw 2
set linetype 2 lc rgb 0xe69f00 lw 2
set linetype 3 lc rgb 0x56b4e9 lw 2
set linetype 4 lc rgb 0x009e73 lw 2
set linetype 5 lc rgb 0xf0e442 lw 2
set linetype 6 lc rgb 0x0072b2 lw 2
set linetype 7 lc rgb 0xd55e00 lw 2
set linetype 8 lc rgb 0xcc79a7 lw 2
set linetype cycle 8
```
  
## Inkscape
Inkscape is great for preparing 2D drawings, and is an alternative to Adobe Illustrator. 
### Copy and paste
Inkscape doesn't seem to have a place to copy and paste a list of RGB values. You can specify individual colors from the RGB values in the table above, but given the nature of editing on inkscape, I think it makes the most sense to just provide this image of the colors. 

<img alt="ColorPalette" src="https://raw.githubusercontent.com/ahrendsen/colorblind/master/wong2011.png">

Which can be copied and pasted into your inkscape file and then the eyedropper tool can be used to pick out the colors. 

### Integrated
Save [this file](inkscape/palettes/colorBlind.gpl) (right click link > "Save link as...") into the directory: 
 - On Windows: "C:\Program Files\Inkscape\share\palettes"
 
The next time you open Inkscape, you will be able to select the palette by clicking on the arrow in the bottom right hand corner next to the colors.

## Microsoft Products
Love it or hate it, it's probably the most popular program to create data visualizations. Though I tried, I couldn't seem to find a way to default the colors to a custom option. The best I can do is to configure the program so that it allows you to easily select the palette after the program has started.

### Copy and Paste
Save [this theme file](https://github.com/ahrendsen/colorblind/blob/master/Theme1.thmx) (right click link > "Save link as...") where you can find it, then in the Office Ribbon go to "Design > Themes > Browse for Themes" and select the file you just downloaded. 
### Integrated
Save [the same file as above](https://github.com/ahrendsen/colorblind/blob/master/Theme1.thmx) (right click link > "Save link as...") into the Templates directory. It can be found at (make sure "hidden items" are shown) "<User Folder>\AppData\Roaming\Microsoft\Templates\Document Themes". Now whenever you open a Microsoft product, you should be able to go to "Design > Themes > Theme1" and have access to the colors.

