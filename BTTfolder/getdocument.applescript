set str to {}
if ((str is equal to str) and (application "Safari" is running)) then
    tell application "Safari"
        repeat with t in tabs of windows
            tell t
                if URL starts with "https://music.youtube.com" then
                    set artworkURL to do JavaScript "artwork= document.querySelectorAll('img.image.style-scope.ytmusic-player-bar')[0].src;"
                    -- set artworkURL2 to do JavaScript "artwork= document.querySelectorAll('img.image.style-scope.ytmusic-player-bar')[0].src;"

                    return artworkURL
                    do shell script "curl -O " & artworkURL & "~/youtube_cover.png"
                    set uri to "~/youtube_cover.png"
                end if
            end tell
        end repeat
    end tell
end if
