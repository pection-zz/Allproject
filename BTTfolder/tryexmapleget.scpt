tell application "BetterTouchTool"
	try
		set dndEnabled to get_string_variable "customVariable2"
		set dndEnabled2 to get_string_variable "customVariable3"
	end try
		if dndEnabled is not dndEnabled2
			set_string_variable "customVartiable3" to dndEnabled
			set_string_variable "customVartiable1" to "songchange"
		else
			set_string_variable "customVartiable1" to "songnotchange"
		end if
end tell