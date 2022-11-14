import random
promi = ('Dieter Nuhr', 'Ulf Poschardt', 'Friedrich Merz', 'Wolfgang Kubicki', 'Anna Schneider',)
buzzword = ('woke', 'linke', 'gendernde', 'grüne', 'autohassende',)
buzzword2 = ('die Demokratie', 'unsere Gesellschaft', 'Deutschland', 'alle Liberale', 'die Meinungsfreiheit',)

for x in range(10):
    rnd_promi = random.randint(0, len(promi) - 1)
    rnd_buzzword = random.randint(0, len(buzzword) - 1)
    rnd_buzzword2 = random.randint(0, len(buzzword2) - 1)
    print(promi[rnd_promi] + " ist also ein Nazi. Das behauptet zumindest die " +
          buzzword[rnd_buzzword] + " Bubble auf Twitter. Mein Gefühl sagt mir, das ist eine Gefahr für " +
          buzzword2[rnd_buzzword2] + ".")
