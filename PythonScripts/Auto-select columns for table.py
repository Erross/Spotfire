###This code will autopopulate columns in a table to allow for visualizations which are reactive to the dataset inserted
###Requires that a table of column names also be supplied when the main data is inserted
import System
import Spotfire.Dxp.Application
import Spotfire.Dxp.Data
from Spotfire.Dxp.Application.Visuals import *
from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Application.Visuals import TablePlot, VisualContent
from System import Array
from System.Collections.Generic import *
from Spotfire.Dxp.Data import DataColumn, TagsColumn
from Spotfire.Dxp.Data import DataPropertyClass, DataType, DataValueCursor, IDataColumn, IndexSet
from Spotfire.Dxp.Data import RowSelection


# Define a dictionary (lookup hash essentially)
dicty = {}
# define the confing table
tableName = 'Config_Table'
# Define the columns to return
columnToFetch = 'Order'
columnToFetch2 = 'ColumnName'
# Define the active table reference
activeTable = Document.Data.Tables[tableName]
# establish size of table
rowCount = activeTable.RowCount
# include all rows
rowsToInclude = IndexSet(rowCount, True)
# define cursors to extract values
cursor1 = DataValueCursor.CreateFormatted(activeTable.Columns[columnToFetch])
cursor2 = DataValueCursor.CreateFormatted(activeTable.Columns[columnToFetch2])

# loop through table to pick up all values and add to dictionary
for row in activeTable.GetRows(rowsToInclude, cursor1, cursor2):
    rowIndex = row.Index
    val1 = cursor1.CurrentValue
    val2 = cursor2.CurrentValue
    dicty.update({val1: val2})
# establish length of dictionary
N = len(dicty)
# create the order array
order = []
# build the order array using dictionary lookup
for x in range(0, N):
    y = str(x + 1)
    b = dicty.get(y)
    # print b
    order.append(b)
# order is established. Use order to build table

#First piece of code here will force columns in 'forced_columns' to appear first
forced_columns = ['col1', 'col2', 'col3', 'col4']

for page in Application.Document.Pages:
    if 'partial page name identifier' in page.Title:
        for vis in page.Visuals:
            if vis.Title == 'Name of visualization to change':
                dt = vis.As[VisualContent]()
                cols = dt.Data.DataTableReference.Columns
                dt.TableColumns.Clear()
                for val in forced_columns:
                    try:
                        dt.TableColumns.Remove(cols[val])
                        dt.TableColumns.Add(cols[val])
                    except:
                        print'fail to add forced column to table'
                        print val
dynamic_columns = order

for page in Application.Document.Pages:
    if 'partial page name identifier' in page.Title:
        for vis in page.Visuals:
            if vis.Title == 'Name of visualization to change':
                dt = vis.As[VisualContent]()
                cols = dt.Data.DataTableReference.Columns

                for val in dynamic_columns:
                    try:
                        dt.TableColumns.Remove(cols[val])
                        dt.TableColumns.Add(cols[val])
                    except:
                        print'fail to add dynamic column to table'
                        print val

                    table = vis.As[VisualContent]()
                    ### This next piece of code forces columns widths on the new table
                    for col in table.TableColumns:
                        if col.Name == 'wide column1' or col.Name == 'wide column2':
                            col.Width = 150
                        else:
                            col.Width = 70