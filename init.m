(* ::Package:: *)

(** User Mathematica initialization file **)

colorBlindPaletteNames={"Black","Orange","Light Blue","Teal","Yellow","Royal Blue","Vermillion","Pink"};
colorBlindPalette={
RGBColor[0/255,0/255,0/255], (* Black *)
RGBColor[230/255,159/255,0], (*Orange*)
RGBColor[86/255,180/255,233/255], (*Light Blue*)
RGBColor[0/255,158/255,115/255],(* Teal *)
RGBColor[240/255,228/255,66/255], (* Yellow *)
RGBColor[0/255,114/255,178/255],(* Royal Blue *)
RGBColor[213/255,94/255,0/255], (* Vermillion *)
RGBColor[204/255,121/255,167/255] (* Pink *)
};

SetOptions[{Plot,LogPlot,LogLogPlot,LogLinearPlot,
ListPlot,ListLogPlot,ListLogLogPlot,ListLogLinearPlot,
BarChart,Histogram},PlotStyle->colorBlindPalette,PlotMarkers->Automatic];
