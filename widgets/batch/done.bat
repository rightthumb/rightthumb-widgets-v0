@echo off

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

echo Done
call p. done
goto:eof
if [%myHome%] == [] call %userprofile%\cc.bat
if [%1] == [] ( call p. done ) else ( call p. done -song %1)

goto:eof



rem set mplayer=D:\Program Files (x86)\Windows Media Player\wmplayer.exe
set mFolder=D:\_Scott\S_Music
set mplayer=%techdrive%:\techApps\VLCPortable\VLCPortable.exe
set mFolder=%techdrive%:\techApps\MP3

set song01=Katherine Jenkins\2011 - Daydream\13. Abigail's Song (Bonus Track).mp3
set song02=Ludovico Einaudi\Ludovico Einaudi - Nuvole Bianche.mp3
rem set song03=Andrea Bocelli\Romanza - Andrea - Bocelli - Say Goodbye.mp3
rem set song04=Jewel\Misc\(Jewel) - Foolish Games.mp3
set song05=Less Than Jake\Hello Rockview\01. Last One Out of Liberty City.mp3
set song06=louis_armstrong_-_somewhere_over_the_rainbow.mp3
rem set song07=My Chemical Romance\My Chemical Romance - Im Not Okay (I Promise) (1).mp3
rem set song08=Saved\George Strait - All My Ex's Live In Texas.mp3
rem set song09=Smashing Pumpkins\Soft\3. Today.mp3
rem set song10=Smashing Pumpkins\Soft\13. Luna.mp3
rem set song11=Smashing Pumpkins\Soft\2. Tonight, Tonight.mp3
rem set song12=Smashing Pumpkins\Soft\14. For Martha.mp3
rem set song13=Smashing Pumpkins\Hard\6. Disarm.mp3
rem set song14=Smashing Pumpkins\Hard\4. Hummer.mp3
rem set song15=The Cranberries\Cranberries - Linger.mp3
rem set song16=The Cranberries\The Cranberries - Zombie.mp3
rem set song17=Slick Shoes\Rusty\Slick Shoes - Cliche.mp3
rem set song19=Slick Shoes\Rusty\Slick Shoes - Feeble.mp3
set song20=Metalica\Fuel - Metallica [HD] [1080p].mp3
set song21=Metalica\Metallica - Fade to Black.mp3
set song22=Metalica\Metallica - Sad But True [Official Music Video].mp3
set song23=Metalica\Metallica - The Unforgiven (Video).mp3
rem set song20=
rem set song99=tapeatalk_records\Time lord treachery.mp3

set song=%song02%


	


start "%mplayer%" "%mFolder%\%song%"