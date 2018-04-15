"""
Functions for finding the best team for a given song,
and calculating score for a given team and song.
"""

from . import account, shininglive

class TeamPerSong:
  """
  Object used to represent an instance of a team played against a
  specific song, with a specific difficulty, event type, play profile,
  and guest.
  """
  
  def __init__(self, song):
    self.song = song
    self.boys = [NULL] * 7
    # 
    self.leaderindex = 0
    self.guestSkill = (shininglive.Rarity.NONE,
      shininglive.Type.NONE,
      shininglive.Color.NONE)
    
    
    

class PhotoSong(Photo):
  def __init__(self, originalPhoto):
    super(self)
    self.name = originalPhoto.name
    self.color = originalPhoto.color
    self.attributes = originalPhoto.attributes
    self.type = originalPhoto.type
    self.skill = originalPhoto.skill
    self.boy = originalPhoto.boy
    self.rarity = originalPhoto.rarity
    
    


def build(profile):
  return None
