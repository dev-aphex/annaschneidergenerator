import random
promi = ('NameA', 'NameB', 'NameC', 'NameD', 'NameE',)
rnd_promi = random.randint(0, len(promi)-1)

buzzword = ('woke', 'linke', 'gendernde', 'grüne', 'autohassende',)
rnd_buzzword = random.randint(0, len(buzzword)-1)

buzzword2 = ('die Demokratie', 'unsere Gesellschaft', 'Deutschland', 'alle Liberale', 'die Meinungsfreiheit',)
rnd_buzzword2 = random.randint(0, len(buzzword2)-1)

print(promi[rnd_promi] + " ist also ein Nazi. Das behauptet zumindest die " +
      buzzword[rnd_buzzword] + " Bubble auf Twitter. Mein Gefühl sagt mir, das ist eine Gefahr für " +
      buzzword2[rnd_buzzword2] + ".")
print('Ihre Anna Schneider.')
