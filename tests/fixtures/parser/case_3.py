from textwrap import dedent

INPUT = dedent("""
The history of visual novels dates back to The Portopia Serial Murder Case (1983). It featured non-linear elements, which include traveling between different areas in a generally open world, a branching dialogue conversation system where the story develops through entering commands and receiving responses from other characters, and making choices that determine the dialogues and order of events as well as alternate outcomes, though there is only one true culprit while the others are red herrings. It also features a phone that could be used to dial any number to contact several non-player characters.[17] The game was well received in Japan for its well-told storyline and surprising twist ending, and for allowing multiple ways to achieve objectives.[16] Shortly after, in 1988, Snatcher appeared, developed by Hideo Kojima and released for the PC-8801 and MSX2 in 1988, in which a cyberpunk detective hunts down a serial killer.[18] Another more non-linear early example was Mirrors, released by Soft Studio Wing for the PC-8801 and FM Towns computers in 1990; it featured a branching narrative, multiple endings, and audio CD music.[19]

A common feature used in visual novels is having multiple protagonists giving different perspectives on the story. EVE Burst Error (1995), developed by Hiroyuki Kanno and C's Ware, introduced a unique twist to the system by allowing the player to switch between both protagonists at any time during the game, instead of finishing one protagonist's scenario before playing the other. EVE Burst Error often requires the player to have both protagonists co-operate with each other at various points during the game, with choices in one scenario affecting the other.[20]

An important milestone in the history of visual novels was YU-NO: A girl who chants love at the bound of this world (1996), which was developed by Hiroyuki Kanno and is ELF's most famous visual novel.[21] It featured non-linear storytelling, with a science fiction plot revolving around time travel and parallel universes. The player travels between parallel worlds using a Reflector device, which employs a limited number of stones to mark a certain position as a returning location, so that if the player decides to retrace their steps, they can go to an alternate universe to the time they have used a Reflector stone. The game also implemented an original system called Automatic Diverge Mapping System (ADMS), which displays a screen that the player can check at any time to see the direction in which they are heading along the branching plot lines.[22]

YU-NO revolutionized the visual novel industry, particularly with its ADMS system.[21] Audiences soon began demanding large-scope plotlines and musical scores of similar quality and ambition to that of YU-NO, and that responded by hiring talent. According to Gamasutra: "The genre became an all-new arena for young artists and musicians once again, with companies willing to take chances on fresh blood; the market thrived with the excitement and the risks that were being taken, and became a hotbed of creativity".[23] The branching timeline system was influential, opening "the door for visual novels to become more elaborate and have a greater range of narrative arcs, without requiring the player to replay the game over and over again".[24] According to Nintendo Life, "the modern visual novel genre would simply not exist without" YU-NO.[25] Branching timeline systems similar to YU-NO also later appeared in role-playing video games such as Radiant Historia (2010)[26][27] and the PSP version of Tactics Ogre (2010).[28]

Chunsoft sound novels such as Machi (1998) and 428: Shibuya Scramble (2008) developed the multiple-perspective concept further. They allow the player to alternate between the perspectives of several or more different characters, making choices with one character that have consequences for other characters.[12][29] 428 in particular features up to 85 different possible endings.[29] Another popular visual novel featuring multiple perspectives is Fate/stay night (2004).[6]
""")

EXPECTED = [
    [
        'The history of visual novels dates back to The Portopia Serial Murder Case (1983).', 'It featured non-linear elements, which include traveling between different areas in a generally open world, a branching dialogue conversation system where the story develops through entering commands and receiving responses from other characters, and making choices that determine the dialogues and order of events as well as alternate outcomes, though there is only one true culprit while the others are red herrings.', 
        'It also features a phone that could be used to dial any number to contact several non-player characters.[17]', 
        'The game was well received in Japan for its well-told storyline and surprising twist ending, and for allowing multiple ways to achieve objectives.[16]', 
        'Shortly after, in 1988, Snatcher appeared, developed by Hideo Kojima and released for the PC-8801 and MSX2 in 1988, in which a cyberpunk detective hunts down a serial killer.[18]', 
        'Another more non-linear early example was Mirrors, released by Soft Studio Wing for the PC-8801 and FM Towns computers in 1990; it featured a branching narrative, multiple endings, and audio CD music.[19]'
    ], 
    [
        'A common feature used in visual novels is having multiple protagonists giving different perspectives on the story.', 
        "EVE Burst Error (1995), developed by Hiroyuki Kanno and C's Ware, introduced a unique twist to the system by allowing the player to switch between both protagonists at any time during the game, instead of finishing one protagonist's scenario before playing the other.", 
        'EVE Burst Error often requires the player to have both protagonists co-operate with each other at various points during the game, with choices in one scenario affecting the other.[20]'
    ], 
    [
        "An important milestone in the history of visual novels was YU-NO: A girl who chants love at the bound of this world (1996), which was developed by Hiroyuki Kanno and is ELF's most famous visual novel.[21]", 
        'It featured non-linear storytelling, with a science fiction plot revolving around time travel and parallel universes.', 
        'The player travels between parallel worlds using a Reflector device, which employs a limited number of stones to mark a certain position as a returning location, so that if the player decides to retrace their steps, they can go to an alternate universe to the time they have used a Reflector stone.', 
        'The game also implemented an original system called Automatic Diverge Mapping System (ADMS), which displays a screen that the player can check at any time to see the direction in which they are heading along the branching plot lines.[22]'
    ], 
    [
        'YU-NO revolutionized the visual novel industry, particularly with its ADMS system.[21]', 
        'Audiences soon began demanding large-scope plotlines and musical scores of similar quality and ambition to that of YU-NO, and that responded by hiring talent.', 
        'According to Gamasutra: "The genre became an all-new arena for young artists and musicians once again, with companies willing to take chances on fresh blood; the market thrived with the excitement and the risks that were being taken, and became a hotbed of creativity".[23]', 
        'The branching timeline system was influential, opening "the door for visual novels to become more elaborate and have a greater range of narrative arcs, without requiring the player to replay the game over and over again".[24]', 
        'According to Nintendo Life, "the modern visual novel genre would simply not exist without" YU-NO.[25]', 
        'Branching timeline systems similar to YU-NO also later appeared in role-playing video games such as Radiant Historia (2010)[26][27] and the PSP version of Tactics Ogre (2010).[28]'
    ], 
    [
        'Chunsoft sound novels such as Machi (1998) and 428: Shibuya Scramble (2008) developed the multiple-perspective concept further.', 
        'They allow the player to alternate between the perspectives of several or more different characters, making choices with one character that have consequences for other characters.[12][29]', 
        '428 in particular features up to 85 different possible endings.[29]', 
        'Another popular visual novel featuring multiple perspectives is Fate/stay night (2004).[6]'
    ]
] 