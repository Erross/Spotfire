#Script to force the spotfire visualization pane to size appropriately to display relatively high resolution content on shitty monitors
#This doesn't work for switching to projectors as it takes the screen bounds at startup rather than current
#Generally requires some sort of trigger onload or such from javascript to work - can trigger this through a document property change


import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import *
from Spotfire.Dxp.Application.Layout import *
from System.Drawing import *

print Screen.PrimaryScreen.WorkingArea

widths = Screen.PrimaryScreen.Bounds.Width
heights = Screen.PrimaryScreen.Bounds.Height


if heights < 800 and widths > 1200:
	Document.Pages.VisualizationAreaSize.FitToWindow = False
	Document.Pages.VisualizationAreaSize.Size = Size(widths,900)

if heights > 800 and widths <1200:
	Document.Pages.VisualizationAreaSize.FitToWindow = False
	Document.Pages.VisualizationAreaSize.Size = Size(1100,heights)

if heights < 800 and widths <1200:
	Document.Pages.VisualizationAreaSize.FitToWindow = False
	Document.Pages.VisualizationAreaSize.Size = Size(1100,900)

if heights > 800 and widths >1200:
	Document.Pages.VisualizationAreaSize.FitToWindow = True



