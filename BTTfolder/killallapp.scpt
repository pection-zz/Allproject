tell application "System Events"
    set listOfProcesses to (name of every process where background only is false)
    tell me to set selectedProcesses to choose from list listOfProcesses with multiple selections allowed
end tell
return listOfProcesses
--The variable `selectedProcesses` will contain the list of selected items.
repeat with processName in selectedProcesses
    --do shell script "Killall " & quoted form of processName
end repeat
