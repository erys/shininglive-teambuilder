"""Objects related to an individual Shining Live Account"""

from . import shininglive

class PlayProfile:
  """
  Individual note profile for one song difficulty.
  """
  
  def __init__(self, song, difficulty):
    self.song = song
    self.difficulty = difficulty
    self.miss = 0
    """Number of misses"""
    
    self.bad = 0
    """Number of bads"""
    
    self.good = 0
    """Number of goods"""
    
    self.great = 0
    """Number of greats"""
    
    self.perfect = self.song.notes.get(self.difficulty, 0)
    """
    Number of perfects, always derived from the total note count
    of the song, and the sum of the other note types
    """
  
  def total_count(self):
    return self.song.notes.get(self.difficulty, 0)
  
  def update_counts(self, great = 0, good = 0, bad = 0, miss = 0):
    """Updates the note counts, perfect is derived from the other counts"""
    
    self.great = great
    self.good = good
    self.bad = bad
    self.miss = miss
    self.perfect = self.total_count() - (miss + bad + good + great)
       
  def is_valid(self):
    """Validats note counts"""
    
    return self.miss >= 0 and (self.bad >= 0 and
      (self.good >= 0 and (self.great >= 0 and (self.perfect >=0
      and ((self.miss + self.bad + self.good + 
      self.great + self.perfect) == self.total_count())))))
      
def create_auto_profile(song, difficulty
  """Returns a profile for auto-playing a song (all goods)"""
  
  auto_profile = PlayProfile(song, difficulty)
  auto_profile.update_counts(0, auto_profile.total_count(), 0, 0)
  return auto_profile
      
class Profile:
  "An object representing the cards and play methods for an account"
  def __init__(self):
    cardlist = {} # key is card name
    songprofile = {}
    for song in shininglive.SONG_LIST.values():
      songprofile[song] = (PlayProfile(song, 'hard'), PlayProfile(song, 'pro'))

class EventPlay:
  "An object representing an individual's event play"
  def __init__(self, profile, event):
    self.event = event
    self.profile = profile
    self.play_profiles = {}
    self.auto_profiles = {}
    
    for song in self.event.setlist:
      self.play_profiles[song] = self.profile.songprofile.get(song, None)
      self.auto_profiles = (create_auto_profile(song, 'hard'),
        create_auto_profile(song, 'pro'))
    
    setlength = len(self.event.setlist)
    self.points = {
      ('hard', 'manual') : [0] * setlength,
      ('pro', 'manual') : [0] * setlength,
      ('hard', 'auto') : [0] * setlength,
      ('pro', 'auto') : [0] * setlength
      }

  def get_best_boost_profile(self, difficulty, play_type, mission = 'normal'): # TODO
    boost_profile = [1] * 7
    evpoints = self.points[(difficulty, play_type)]
    