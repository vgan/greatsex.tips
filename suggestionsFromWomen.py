from random import choice
from fakeNames import fakeNames

firstname = choice(fakeNames['first']['women'])
lastname = choice(fakeNames['last'])

podcasts =     [
        "\"Dick\'s Nixon\", where I debate his neo-conservative dick on the legacy of Richard Nixon",
        "\"Lady And The Dick\", where his dick and I discuss our favorite Disney films.",
        "about our top 100 MMA fights of all time.",
        "\"Slamilton\", where we rank each song from Hamilton based on how much it distracts us from having sex.",
        "\"The Bone Zone\", where we talk about skeletons we\'d like to fuck.",
        "\"Half in the Vag\", where we describe in loving detail celebrity vaginas.",
        "\"Gotta Go Cum\", where we read our favorite Sonic erotic fan fictions.",
        "\"98.6% Intangible\", where we talk about challenge coins for 8 hours.",
        "\"Savage Love\", where we list things we love about Fred Savage.",
        "\"Welcum to Spermvale\", our serial about an radio announcers sexy adventures in a strange town."
    ]
podcast = choice(podcasts)

dicelist =     [
        "are \"pomegranate\" and \"dick\"",
        "say roll again",
        "are blank",
        "are emoji",
     ]
dice = choice(dicelist)

suggestionsFromWomen = [
   firstname + " " + lastname +  " "
  , 
  [
    "tells us",
    "writes",
    "wrote in to say",
    "confessed to us",
    "let us know"
  ],
  
  " \""
  ,
  [
    "My husband",
    "My hubby",
    "My boyfriend",
    "My man",
    "My bae",
    "My sweetie",
    "My sister\'s husband",
    "This guy I know",
    "Chad",
    "My Tindr hookup"
  ],
  [
    " loves it when " ,
    " really likes it when ",
    " goes wild when ",
    " thinks he\'s died and gone to heaven when ",
    " gets turned on when "
  ],
  [
    "I give him a long, slow blowjob while struggling to read Simone de Beauvoir\'s The Second Sex.",
    "we spend an entire evening avoiding eye contact with each other.",
    "I jerk on his dick to the beat of Kid Rock\'s Early Mornin\' Stoned Pimp.",
    "we compare our credit scores from Experian to the ones from Equifax.",
    "we play \'Sexy Monopoly\', which is like regular Monopoly except it takes longer.",
    "I give him a sexy striptease to the Johnny Cash cover of \"Hurt\".",
    "I put googly eyes on his penis and practice ventriloquy.",
    "I show him all my favorite speedruns of games in the Bubsy series.",
    "I describe and rate every hair on his balls.",
    "we record a new episode of our podcast " + podcast,
    "we watch unboxing videos together.",
    "I strap a large piece of dirty drywall to my face and tell him I\'m his glory hole.",
    "I buff his dick to a mirror shine.",
    "I perform my comedy monologue in a Big Bird costume.",
    "I put the lotion on its skin.",
    "I flap my arms and scream like a pterodactyl.",
    "I donate to The F Plus podcast.",
    "we use those sexy dice but all the sides " + dice,
    "I invest all of our funds in overpriced, over engineered Silicon Valley kitchen appliances.",
    "I use his penis in a tasteful still life.",
    "I jiggle his balls like dice in a cup.",
    "I milk his penis like a cow udder.",
    "I berate him in front of the other girls in the book club.",
    "I let him win a game of Steal the Bacon.",
    "we wrestle in a pool of slimy elbow noodles.",
    "we mosh pit naked in our bedroom.",
    "I go along with his Zeus otherkin story.",
    "I wear old-timey prospector wig and pajamas and open the butt flap.",
    "I edit his articles on Wikipedia.",
    "I do a fan dance with handfuls of live snakes.",
    "we try to orgasm before finishing the elevator game.",
    "we draw penises in our old college textbooks.",
    "I wear him like a glove.",
    "I roast his chestnuts over an open fire.",
    "I hide in a crane game and he has to win me.",
    "I piledrive him into the bed for foreplay.",
    "I mail a pair of my used underwear to his workplace.",
    "I preserve his jizz in the Svalbard Global Seed Vault.",
    "I put my breasts in a paint can shaker.",
    "I bodypaint all his ex-girlfiend\'s names on my ass.",
    "I encase my breasts in tuna aspic for sexy edible foreplay.",
    "I hide the nights I want to have sex in a cryptex.",
    "I bench press him for 100 reps.",
    "I dress in an oppo suit made of swiss cheese.",
    "I unhinge my jaw and devour an entire roast chicken.",
    "I play my melodica during sex."
  ],
  [
    " It certainly makes for an interesting evening!",
    " Waiter? Check Please!",
    " We just make sure the door is locked first!",
    " What a rush!",
    " The police know where we live!",
    " Maximum fun!",
    " A sure-fire turn on!",
    " We couldn\'t keep our hands off each other!",
    " He always asks for more!"
  ],
  
  "\""
]

suggestionfromwomen = suggestionsFromWomen[0] +  choice(suggestionsFromWomen[1]) + suggestionsFromWomen[2] +  choice(suggestionsFromWomen[3]) + choice(suggestionsFromWomen[4]) + choice(suggestionsFromWomen[5]) + choice(suggestionsFromWomen[6]) + suggestionsFromWomen[7]