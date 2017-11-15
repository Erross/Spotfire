# Spotfire Scripts
## Javascripts
### Accordion
Accordion.js provides the javascript for building an accordion menu <br>
which will repopulate on refresh in order to 'fix' broken filters which occured<br>
on the change to Spotfire 7.7

### javascript to push button on load
Script will push a button (by spotfire identifier, modify in script) to allow for actions to trigger on load of the text area (this occurs every time the page is navigated to) - good in synchronicity with the screen resolution fixer.py

## PythonScripts
### Change Graph Setup
Change Graph Setup.py provides a generic ironpython script which can be used to
change a graphs x axis properties and title - extensible with other graph related doodads

### Reset Discngine
In order to efficiently use the discngine connector it makes more sense to have each visualization
point to a specific form, rather than use the discngine provided menu structure. In order to do this 
a property must be maintained which keeps this linkage current

### Screen Resolution Fixer
Code to force the display size to be larger than the resolution on monitors where people have decided to run
a 1992 simulator

### Tag rows
Generic Script to tag rows - requires pre defined tags

### Tag rows with free text
Generic Script to tag rows with a user entered free text - defines tags on the fly (requires tag group to exist only)

### Trigger Data Function
Ironpython code to trigger a named data function

### Display altered filters
Ironpython code which will build HTML to inject into a text area (it does this inject) named Show_Filters - only shows modified filters for the filter scheme of the active page.

### Auto-select columns for table
Ironpython code which will take a column order from one table (name and order number 1 .. x) and rebuild the table viz to reflect the incoming data - includes code for forcing first columsn through hard code, adding ordered columns and then assigning width to the columns (default or forced to wider for known columns where this is required)


## R

### regression
This R code snippet will create parameters to use to plot regeression of 2 columns on a graph (intercept and slope of line as outputs)

### supsmu curve
supsu curve function for R in Spotfire - creates a supsmu curve dataset to plot on top of data
## HTML
### Left Side Slideout
This creates a text area which moves into and out of the left side of the screen onclick

### Right Side Slideout
This creates a text area which moves into and out of the right side of the screen onclick

