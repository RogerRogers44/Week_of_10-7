x = "There are %d types of people." % 10  # x is that sentence
binary = "binary"  # binary is binary
doNot = "don't"  # doNot is don't
y = "Those who know %s and those who know %s" % (binary, doNot)  # y is this sentence

print(x)  # says x
print(y)  # says y

print("I said: %r.:" % x)  # says x again
print("I also said: '%s'." % y)  # says y again

hilarious = True  # true
jokeEvaluation = "Isn't that joke so funny?! %r"  # jokeEvaluation is the joke is funny #nofriends

print(jokeEvaluation % hilarious)  # says his joke is funny
w = "This is the left side of..."  # w is the left side of
e = "a string with a right side."  # e is the right side of

print(w+e)  # say both sides

print("Mary had a little lamb.")  # says stuff about Mary
print("Its fleece was white as %s." % 'snow')  # says stuff about her lamb
print("And everywhere that Mary went.")  # rest of song
print("." * 10)  # don't sing the whole song

end1 = "C"  # O
end2 = "h"  # H
end3 = "e"  #
end4 = "e"  # M
end5 = "s"  # Y
end6 = "e"  #
end7 = "B"  # G
end8 = "u"  # O
end9 = "r"  # D
end10 = "g"  # .
end11 = "e"  # .
end12 = "r"  # .

print(end1 + end2 + end3 + end4 + end5 + end6)  # say cheese
print(end7 + end8 + end9 + end10 + end11 + end12)  # say burger

formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))

days = "1, 2, 3, 4, 5..."
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
Withe the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

# r formatter keeps the \n

# escape sequences
tabbyCat = "\tI'm tabbed in"
persianCat = "I'm split\non a line"
backslashCat = "I'm \\ a \\ cat"
topCat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t*Grass
"""
print(tabbyCat)
print(persianCat)
print(backslashCat)
print(topCat)
