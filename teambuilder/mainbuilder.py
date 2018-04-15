'main'
from teambuilder import builderio, builder, shininglive, account

def display_teams():
  event_songs = my_event_play.event.setlist
  

def update():
  return

def usage():
  print("Usage:")
  print("  -excel <teambuilderfile>")
  print("     builds based on an original teambuilder sheet")
  print("  -csv <song file> <event info> <card list> <play profile>")
  print("     builds based on csv files")
  print("  -convert <excel file> [-outfiles <song file> <event file> <card file> <play profile file>] | [-outdir <directory>]")
  print("     converts from excel teambuilder to csv files, to specified files or directory, or current directory")
  print("  -update <update type> <csv file>")
  print("     update type = card, song, event, profile")
  print("       updates csv files for cards, songs, event, or play profile")
  print("  -h")
  print("     displays this message")
  print()

# need csv for song list, card list, profile, or excel builder
def main(argv):
  action = argv[1]
  if action == "-excel" or action == "-convert":
    excelbook = builderio.load(argv[2])
    my_cards = builderio.read_excel_cards(excelbook)
    #print(excelbook.sheetnames())
    builderio.read_excel_songs(excelbook, 'Song Database')
    print(shininglive.SONG_LIST)
    my_event = builderio.read_excel_event(excelbook, 'Settings')
    my_profile = builderio.read_excel_profile(excelbook, 'Settings')
    if action == "-convert":
      builderio.write_csv_cards(my_cards)
      builderio.write_csv_songs(shininglive.SONG_LIST)
      builderio.write_csv_event(my_event)
      builderio.write_csv_profile(my_profile)
      return
  elif action == "-csv":
    my_cards = builderio.read_csv_cards
  elif action == "-update":
    update_type = argv[2]
    update_file = argv[3]
    update(update_type, update_file)
  else:
    usage()
    return
  my_profile.cardlist = my_cards
  my_event_play = account.EventPlay(my_profile, my_event)
  my_teams = build(event_play)
  display_teams(my_event_play, my_teams)
    
if __name__ == "__main__":
  import sys
  main(sys.argv)