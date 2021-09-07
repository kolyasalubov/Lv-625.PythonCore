def are_you_playing_banjo(name):
  s = name.lower()
  if s[0] == 'r':
    return f'{name} plays banjo'
  else:
    return f'{name} does not play banjo'

r="Tick"
r=are_you_playing_banjo(r)
print(r)
