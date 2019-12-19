# colorblind intro
A repository to store colorblind palettes for plots in all programming languages and programs. This
repository is meant to be accessible on multiple levels, whether you are just starting out 
in a particular programming language or a seasoned veteran. Each program is divided into two
sections, the "copy paste" method and the "integrated" solution.  The "copy and paste" method 
will allow you to copy and paste a few lines of code to make your work colorblind friendly. 
The "integrated" solution will change the default plot options for a program so that it will 
always create material that is colorblind friendly.

# Sources

# Raw RGB Values

# Program Implementations

## Mathematica
Mathematica is where I do the majority of my work, so it will be the first program to be filled out.
### Copy and Paste

To any plot, add the paste in the following list of colors as the argument for "PlotStyle"
For example: ListPlot[{{1,2,3},{4,5,6}},PlotStyle->{RGBColor[0/255],...}]


{RGBColor[0/255,0/255,0/255], (* Black *)

RBBColor[230/255,159/255,0], (*Orange*)

RGBColor[86/255,180/255,233/255], (*Light Blue*)

RGBColor[0/255,158/255,115/255],(* Teal *)

RGBColor[240/255,228/255,66/255], (* Yellow *)

RGBColor[0/255,114/255,178/255],(* Royal Blue *)

RGBColor[213/255,94/255,0/255], (* Vermillion *)

RGBColor[204/255,121/255,167/255] (* Pink *)

}


