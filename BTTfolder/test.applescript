set itemsToDelete2 to {" ", "likes", "view", "views", "Home", "Hotlist", "Library", "Queue", "Videos", "Songs", "Plahiylists", "Artists", "Albums", "2017", "2018", "2020", "2019", "ไม่ได้ทำเพื่อการกุศล", "SUBSCRIBE", "YouTubeMusic", "2015", "2016", "SINGLE", "หน้าแรก", "เพลย์ลิสต์ใหม่มาแรง", "คลังเพลง", "มิกซ์สำหรับคุณ", "", "วิดีโอที่ชอบ", "เพลย์ลิสต์อัตโนมัติ", "", "มิกซ์ของคุณ", "เพลงต่อเนื่องที่ปรับเปลี่ยนในแบบของคุณ", "", "Discover Mix", "อัปเดตทุกวันพุธ", "รายการโปรด", "การดู", "ผู้ติดตาม", "อัลบั้ม", "วีดีโอที่ชอบ", "ค้นหา", "YouTubeMusic", "YouTube Music", "เพลย์ลิสต​์", "DiscoverMix", "คิว"}

set artistname to {"boyimagine", "เทียนไขและวานิช"}
set checkdup to {}
set containvaluelist to {"หมื่นครั้ง", "แสนครั้ง", "ล้านครั้ง", "ชอบ"}
set counttime to 0
set StartFind to "False"
set cleanartist4 to {}
set cleanartist2 to {}
set cleanartist3 to {}
set namesongsplit to {}
set nextsong to {}
set namesongsplit to {}
set artistsong to {}
set mike to {}
set str to "" as string

tell application "Safari"
	repeat with t in tabs of windows
		tell t
			if URL starts with "https://music.youtube.com" then
				set tmp2 to text of t as string
				set title2 to text 2 thru -1 of tmp2
				set StartFind to "True"
			end if
		end tell
	end repeat
end tell

if StartFind is "True" then
	-- set AppleScript's text item delimiters to " - YouTube Music"
	-- set namesong to text item 1 of title as string
	-- set AppleScript's text item delimiters to namesong
	set artist to paragraphs of title2
	repeat with i from 1 to length of artist
		repeat with j from 1 to length of itemsToDelete2
			set artist's item i to findAndReplaceInText(artist's item i, itemsToDelete2's item j, "")
			set artist's item i to findAndReplaceInText(artist's item i, "•", "")
		end repeat
	end repeat

	set cleanartist4 to removeItem(artist, itemsToDelete2)
	set Nowplaying to (getIndex of "แถบโปรแกรมเล่นเพลง" from cleanartist4) + 1
	repeat with i from Nowplaying to (length of cleanartist4)
		copy cleanartist4's item i to the end of the cleanartist2
	end repeat
	set cleanartist2 to addr(cleanartist2, checkdup)
	set Nowplayingsong to getIndex of (cleanartist2's item 2) from cleanartist4
	repeat with i from 1 to 3
		copy cleanartist4's item ((Nowplayingsong) + (i * 3)) to the end of the nextsong
	end repeat
	set cleanartist3 to removesplitText(cleanartist2, "-", cleanartist3, containvaluelist)
	repeat with i from 1 to length of (artistname)
		set artistnamevalue to "0"
		if cleanartist3's item 2 contains artistname's item i then
			set artistnamevalue to "1"
			exit repeat
		end if
	end repeat
	if artistnamevalue is "1" then
		copy cleanartist3's item 2 to the end of the artistsong
		copy cleanartist3's item 3 to the end of the namesongsplit
	else
		copy cleanartist3's item 3 to the end of the artistsong
		copy cleanartist3's item 2 to the end of the namesongsplit
	end if

	set namesongsplit to namesongsplit as text
	set artistsong to artistsong as text
	tell application "BetterTouchTool"
		set_string_variable "nowplayingstring" to cleanartist2's item 1 as text
		set_string_variable "namesongstring" to namesongsplit
		set_string_variable "artistsongstring" to artistsong
		repeat with i from 1 to length of nextsong
			set_string_variable "nextsong" & i to nextsong's item i
		end repeat
	end tell
end if
return "{\"text\":\"" & namesongsplit & "\\n {icon} - " & artistsong & "\",\"font_color\":\"255,255,255,255\",\"icon_path\":\"~/mike2.png\"}"

on name_matches(match_text)
	set match_words to words of match_text
	repeat with i from 1 to (count match_words)
		if nameOnDevice contains item i of match_words then
			return true
		end if
	end repeat
	return false
end name_matches
to getIndex of i from l
	set tid to text item delimiters
	set text item delimiters to return
	set l to return & l & return
	set text item delimiters to return & i & return
	tell l's text items to if (count) is 1 then
		set i to 0
	else
		set i to count item 1's paragraphs
	end if
	set text item delimiters to tid
	return i
end getIndex
on convertListToString(theList, theDelimiter)
	set AppleScript's text item delimiters to theDelimiter
	set theString to theList as string
	set AppleScript's text item delimiters to ""
	return theString
end convertListToString
on removeItem(theList, itemsToDelete)
	set cleanList to {}
	repeat with i from 1 to count theList
		if {theList's item i} is not in itemsToDelete then
			set cleanList's end to theList's item i
		end if
	end repeat
	return cleanList
end removeItem
on checkContain(theList, itemsToDelete)
	set cleanList to {}
	repeat with j from 1 to count theList
		repeat with i from 1 to count itemsToDelete
			if name_matches(theList's item j, itemsToDelete's item i) then
				exit repeat
			else
				set cleanList's end to theList's item j
			end if
		end repeat
	end repeat
	return cleanList
end checkContain
on splitText(theText, theDelimiter)
	set AppleScript's text item delimiters to theDelimiter
	set theTextItems to every text item of theText
	set AppleScript's text item delimiters to ""
	return theTextItems
end splitText
on removesplitText(listitem, removeItem, outputset, containitem)
	if class of listitem is string then
		set listitem to {listitem}
	end if
	if length of listitem is 1 then
		set outputset's end to listitem's item 1
		return outputset
	end if
	repeat with i from 1 to length of listitem
		if length of splitText(listitem's item i, removeItem) < 2 then
			set caches to "0"
			repeat with k from 1 to length of containitem
				if listitem's item i contains containitem's item k then
					set caches to "1"
					exit repeat
				end if
			end repeat
			if caches is "0" then
				set outputset's end to listitem's item i
			end if
		else
			repeat with j from 1 to length of splitText(listitem's item i, removeItem)
				set caches to "0"
				repeat with k from 1 to length of containitem
					if splitText(listitem's item i, removeItem)'s item j contains containitem's item k then
						set caches to "1"
						exit repeat
					end if
				end repeat
				if caches is "0" then
					set outputset's end to splitText(listitem's item i, removeItem)'s item j
				end if
			end repeat
		end if
	end repeat
	return outputset
end removesplitText
on findAndReplaceInText(theText, theSearchString, theReplacementString)
	set AppleScript's text item delimiters to theSearchString
	set theTextItems to every text item of theText
	set AppleScript's text item delimiters to theReplacementString
	set theText to theTextItems as string
	set AppleScript's text item delimiters to ""
	return theText
end findAndReplaceInText

to addr(l, c)
	script foo
		property foo2 : l
		property okAddresses : {}
	end script

	considering case
		repeat with i from 1 to count (foo's foo2)
			set x to ((foo's foo2)'s item i)
			if x is in foo's okAddresses then
				set end of c to x
			else
				set end of foo's okAddresses to x
			end if
		end repeat
	end considering
	foo's okAddresses
end addr
