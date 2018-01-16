# -*- coding: utf-8 -*-
import tweepy
from subprocess import Popen,PIPE,STDOUT
import time
import os
import re
import random
from random import randint
from time import sleep
import textwrap
import pytumblr
from keys import *
import mmap
from name_gen import generateName
from animals import animal
import inflect
from mastodon import Mastodon


auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_token_key, twitter_token_secret)
api = tweepy.API(auth)
client = pytumblr.TumblrRestClient(tumblr_consumer_key, tumblr_consumer_secret, tumblr_token_key, tumblr_token_secret)

basedir = "/home/vgan/rodserlingzone/"
rando = (randint(1,10))
blank = basedir + "blank/" + "serling" + str(rando) + ".jpg"
image = basedir + "rodserlingzone.jpg"
intros = basedir + "intros.txt"
font="/usr/share/fonts/alte_haas_grotesk/AlteHaasGroteskBold.ttf"
points="28"
colors = ["yellow","white"]
font_color = random.choice(colors)

p = inflect.engine()

mastodon = Mastodon(
        api_base_url='https://botsin.space',
        client_id = basedir + 'mastodon_clientcred.txt',
        access_token = basedir + 'mastodon_usercred.txt'
)

def sendToInterwebs(image,imageObj,text):
	try:
                tweet_text = text
      		s = api.update_with_media(image,status=" "+ tweet_text , file=imageObj)
	except:
        	print "tweeting failed :("
	try:
		client.create_photo('twilightzoneintros', state="published", tags=[ "Twilight Zone" ], data=str(image))
	except:
		print "tumbling failed"
        try:
                toot_text = text
                media_dict = mastodon.media_post(image)
                mastodon.status_post(toot_text, media_ids=[media_dict,], sensitive=False)
        except:
                print "tooting failed :|"

pronouns = [["male","female",None],[ "himself", "herself", "themselves" ],[ "he", "she", "they" ],["him","her","they"],["his","her","their"],["Mr.","Ms."]]
genders = [ 0,1 ]
gender = random.choice(genders)
gender_label = pronouns[0][gender]
himself = pronouns[1][gender]
he = pronouns[2][gender]
him = pronouns[3][gender]
his = pronouns[4][gender]
mr = pronouns[5][gender]

nameArray = generateName(gender_label)
name = nameArray[0]
gender_label = nameArray[1]

animals = p.plural(animal)
ananimal = p.an(animal)

people_list = [ "cowboy","computer operator","opera singer","exotic dancer","prison guard","baseball player","circus clown","janitor","fighter pilot","badger","secretary","soda jerk","cab driver","pianist","saxophonist","coyote","stork","astronaut","stagecoach driver","farmer","Martian","space man","office clerk","school teacher","monk","podiatrist","beatnik","aardvark","capybara","crossing guard","shopkeeper","ferret","cattle rancher","hamster","hedgehog","janitor","librarian","scientist","switch board operator","mermaid","middle manager","monkey","mouse","orangutan","parakeet","park ranger","pig","raccoon","reindeer","short order cook","bus boy","ham radio operator","scout leader","game show host","walrus","sheriff","barber","sheriff","carpenter","waitress","bellhop","bus driver","archaeologist","historian","astronomer","psychiatrist","grave digger","mortician","butcher","quarterback","iguana","sailor","pirate","sea captain","cheerleader", "soldier","bartender" ]

person = random.choice(people_list)
people = p.plural(person)
aperson = p.a(person)

longlostthing_list = [ "lava lamp","bale of hay","pitchfork","can of sardines","apple crate","yardstick","compass","doorknob","padlock","chest of drawers","pair of trousers","pair of shoes","pair of scissors","fountain pen","camera","slot machine","diaper","satchel of garlic","brisket","colony of sea monkeys","slide rule","transistor radio","boomerang","letterman jacket","frisbee","hula hoop","ant farm","pocketbook","penguin","bag of rocks","thermos","canteen","beret","baseball","rubber band ball","hair net","broom","handkerchief","overcoat","slipper","neck tie","satchel","candy bar","knapsack","picnic basket","purse","hair brush","waste basket","smoking jacket","thermometer","teapot","fedora","top hat","pocket comb","switchblade", "pocket watch","shoe-horn","sack of potatoes", "fruit basket","ironing board","revolver","football","tin can","apple crate","phonograph","pair of dice", "deck of cards","mirror","undershirt","baby","pocket knife","fishing rod","sailor\'s cap","bag of marbles","bow tie","tinker toy","hamper","monocle","ship in a bottle","blender","bowling ball","plunger","turkey baster","meat thermometer","puppet","wristwatch","short wave radio","pogo stick","hula hoop","can of baked beans","velvet clown painting" ]
longlostthing = random.choice(longlostthing_list)
alonglostthing = p.a(longlostthing)
longlostthings = p.plural(longlostthing)

