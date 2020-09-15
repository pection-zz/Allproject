try
	--@yuuiko: Get User Preference
	tell application "BetterTouchTool"
		try
			set UsrPref_CS_Highlighting to get_string_variable "customVariable3"
		end try
		if UsrPref_CS_Highlighting is "ON" then
			set_string_variable "customVariable3" to "OFF"
		else
			set_string_variable "customVariable3" to "ON"
		end if
		return UsrPref_CS_Highlighting
	end tell
end try