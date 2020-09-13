to clickID(theId) --creates a function that we can use over and over again instead of writing this code over and over again
	
	tell application "Safari" -- lets AppleScript know what program to controll
		
		do JavaScript "document.getElementById('" & theId & "').click();" in document 1 -- performs JavaScript code that clicks on the element of a specific id
		
	end tell -- tells Applescript you are done talking to Safari
	
end clickID -- lets AppleScript know we are done with the function
to clickClassName(theClassName, elementnum)
	
	tell application "Safari"
		
		do JavaScript "document.getElementsByClassName('" & theClassName & "')[" & elementnum & "].click();" in document 1
		
	end tell
	
end clickClassName

to clicktagName(thetagName, elementnum)
	
	tell application "Safari"
		
		do JavaScript "document.getElementsByTagName('" & thetagName & "')[" & elementnum & "].click();" in document 1
		
	end tell
	
end clicktagName

clickClassName("SnhBsb hrdBHb", 0)