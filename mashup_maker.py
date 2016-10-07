import sys, getopt
from pydub import AudioSegment
import random 

class Mashup_Maker():
	
	def __init__(self, songs):
		self.SECOND = 1000
		self.MIN_SEG_LEN = 2
		self.MAX_SEG_LEN = 8
	
		self.mashup_title = "mashup"	
		self.songs = []
		for i in range(0, len(songs)):
			song_title  = songs[i]
			self.mashup_title += ("_" + song_title.split(".")[0]) #this way the file doesnt have an extra underscore at the end
			self.songs.append(self.open_song(song_title))

		self.get_min_len()



	def open_song(self, file_name):
		# Opens the song file using pydub
		s_type = file_name.split(".")[1]
		s = AudioSegment.from_file(file_name, s_type)
		return s

	def get_min_len(self):
		# Finds the song with the minimum length
		self.min_len = len(self.songs[0])
		self.short_song_index = 0 
		for i in range(len(self.songs)):
			if len(self.songs[i]) < self.min_len:
				self.min_len = len(self.songs[i])
				self.short_song_index = i
		
	def mash(self):
		# Mashes random segments from each song
		self.pos = 0
		self.mashup = self.get_song_seg(0)
		self.seg_count = 1
		while self.pos < self.min_len:
			print self.seg_count
			curr_song_index = self.seg_count % len(self.songs)
			seg = self.get_song_seg(curr_song_index)
			self.seg_count +=1
			self.mashup = self.mashup.append(seg, crossfade=100) 
		self.mashup.export(self.mashup_title + ".mp3", format="mp3")

	def mash_tape(self, tape_length):
		# Mashes random segments from each song into a mixtape of tape_length
		#this feature is not ready for prime time yet
		self.pos = 0
		self.mashup = self.get_song_seg(0)
		self.seg_count = 1
		while self.pos < tape_length:
			print self.seg_count
			curr_song_index = self.seg_count % len(self.songs)
			seg = self.get_song_seg(curr_song_index)
			self.seg_count +=1
			self.mashup = self.mashup.append(seg, crossfade=100) 
		self.mashup.export(self.mashup_title + ".mp3", format="mp3")

	def get_song_seg(self, song_index):
		# Gets a random segment of the indexed song 
		seg_len = random.randint(self.MIN_SEG_LEN, self.MAX_SEG_LEN)*self.SECOND
		if self.pos + seg_len > self.min_len:
			# If this segment would put us over the end of the shortest song, finish the mashup with that song
			seg = self.songs[self.short_song_index][self.pos:]
		else:
			# Grab a random segment from the song
			seg = self.songs[song_index][self.pos:self.pos + seg_len]
		self.pos += seg_len
		return seg

if __name__ == '__main__':
	song_paths = []
	tape_length = 0
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hs:l:",["song=","length="])
	except getopt.GetoptError:
		print 'mashup_maker.py -s <song1> -s <song2> -s <song3> -l <mixtape length>'
		sys.exit(2)
	for opt, arg in opts:
		print 'opt is '+ opt
		print 'arg is' + arg
   		if opt == '-h':
			print 'just figure it out for yourself'
		 	sys.exit()
	  	elif opt in ("-s", "--song"):
			song_paths.append(arg)
	  	elif opt in ("-l", "--length"):
	  		print "warning, this feature is not really ready yet"
			tape_length = arg
	print song_paths

	if tape_length == 0:
		mashup_maker = Mashup_Maker(song_paths)
		mashup_maker.mash()
	else:
		mashup_maker = Mashup_Maker(song_paths)
		mashup_maker.mash_tape(tape_length)