messages1 = [ "Kill","Love","Don\'t trust","Don\'t rely on","The answer was always","Eat","Listen to" ]
messages2 = [ name, name, name, name, "the pirates","your breakfast","the dirt","tobacco","bricks","your mother","your mommy","your daddy","butter","coffee","Love","the potato","science","rhubarb","Satan","math","bread","Ovaltine","flannel","Anarchy","polyester","barbecue","the dinosaurs","the spatula","pencils","earthworms","plaster","fake eyelashes","the wigs","the prosthetic arm","the glass eye","the bear costume" ] 
message = random.choice(messages1) + " " + random.choice(messages2)

experiences = [ "friendship","loneliness","terror","tolerance","love","barbarism","humility","joy","fear","tenderness","humbleness","faithfulness","fun","the limbo","life","boredom","freedom","independence","perseverance" ]
experience = random.choice(experiences)

lessons = [ "tolerance","love","humility","faithfulness","survival","self-respect","independence","perseverance" ]
lesson = random.choice(lessons)

museums = [ "turkey baster","balloon animal","fishing lure","ham radio","cold cut","grapefruit","empanada","parakeet","cabbage","pepperoni","clown","bongo","marital aid","dirt","mold","fungus","plastic","potato","hot sauce","cockroach","mushroom","ice cream","lawn mower","clam chowder","sewer rat","poker","asphalt","banana","sewage","tobacco","salt","gravy","fornication","bowling ball","brick","pancake","golden retriever","olive oil","fruit cake","shoe-horn","chalk","banjo","tractor","ping pong","robot","glass","doll house","saxophone","taco","dental","shotgun","stove","typewriter","dolphin","tarantula","corn","hammer", "tapeworm", "puppetry","vampire","miniature " + longlostthing,"werewolf","plunger","toilet","tortoise","piglet","hobo","gumbo" ]
museum = random.choice(museums) 
museumtypes = [ "museum","theme park","variety show","speakeasy","colony","emporium", "mall" ]
museumtype = random.choice(museumtypes)
becomes = [ "a ghost","a marionette","an exotic dancer","a burlesque dancer","a ventriloquist dummy","an alien","the president","head chef","a mummy","a werewolf","a vampire","a murderer","a character in a TV show","a child\'s toy" ]
become = random.choice(becomes)

openings = [ "because","for","as","and","since" ]
opening = random.choice(openings)

openings2 = [ "simple","ordinary","average","typical","unexceptional","unremarkable","run of the mill","unassuming", "mere", "non-descript"  ]
opening2 = random.choice(openings2)

weirdshits = [ "baby mice","tentacles","brisket","lead","barbed wire","aluminum foil","cellophane","sea monkeys","Tang","ball bearings","bread crumbs","French bread","bread sticks","molasses","cigar ashes","almonds","avocados","sliced bananas","BBQ sauce","bee pollen","corned beef","bitters","blueberries","broccoli florets","bug spray","buttermilk","chamomile tea","channa masala","springs","Vics VapoRub","chocolate pudding","beef stew","coffee","sand","beef stroganoff","melted butter","eggplant","soft boiled eggs","egg yolk","espresso","malted milk","flan","sawdust","flour","French dressing","artichoke hearts","frosting","garlic","ghost peppers","granola","grapes","grape jelly","gravy","Greek yogurt","green tea","grits","earthworms","ham","habanero peppers","haggis","honey","horse radish","pizza","hot sauce","ice cream","ketchup","Kool-Aid","lettuce","Listerine","lunch meat","mango chutney","maple syrup","marmalade","Marmite","mayonnaise","nutmeg","olive oil","onions","oregano","Oreos","Ovaltine","pastrami","peanuts","peanut butter","pepper","pepperoni","peppermint","stuffed animals","pork chops","pretzels","pickle juice","pinto beans","potatoes","powdered sugar","radish","ranch dressing","red pepper flakes","red velvet cake","roast beef","salt water taffy","sardines","seaweed","sour milk","soft serve","soy sauce","sauerkraut","pudding","tater tots","tomatoes","Tootsie Rolls","walnuts","wasabi","ovaltine","aftershave","ants","asbestos","banana peels","battery acid","bees","beetle wings","bleach","Borax","broken glass","cardboard","cat hair","catnip","chlorine","beer","conditioner","confetti","coolant","DDT","detergent","Drano","Elmer\'s glue","embalming fluid","fabric softener","fake eyelashes","fertilizer","glitter","hair dye","hair spray","kitty litter","hand lotion","imodium ad","mercury","butter","motor oil","nail polish remover","paint thinner","pomade","gravel","rat poison","rubbing alcohol","rubber cement","super glue","hand soap","shampoo","shaving cream","soil","spider legs","termites","talcum powder","chewing tobacco","bacon grease","transmission fluid","tuna","prune juice","Vaseline","Windex" ]
weirdshit = random.choice(weirdshits)

