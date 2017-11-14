#Script will take a document property (in this case one which is entered in a text box by the user) and tag marked rows with the value of the document property
#The script first assesses if the tag group contains the text as a tag, if not it will add the tag, it then applies the tag to the marked rows


from Spotfire.Dxp.Application.Visuals import *
from Spotfire.Dxp.Data import *
from System.Collections.Generic import *
from Spotfire.Dxp.Data import DataColumn, TagsColumn



Comment = Document.Properties["NAME OF DOCUMENT PROPERTY WITH VALUE TO TAG"]
print Comment
for X in Document.Data.Tables:
	if X.Name == 'YOUR TABLE NAME':
		try:
			myTagColumn = X.Columns.Item['YOUR TAG COLUMN'].As[TagsColumn]()
			CommentArray = myTagColumn.TagValues
			CA = set(CommentArray)
			print CA
			if Comment not in CA:
				print "not there"
				myTagColumn.TagValues = List[str](CA.union([Comment]))
		except:
			print 'fail tag add'

# Tag the marked rows
markedRowSelection = Document.ActiveMarkingSelectionReference.GetSelection(Document.Data.Tables["UD Data"]) #gets marked rows from named table
table = Document.Data.Tables["YOUR TABLE NAME"] #is all like, this is the table man
myTagColumn = table.Columns.Item[YOUR TAG COLUMN"].As[TagsColumn]() #is all like, this column dude


selectRows = IndexSet(table.RowCount, True)
myTagColumn.Tag(Comment, markedRowSelection )





