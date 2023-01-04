import random

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

noun1, noun2, noun3 = random.choice(nouns), random.choice(nouns), random.choice(nouns)
verb1, verb2, verb3 = random.choice(verbs), random.choice(verbs), random.choice(verbs)
adj1, adj2, adj3 = random.choice(adjectives), random.choice(adjectives), random.choice(adjectives)
prep1, prep2 = random.choice(prepositions), random.choice(prepositions)
adverb1 = random.choice(adverbs)

vowels = ("a", "e", "i", "o", "u")
if adj1.startswith(vowels):
    a_an = "An"
else:
    a_an = "A"

print(f"""
{a_an} {adj1} {noun1}\n
{a_an} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
{adverb1}, the {noun1} {verb2}
the {noun2} {verb3} {prep2} a {adj3} {noun3}
""")