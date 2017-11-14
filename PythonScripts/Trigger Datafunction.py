#Script to trigger a data function - needs to have imports cleaned up somewhat, not all of these are needed

from Spotfire.Dxp.Data.DataFunctions import DataFunctionExecutorService, DataFunctionInvocation, DataFunctionInvocationBuilder
import System
import Spotfire.Dxp.Application
import Spotfire.Dxp.Data
from Spotfire.Dxp.Data import *
from System.Collections.Generic import *


dataManager = Document.Data

for function in dataManager.DataFunctions:
	print function.Name
	if function.Name == 'Name of Data Function':
		dataFunction = function
		dataFunction.Execute()