disgustings = [ "a debilitating","a disgusting","a filthy","an obscene","an abhorrent","an abominable","a repugnant","a heinous", "a reprehensible","a repulsive" ] 
disgusting = random.choice(disgustings)

remarkables = [ "a peculiar","an enchanted","a remarkable","a miraculous","an astonishing","an astounding","an extraordinary","an incredible","an inexplicable","a very special","a marvelous","a monstrous","a phenomenal","a spectacular","a strange","a supernatural","an unbelievable","a wondrous" ]
remarkable = random.choice(remarkables)

recentlyacquireds = [ "recently acquired", "is about to develop", "just developed", "recently developed" ]
recentlyacquired = random.choice(recentlyacquireds)

meets = [ "Consider", "Meet","This is","Introducing","Allow me to introduce","Here we have" ]
meet = random.choice(meets)

smells = [ "moth balls","dog food","cat food","liver wurst","poutine","wet dog","gasoline","Limburger cheese","Parmesan cheese","cigar smoke","bananas","BBQ sauce","blue cheese","bug spray","sour milk","curry","Vics VapoRub","onions","menthol","eucalyptus","pine sol","rotton eggs","garlic","rotting meat","gravy","ham","horse radish","pizza","Listerine","mango chutney","oregano","pastrami","pepperoni","burnt toast","burning hair","sardines","sour milk","cologne","aftershave","bleach","chlorine","garbage","embalming fluid","fertilizer","hair spray","nail polish remover","paint thinner","rubbing alcohol","talcum powder","tuna","sulfur", "a men's locker room" ]
smell = random.choice(smells)

stuffstoworship = [ animal, animal, animal, animal, "diaper","basket","brick","thermos","mime""wooden pony", "toy soldier", "gravy", "mustache", "body hair", "hairball", "peanut", "fruitcake", "hand-puppet", "marionette","sea monkey","tentacle","beef stew", "coffee", "lard", "burrito", "rock and roll music", "plastic" ]
stufftoworship = random.choice(stuffstoworship)  

cults = [ stufftoworship + " worshipping", animal + " worshipping"]
cult = random.choice(cults)

while weirdshit == smell:
                weirdshit = random.choice(weirdshits)
                smell = random.choice(smells)

places = [ "at the local library","in the heart of the jungle","at a pharmacy","in the galley of a ship","at a diner","in a fallout shelter","in a tree house","in a railroad freight car","in the middle of the desert","in the back of a horse drawn carriage"]
place = random.choice(places)

quantities = [ "a plethora of","a couple of","a few","some","a hoard of","multitudes of","several","hundreds of","thousands of","millions of","billions of" ]
quantity = random.choice(quantities)

opinions = [ "cursed","disgusting","absurd","abhorrent","abominable","repugnant","heinous","reprehensible","repulsive","wonderful","majestic","decrepit","benevolent", "altruistic","twisted","cantankerous","delusional","humble","rambunctious","arrogant","misguided","shifty","level-headed","pathetic","self-centered","disoriented","curious","revered","noble","infallible","meticulous","simple","forgetful","oblivious","garish","unusual","angelic","respectable" ]
opinion = random.choice(opinions)

sizes = [ "absurdly small","miniature","dense","slim","chubby","obese","tiny","pygmy","small","very small","short","itty bitty","very big","massive","huge","gargantuan","colossal","enormous","gigantic","humongous","absurdly large" ]
size = random.choice(sizes)

agenum = str(randint(2,120))
ages = [ agenum + "-year-old", agenum + "-year-old","baby","infant","adult","geriatric","ancient","pre-historic","teen aged","pre-teen","adolescent" ]
age = random.choice(ages)

shapes = [ "round","square","triangular","hexagonal","spherical","rectangular","octagonal" ]
shape = random.choice(shapes)

colors = [ "aqua","burgundy","beige", "black","blue", "brown","cyan","green","hot pink","magenta","maroon","off-white","orange","peach","pink","plaid","powder blue", "purple","rainbow", "turquoise","violet","yellow"]
color = random.choice(colors)

