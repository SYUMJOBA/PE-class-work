#this library associates colours to the functions, calling functions here means pulling up my custom colors
#the colors here have to be set in hexadecimal

#here are all the colours set in the dictionary for every single funcion of the twelve
colours = {"Communicate" : "#e1af5a",
    "Kill enemies" : "#e43d51",
    "Standby mode" : "#8acede",
    "Fight worms" : "#9db34a",
    "Cause inflammation" : "#ec794a",
    "Activate other cells" : "#f7cd47",
    "Produce antibodies" : "#399ae5",
    "Kill infected cells" : "#e473a5",
    "Strategic decisions" : "#ffffff",
    "Remember enemies" : "#8253a2",
    "Mark/disable enemies 1" : "#63a99f",
    "Mark/disable enemies 2" : "#57fbcd"
}

#here there are the cells functions all stored in a dictionary, it's not yet completed

cellsFunction = {"Macrophage" : ["Kill enemies", "Cause inflammation", "Activate other cells", "Communicate"],
    "Neutrophil" : ["Kill enemies", "Activate other cells"],
    "Natural killer cell" : ["Kill enemies" , "Communicate"],
    "Complement" : ["Mark/disable enemies 1"],
    "Mast cell" : [],
    "Monocyte" : [],
    "Follicular dendritic cell" : ["Activate other cells"],
    "Dendritic cell" : ["Activate other cells", "Cause inflammation"], # why does the video chow it defferently as [6, 9]???
    "Memory helper T cell" : [],
    "Bosophil" : [],
    "Eosinophil" : [],
    "Virgin helper T cell" : ["Standby mode", "Activate other cells"],
    "Helper T cell" : [],
    "Memory helper stem T cell" : [],
    "Virgin killer T cell" : ["Standby mode", "Kill infected cells"],
    "Antibodies" : ["Mark/disable enemies 2"],
    "Killer T cell" : ["Kill infected cells"],
    "Memory killer T cell" : [],
    "Virgin B cell" : [],
    "B cell" : ["Produce antibodies", "Activate other cells"],
    "Memory B cell" : ["Produce antibodies" , "Remember enemies"],
    "Memory B stem cell" : [],
    "Memory killer stem cell" : []

    #Kurzgesagt if you are seeing this, just know that I'm getting pretty confused ... 😅 and suprisingly emojis can be put in comments, I'm gonna take a break

}

UnDoneYet = 60
cellsSizes = {"Macrophage" : 60,
    "Neutrophil" : 30,
    "Natural killer cell" : 50,
    "Complement" : UnDoneYet,
    "Mast cell" : UnDoneYet,
    "Monocyte" : UnDoneYet,
    "Follicular dendritic cell" : 40,
    "Dendritic cell" : 50, # why does the video show it defferently as [6, 9] (talking about the function colors) ???
    "Memory helper T cell" : UnDoneYet,
    "Bosophil" : UnDoneYet,
    "Eosinophil" : UnDoneYet,
    "Virgin helper T cell" : UnDoneYet,
    "Helper T cell" : UnDoneYet,
    "Memory helper stem T cell" : UnDoneYet,
    "Virgin killer T cell" : UnDoneYet,
    "Antibodies" : 7,
    "Killer T cell" : UnDoneYet,
    "Memory killer T cell" : UnDoneYet,
    "Virgin B cell" : UnDoneYet,
    "B cell" : 75,
    "Memory B cell" : 75,
    "Memory B stem cell" : UnDoneYet,
    "Memory killer stem cell" : UnDoneYet

    #Kurzgesagt if you are seeing this, just know that I'm getting pretty confused ... 😅 and suprisingly emojis can be put in comments

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