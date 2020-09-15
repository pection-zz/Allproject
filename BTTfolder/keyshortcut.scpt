tell application "System Events"
	tell application "Safari" to activate
	keystroke "p" using shift down
	set visible of process "Safari" to false
end tell