origins = [ "Russian","Siberian","Yemeni","Martian","Uruguayan","Native American","Argentinian","Chilean","Congolese","Chinese","Ecuadorian","Japanese","Jamaican","Guatemalan","Viennese","Finnish","Lithuanian","Estonian","Tibetan","Himalayan","Bavarian","Tahitian","Cuban","Lebanese","Victorian","Vietnamese" ]
origin = random.choice(origins)

adjective_list = [ "comical", "forlorn","decrepit","muscular","barbaric","delicate","introverted","diabetic","sentimental","benevolent", "altruistic","twisted","delusional","humble", "repressed", "bashful", "depressed","geriatric","diabolical","rambunctious","arrogant","misguided","barbaric","ferocious","tiny","alien","frail","cybernetic","animatronic","mechanical","robotic","eccentric","self-centered","disoriented","snide","curious" ]
adjective = random.choice(adjective_list)
anadjective = p.an(adjective)

material_list = [ "aluminum","inflatable","polyester","cellophane","glass","plaster","plastic","rubber","leather","wooden","robotic","mechanical","wind-up","porcelain","ceramic","wooden","patchwork","needlepoint","origami","soap stone","marble","crystal","steel","metallic","chrome" ]
material = random.choice(material_list)
materials = p.plural(material)

purpose_list = [ "work","reference","fishing","sports","sleeping" ]
purpose = random.choice(purpose_list)

amputated_list = ["amputated","dead"]
amputated = random.choice(amputated_list)
bodypart_list = [ "finger","horn","tusk","eyeball","tongue","ear","pinkie","toe","foot","hand","nose","leg","arm" ] 
bodypart = random.choice(bodypart_list)
bodyparts = p.plural(bodypart)

carcass = ["The carcass of " + ananimal, "A deceased " + animal,"A flayed " + animal ]
darkshit1 = random.choice(carcass)
darkshit2 = p.an(amputated + " " + bodypart)   

entrance_list = [ "suddenly materialized... in ","abruptly fallen from the sky... to ","suddenly appeared... in ","just crept into... ","abruptly invaded...","just assumed control of... " ]
justentered= random.choice(entrance_list) 

innocents = [ "an innocent","a naive","a young","an uncorrupted","an honest","a humble" ]
innocent = random.choice(innocents)

displays = [ "just noticed an unplugged television set displaying the phrase","just gazed up into the marquee of a long abandoned theater which reads", "just looked down to see a trail of ants winding themselves into the words", "just opened a dusty library book and the first page reads","just picked up todays news paper and the headline reads" ]
display = random.choice(displays)

guacs = [ "guacamole", "an extra scoop of ice cream","a large malted milk","the double cheeseburger","extra gravy","sardines" ]
guac = random.choice(guacs)

remarkable_actions1 = [ "creates","controls","turns " + weirdshit + " into" ]
remarkable_action1 = random.choice(remarkable_actions1)

remarkable_actions2 = [ "wind","earthquakes","money","wishes","oceans","robotic " + animals,"martians" ]
remarkable_action2 = random.choice(remarkable_actions2)

remarkable_action = remarkable_action1 + " " + remarkable_action2

condiments = [ "pureed spam","toothpaste","nutella","pure lard","pixie sticks","candy corn","peanut butter","gummy bears","crushed oreos","maple syrup","chocolate syrup","mashed bananas","ice cream","vicks vapo rub","pomade","cottage cheese","candy corn","jello","pudding" ]
condiment = random.choice(condiments)

hotdogs = [ "popcorn","french fries","hotdog","pastrami sandwich","ham sandwich","grilled cheese sandwich","chicken fried steak","hamburger","steak","filet mignon","fried chicken","pork chops","meatloaf" ]
hotdog = random.choice(hotdogs)

actions = [ "fighting over","dismantling","attempting to eat","staring at","caressing","dancing with","sniffing","admiring","destroying", "serenading" ]
action = random.choice(actions)

witnesses = [ "witness an act which will forever change " + him, "learn the true potential of human perversion", "understand what is the true potential of human depravity" ]
witness = random.choice(witnesses)

