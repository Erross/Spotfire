#When using discngine in spotfire it is better to force spotfire to the base form rather than use the discngine menu
#This script forces the DiscngineWebPanelURL document property to always return to the right start form so saves
#Dont screw everything up

Document.Properties["DiscngineWebPanelURL"] = [URL FOR PILOT PROTOCOL CREATING BASE FORM]