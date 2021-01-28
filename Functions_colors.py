#this library associates colours to the functions, calling functions here means pulling up my custom colors
#the colors here have to be set in hexadecimal

#here are all the colours set in the dictionary for every single funcion of the twelve
colours = {"Communicate" : "#f5be8b",
    "Kill enemies" : "#f93571",
    "Standby mode" : "#72cadc",
    "Fight worms" : "#b5cd64",
    "Cause inflammation" : "#ec725d",
    "Activate other cells" : "#f0bb4d",
    "Produce antibodies" : "#00a1de",
    "Kill infected cells" : "#f685cc",
    "Strategic decisions" : "#e8dbd8",
    "Remember enemies" : "#8850b5",
    "Mark/disable enemies 1" : "#4bb4be",
    "Mark/disable enemies 2" : "#06e0cb"
}

#here there are the cells functions all stored in a dictionary

cellsFunction = {"Macrophage" : ["Kill enemies", "Cause inflammation", "Activate other cells", "Communicate"],
    "Neutrofile" : ["Kill enemies", "Activate other cells"],
    "Natural killer cell" : ["Kill enemies" , "communicate"]
    "Complement" : ["Mark/disable enemies 1"],
    "Mast cell" : [""],
    "Monocyte" : [""],
    "Follicular dendritic cell" : ["Activate other cells"],
    "Dendritic cell" : ["Activate other cells", "Cause inflammation"]
}


#CELL SCHEME
    #	_____________________________________________________________________________________________________________________________________________________
    #	-	Macrophage					Neutrophil				Natural Killer Cell		Complement		Mast Cell			Monocyte
    #		1-2-5-6						6-2						1-2						11				1-4-5-6				3-2-9
    #
    #	-	Follicular Dend. Cell		Dendritic Cell			Memory helper T Cell	Bosophil		Eosinophil			Virgin Helper T Cell	
    #		6							6-5						1-10-6					6-5-4			5-4-6				3-6
    #
    #	-	Helper T Cell				Mem Helper Stem T Cell	Virgin Killer T Cell	Antibodies		Killer T Cell		Memory Killer T Cell
    #		1-6							1-10					3-8						12				8					10-8
    #
    #	-	Virgin B Cell				B Cell					Memory B Cell			Memory B Stem Cell					Mem Killer Stem Cell
    #		7-3							7-6						10-7					10-7								10-8
    #	‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    #	__________________________________________________________________________________
    #	-	1. Communicate		5. Cause inflammation	9.  Strategic decisions
    #    -	2. Kill enemies		6. Activate other cells	10. remember enemies
	#    -	3. stanby mode		7. produce antibodies	11. mark/disable enemies 1
    #	-	4. fight worms		8. kill infected cells	12. mark/disable enemies 2
	#    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