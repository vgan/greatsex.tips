from random import choice
from bodyParts import bodyParts
from fakeNames import fakeNames

firstname = choice(fakeNames['first']['men'])
lastname = choice(fakeNames['last'])

nonPenisActionsFromMen = [
  firstname + " " + lastname + " ",
  [
    "says",
    "tells us",
    "confesses",
    "writes"
  ],
  " \"",
  [
    "I love it when",
    "It turns me on when",
    "It drives me wild when",
    "I feel like I've died and gone to heaven when",
	"My heart skips a beat when"
  ],
  " ",
  [
    "a chick",
    "a woman",
    "a babe",
    "a lady",
    "a girl",
    "my waifu",
    "my bae"
  ],
  " ",
  [
    "tugs on",
    "slaps",
    "twists",
    "flicks",
    "spits on",
    "lightly touches",
    "silently judges",
    "nibbles on",
    "stares intently at",
    "screams at",
    "cries on",
    "makes a big fucking deal of",
    "alternates an ice pack and hot water bottle on",
    "burns",
    "dribbles chocolate sauce on",
    "films",
    "liveblogs",
    "folds",
    "sculpts",
    "massages",
    "pokes",
    "judges",
    "annoys",
    "volleys",
    "grinds to dust",
	"drools on",
	"instagrams",
	"snapchats",
	"sends all my facebook friends photos of"
  ],
  " my " + choice(bodyParts) + ". It ",
  [
    "drives me crazy every time",
    "absolutely destroys me each time",
    "makes me want to propose marriage",
    "makes me want to do the same thing back to her",
    "makes me rethink all my life choices up til that point",
    "really is something we men sure do like a lot",
    "makes me want to flee the country",
    "makes for a great Reddit post",
    "helps me finish my screenplay",
    "is an amazing revalation",
    "sustains me emotionally",
    "scratches that itch",
    "is really quite inopportune",
    "is a war crime",
    "threatens me emotionally",
    "makes me consider real estate on the moon",
    "fixes my credit score",
    "sends me to Hogwarts",
    "sorts my biscuits",
    "really gives me something to discuss with my therapist this week",
    "is great I guess",
    "makes me reconsider the capitalist system",
    "makes me take up competitive curling",
    "jazzes my jizz",
    "flips my flaps at the good ol' sock hop",
    "causes my penis to spin around in a comical manner",
    "makes me consider orgasms",
    "seems legit",
    "causes my hair to turn white and rocket from my body",
    "makes me buy six different burritos and preserve them in resin",
    "makes me remove my disguise and run off with the Queen's jewels",
	"reminds me of my life before the Witness Relocation Program",
	"gives me goosebumps just thinking about it",
	"made sense at the time. I guess you had to be there",
	"is why my neighbors all installed sound proofing",
	"helps me feel again",
	"levels up my sex skill",
	"is all very predictable",
	"puts a fine shine on my coat",
	"feels mighty fine by golly",
	"really puts this thing we call life into perspective",
	"fixes all of the tax problems I've had with the IRS",
	"reminds me how insignificant this all is in the grand scheme of things"
  ],
  [
    "!", "!", "!!!", "."
  ],
  "\""
]

nonpenisaction = nonPenisActionsFromMen[0] + choice(nonPenisActionsFromMen[1]) + nonPenisActionsFromMen[2] +  choice(nonPenisActionsFromMen[3]) + nonPenisActionsFromMen[4] + choice(nonPenisActionsFromMen[5]) + nonPenisActionsFromMen[6] + choice(nonPenisActionsFromMen[7]) + nonPenisActionsFromMen[8] + choice(nonPenisActionsFromMen[9]) + choice(nonPenisActionsFromMen[10]) + nonPenisActionsFromMen[11]