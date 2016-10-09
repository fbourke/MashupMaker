# MashupMaker
Software to make only the best of audio mashups (aka randomly create mashups)

This incredibly complex algorithm uses a random number generator to create random mashups of songs. If it isn't clear, this is a joke and took 30 minutes. Don't judge. 

To run, download pydub http://pydub.com/ by running `pip install pydub`

`pmashup_maker.py [-r] -s <song1> -s <song2> -s <song3> ...` 

Use the `-r` flag if you want to take random smippets from songs, otherwise MaskupMaker will choose linear segments from each song (effectively switching back and forth between songs as they play).

I have had no issues using mp3's and m4a's and it should theoretically handle other file formats.  

The resulting mashup will be as long as the shortest song. It can handle any number of songs as long as the shortest song isn't shorter than approximately 4 seconds multipled by the number of songs.  

You can also attempt to use the -l flag and specify the length of the mashup in milliseconds, but going over the length of the shortest song is currently not supported.