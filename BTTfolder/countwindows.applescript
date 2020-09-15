
if application "Google Chrome" is running then 
	tell application "Google Chrome"
		try
			set chromecount to count every tab of every window
		on error
			set chromecount to 8
		end try
	end tell
end if
if application "Safari" is running then 
	tell application "Safari"
		try
			set safaricount to count every tab of every window
		on error
			set safaricount to 8
		end try
	end tell
end if


set summary to chromecount + safaricount
set tabcount to summary
if tabcount > 8 then
	set tabcount to 8
end if
set title to "\"text\":\"" & "{icons} " & "\""
set tabpath to "\"icon_path\":\"~/Documents/BTTiconchrome copy/" & (tabcount as string) & ".png\""
return "{" & title & "," & tabpath & "}"