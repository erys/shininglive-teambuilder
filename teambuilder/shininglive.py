"""General classes for single objects in shininglive."""
from enum import Enum
from math import ceil

class Color(Enum):
  RED = 1
  BLUE = 2
  YELLOW = 3
  NONE = 4
  
  def __str__(self):
    return self.name.capitalize()

  def is_valid(self):
    return self.value != 4
    
class Rarity(Enum):
  UR = .6
  SR = .5
  R = .4
  N = 0
  
  def __str__(self):
    return self.name
    
class Type(Enum):
  DANCE = 0
  VOCAL = 1
  CHARM = 2
  ACT = 2
  NONE = 3
  
  def __str__(self):
    return self.name.capitalize()
  
  def is_valid(self):
    return self != Type.NONE    

class Boy(Enum):
  OTOYA = 0
  MASATO = 1
  NATSUKI = 2
  TOKIYA = 3
  REN = 4
  SYO = 5
  CECIL = 6
  REIJI = 7
  RANMARU = 8
  AI = 9
  CAMUS = 10
  NOBODY = 11
  
  def is_valid(self):
    return self != Boy.NOBODY
    
  def __str__(self):
    return self.name.capitalize()


class SkillType(Enum):
  CUTIN = ('percent', ['Cut In Bonus'])
  PERFECT = ('percent', ['Perfect Score Up', 'Just Perfect Score Up'])
  SCORENOTE = ('notes', ['Add Score Notes'])
  GOODLOCK = ('notes', ['Bad to Good', 'Bad to Great'])
  GREATLOCK = ('notes', ['Bad Good to Great', 'Bad Great to Perfect'])
  LIFENOTE = ('notes', ['Add Life Notes'])
  NONE = ('', [''])
  
  def __str__(self):
    return self.value[1][0]
    
class Skill:
  
  def __init__(self, skill_type=SkillType.NONE, skill_magnitude=0):
    self.skill_type = skill_type
    self.skill_magnitude = skill_magnitude
    
  def __str__(self):
    if self.skill_type.value[0] == 'percent':
      return '{0} +{1}%'.format(self.skill_type, self.skill_magnitude*100)
    else:
      return '{0} +{1}'.format(self.skill_type, self.skill_magnitude)
    
  def is_valid(self):
    return (self.skill_type != SkillType.NONE) and (self.skill_magnitude > 0)
   
class Photo:
  """A single photo"""
  
  def __init__(self):
    self.name = ''
    self.color = Color.NONE
    self.attributes = {
      Type.DANCE : 0,
      Type.VOCAL : 0,
      Type.CHARM : 0
    }
    self.type = Type.NONE
    self.skill = Skill()
    self.boy = Boy.NOBODY
    self.rarity = Rarity.N
    
  def __str__(self):
    return "<{0}, {1}, {2}, {3}, [{4}, {5}, {6}], {7}, {8}>".format(self.name, self.rarity, self.boy, self.color, self.attributes[Type.DANCE], self.attributes[Type.VOCAL], self.attributes[Type.CHARM], self.skill, self.type)
  
  def base_total(self):
    return sum(self.attributes.values())
    
  def get_bonus(self, rarity, type):
    if type.is_valid() and rarity != Rarity.N:
      return self.attributes[type] * rarity.value
    return 0
  
  def get_bonus_from_photo(self, leader):
    return self.get_bonus(leader.rarity, leader.type)
  
  def get_attributes(self, song, event_type=Type.NONE):
    total = self.base_total()
    if self.color == song.color:
      total += .3 * self.base_total()
    total += self.attributes.get(event_type, 0)
    if self.boy in song.singers:
      total += .1 * self.base_total()
    return total

class Song:
  def __init__(self):
    self.name = ''
    self.singers = set()
    self.color = Color.NONE
    self.notes = {'hard' : 0, 'pro' : 0}
   
  def is_valid(self):
    return self.color != Color.NONE

# keys are song names
SONG_LIST = {}

HARD_CAP = [ceil(470 * (1 + 0.15 * x)) for x in range(7)]

MISSION_POINTS = {
  ('hard', 'fc') : 400,
  ('hard', 'normal') : 350,
  ('pro', 'fc') : 500,
  ('pro', 'normal') : 450
  }

class Event:
  def __init__(self):
    self.name = ''
    self.reward = Boy.NOBODY
    self.type = Type.NONE
    self.setlist = []

  
    
    
    
    
  