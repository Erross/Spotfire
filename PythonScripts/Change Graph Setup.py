#This script is used to switch a graph from one set of columns to another as a spacesaver
#Switches Graph A to Graph B - 4 metrics on X axis, Y axis is set to -5/5 range

import System
import Spotfire.Dxp.Application
import Spotfire.Dxp.Data
from Spotfire.Dxp.Application.Visuals import ScatterPlot, BarChart
from Spotfire.Dxp.Application.Visuals import AxisRange

for vis in Document.ActivePageReference.Visuals:
    sp = vis.As[BarChart]()

    if vis.Title == "GRAPH NAME A" or vis.Title == "GRAPH NAME B":
        sp = vis.As[BarChart]()
        if vis.Title == "GRAPH NAME B":
            sp.YAxis.Expression = "Sum([METRIC1 A]) as [M1A], Sum([METRIC2 A]) as [M2A], Sum([METRIC3 A]) as [M3A], Sum([Metric4 A]) as [M4A]"
            sp.XAxis.Expression = '<[Axis.Default.Names]>'
            sp.ColorAxis.Expression = '<[Axis.Default.Names] as [Metric]>'
            vis.Title = "GRAPH NAME B"
            sp.YAxis.Range = AxisRange(-5, 5) #here force the graph to have an axis range that works for your data
            print sp.YAxis.Range
        elif vis.Title == "GRAPH NAME A":
            sp.YAxis.Expression = "Sum([METRIC1 B]) as [M1B], Sum([METRIC2 B]) as [M2B], Sum([METRIC3 B]) as [M3B], Sum([Metric4 B]) as [M4B]"
            sp.XAxis.Expression = '<[Axis.Default.Names]>'
            sp.ColorAxis.Expression = '<[Axis.Default.Names] as [Metric]>'
            vis.Title = "GRAPH NAME B"
            sp.YAxis.Range = AxisRange(-5, 5)  # here force the graph to have an axis range that works for your data