#Code to tag marked rows in a named table
#For this code snippet the tags must be predefined or the script will fail

# Includes
from Spotfire.Dxp.Data import DataColumn, TagsColumn
from Spotfire.Dxp.Data import DataPropertyClass, DataType, DataValueCursor, IDataColumn, IndexSet
from Spotfire.Dxp.Data import RowSelection

# Tag the marked rows
markedRowSelection = Document.ActiveMarkingSelectionReference.GetSelection(Document.ActiveDataTableReference)
table = Document.ActiveDataTableReference
myTagColumn = table.Columns.Item["YOUR TABLE NAME"].As[TagsColumn]()

selectRows = IndexSet(table.RowCount, True)
myTagColumn.Tag("YOUR TAG NAME", markedRowSelection)
