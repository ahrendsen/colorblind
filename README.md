# colorblind intro
A repository to store colorblind palettes for plots in all programming languages and programs. This
repository is meant to be accessible on multiple levels, whether you are just starting out 
in a particular programming language or a seasoned veteran. Each program is divided into two
sections, the "copy paste" method and the "integrated" solution.  The "copy and paste" method 
will allow you to copy and paste a few lines of code to make your work colorblind friendly. 
The "integrated" solution will change the default plot options for a program so that it will 
always create material that is colorblind friendly.

The first step in implementing any of these is to first send an email to the provider of your software and request that they change the default sequence to be colorblind friendly. The majority of the population will only use them if they are the defaults, and only the software providers can accomplish this.  

# Sources
Credit should be given where it is due. I have not developed any of these color schemes, I am merely trying to organize them into a format that is easily accessible for all creators. The following is a list of sources where I got these palettes. They are organized roughly by when I became aware of them.

1. http://mkweb.bcgsc.ca/colorblind/ - Martin Krzywinski (also http://mkweb.bcgsc.ca/brewer/)
2. http://colorbrewer2.org/ - Cynthia Brewer and Mark Harrower
3. https://personal.sron.nl/~pault/ - Paul Tol

# Raw RGB Values
1. Wong 2011

| Color name | R (dec) | G (dec) | B (dec) | R (hex) | G (hex) | B (hex) | RGB (hex) |
|   ---      |  ---    |   ---   |   ---   | --- |      --- |    ---      | --- |
| Black      | 0       |  0      |   0     | 00  | 00 | 00 | 000000 | 
| Orange | 230 | 159 | 0 |                    e6 | 9f | 00 | e69f00 | 
| Sky blue | 86 | 180 | 233 |                 56 | b4 | e9 | 56b4e9 | 
| Bluish green | 0 | 158 | 115 |              00 | 9e | 73 | 009e73 |
| Yellow | 240 | 228 | 66 |                   f0 | e4 | 42 | f0e442 |
| Blue | 0 | 114 | 178 |                      00 | 72 | b2 | 0072b2 | 
| Vermillion | 213 | 94 | 0 |                 d5 | 5e | 00 | d55e00 |
| Reddish purple | 204 | 121 | 167 |          cc | 79 | a7 | cc79a7 |

# Program Implementations
For all of these implementations, I will provide the text input for the Wong 2011 palette on
this page.
In the future, I hope to have a python script that will allow for generation of any of 
the palettes in any of the languages.
## Mathematica
Mathematica is where I do the majority of my work, so it will be the first program to be filled out.
### Copy and Paste

To any plot, add the paste in the following list of colors as the argument for `PlotStyle`
For example: `ListPlot[{{1,2,3},{4,5,6}},PlotStyle->{RGBColor[0/255,0/255,0/255],...}]`


  {RGBColor[0/255,0/255,0/255], (\* Black \*)
  RBBColor[230/255,159/255,0], (\* Orange \*)
  RGBColor[86/255,180/255,233/255], (\* Light Blue \*)
  RGBColor[0/255,158/255,115/255], (\* Teal \*)
  RGBColor[240/255,228/255,66/255], (\* Yellow \*)
  RGBColor[0/255,114/255,178/255], (\* Royal Blue \*)
  RGBColor[213/255,94/255,0/255], (\* Vermillion \*)
  RGBColor[204/255,121/255,167/255] (\* Pink \*)
  }
  
## gnuplot
I do a small amount of auto-generation of plots in gnuplot. Since it's text based, the copy paste and integrated solutions are essentially the same.
### Copy and Paste
If you have a gnuplot script that is generating the plots, copy and paste these commands into the script above where the plot is generated.


  set linetype 1 lc rgb 0x000000 lw 2
  
  set linetype 2 lc rgb 0xe69f00 lw 2
  
  set linetype 3 lc rgb 0x56b4e9 lw 2
  
  set linetype 4 lc rgb 0x009e73 lw 2
  
  set linetype 5 lc rgb 0xf0e442 lw 2
  
  set linetype 6 lc rgb 0x0072b2 lw 2
  
  set linetype 7 lc rgb 0xd55e00 lw 2
  
  set linetype 8 lc rgb 0xcc79a7 lw 2
  
  set	linetype cycle 8

### Integrated
Copy and paste the following lines into the gnuplot configuration file, default location: "~/.gnuplot". This configuration file might also need to be copied to the root user's home directory "/root/.gnuplot", if you run scripts with root when you collect data.

  set linetype 1 lc rgb 0x000000 lw 2
  
  set linetype 2 lc rgb 0xe69f00 lw 2
  
  set linetype 3 lc rgb 0x56b4e9 lw 2
  
  set linetype 4 lc rgb 0x009e73 lw 2
    
  set linetype 5 lc rgb 0xf0e442 lw 2
  
  set linetype 6 lc rgb 0x0072b2 lw 2
  
  set linetype 7 lc rgb 0xd55e00 lw 2
  
  set linetype 8 lc rgb 0xcc79a7 lw 2
  
  set	linetype cycle 8
  
## Inkscape
Inkscape is great for preparing 2D drawings, and is an alternative to Adobe Illustrator. 
### Copy and paste
Inkscape doesn't seem to have a place to copy and paste a list of RGB values. You can specify individual colors from the RGB values in the table above, but given the nature of editing on inkscape, I think it makes the most sense to just provide this image of the colors. 
<img alt="ColorPalette" src="https://raw.githubusercontent.com/ahrendsen/colorblind/master/wong2011.png">
### Integrated
Save [this file](https://github.com/ahrendsen/colorblind/raw/master/colorBlind.gpl) into the directory: 
 - On Windows: "C:\Program Files\Inkscape\share\palettes"
The next time you open Inkscape, you will be able to select the palette by clicking on the arrow in the bottom right hand corner next to the colors.