def makeImage(blank,text):
	wrapped_text='\n'.join(textwrap.wrap( text, 55))
	rodserlingcmd = [ "/usr/bin/convert", blank,"-pointsize", points,"-font",font,"-fill",font_color,"-undercolor","#0008","-gravity","SouthWest","-annotate","+80+50",wrapped_text,image ]
        p = Popen(rodserlingcmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        output = p.stdout.read()
        print output

def generateText(template_id):
	templates = [
                meet + " " +  name + ", " + he + " is about to " + witness + " as " + his + " neighbor calmly applies " + condiment + " to " + his + " " + hotdog + "... in The Twilight Zone.",
                "for " + anadjective + " " + person + " who finds " + himself + " the owner of " + remarkable + " " + origin + " " + longlostthing + "... in The Twilight Zone.",
                opening + " " + he + " discovers a " + museum + " " + museumtype + " is about to open... in The Twilight Zone.",
                "and even " + p.an(opening2) + ", " + adjective + " " + person + " might learn a lesson in " + lesson + "... in the Twilight Zone.",
                "has left " + him + " covered in " + weirdshit + " and reeking of " + smell + "... in the Twilight Zone.",
                opening + " " + p.an(adjective) + " " + person + " will soon be re-united with " + remarkable + " "  + longlostthing + "... in the Twilight Zone.",
                opening + " " + p.an(opening2) + ", " + adjective + " " + person + " is about to join " + p.an(cult) + " cult... in the Twilight Zone.",
                opening + " " + p.an(opening2) + ", " + adjective + " " + person + " " + display + " \"" + message + "\"... in the Twilight Zone.",
                "yet " + p.an(opening2) + ", " + adjective + " " + person + " is about to discover the true meaning of " + experience + "... in the Twilight Zone.", 
		meet + " " +  name + ", " + anadjective + " " + person + " who has recently acquired " + remarkable + " " + longlostthing + "... in the Twilight Zone.",
		meet + " " + name + ", "  + anadjective + " " + person + ". " + he.title() + " is about to wake up all alone " +  place + " covered in " + p.an(disgusting) + " quantity of " + weirdshit +  "... in the Twilight Zone.",
		darkshit1 + ", " + darkshit2 + ", some " + weirdshit + "... and " + mr + " " + name + ". Preparing to take the longest walk of " + his + " life, to the center of the Twilight Zone.",
		#he + " will understand what are the properties of " + experience + ". " + anadjective.capitalize() + " " + thing +  " will lead " + him + " by the hand and walk with " + him + " into a nightmare... down to the center of the Twilight Zone.",
		opening + " " + p.an(opening2) + ", " + adjective + " " + person + " is about to discover that " + he + " is in fact " + become + "... in the Twilight Zone.",
		opening + " " + p.an(opening2) + ", " + adjective + " " + person + " has just developed " + disgusting + " addiction to " + weirdshit  + "... in the Twilight Zone.",
		opening + " two " + adjective + " " + people + " " + action + " "  + p.an(longlostthing) + " are about to discover the true meaning of " + lesson + "... in the Twilight Zone.",
		#opening + " " + p.an(opening2) + ", " + adjective + " " + thing + " has made it just in the nick of time for the early bird special... in the Twilight Zone.",
		#opening + " " + p.an(opening2) + ", " + adjective + " " + thing + " has just discovered that " + guac + " only costs a nickel... in the Twilight Zone.",
		#opening + " " + p.an(opening2) + ", " + adjective + " " + thing + " has just learned where babies come from... in the Twilight Zone.",
		#opening + " " + p.an(opening2) + ", " + adjective + " " + thing + " has just filed " + his + " taxes before they were due... in the Twilight Zone.",
		#opening + " " + p.an(opening2) + ", " + adjective + " " + thing + " has just discovered that the large beer glass actually contains the same volume as the small one... in the Twilight Zone.",
		#quantity.capitalize() + " " + things + "   "... in the Twilight Zone."
		]
	templates_total = (len(templates) - 1)
	if template_id == "random":
        	template_id = randint(0,templates_total)
	text = templates[template_id]
        return (text)

def isItNew(intro,intros):
        if os.path.isfile(intros):
                introsObj = open(intros,"a+")
                introsmm = mmap.mmap(introsObj .fileno(), 0, access=mmap.ACCESS_READ)
                if introsmm.find(intro) == -1: # intro not found, string is new!
                        introsObj.write(intro + "\n") # store text to check for uniqueness
                        intro = "True"
                        return intro
                else:
                        intro = "False"
                        return intro
                introsObj.close()
        else:
                print intros + " does not exist..."

def testTheDamnThing(template_id):
        text = generateText(template_id)
        print text

def doTheDamnThing(template_id):
	text = generateText(template_id)
	new = isItNew(text,intros)
        while new == "False":
                print text + " is not new intro, making a new one..."
		text = generateText()
	makeImage(blank,text)
	if (os.path.isfile(image) and os.path.isfile(image)):
        	imageObj = open(image)
             	sendToInterwebs(image,imageObj,text)
                os.remove(image)
	else:
        	print "no image :("

testTheDamnThing("random") # pass in the number if you want to test a certain template
#doTheDamnThing("random")
