def get_input(word_type: str):
    user_input = input(f"Enter a {word_type}: ")
    return user_input

noun1 = get_input("Noun")
noun2 = get_input("Noun")
noun3 = get_input("Noun")
noun4 = get_input("Noun")
noun5 = get_input("Noun")
noun6 = get_input("Noun")
name1 = get_input("Name")
name2 = get_input("Name")
place_noun1 = get_input("Place")
place_noun2 = get_input("Place")
adjective1 = get_input("Adjective")
adjective2 = get_input("Adjective")
adjective3 = get_input("Adjective")
adjective4 = get_input("Adjective")
adjective5 = get_input("Adjective")
adjective6 = get_input("Adjective")
verb1 = get_input("Verb")
verb2 = get_input("Verb")
verb3 = get_input("Verb")
verb4 = get_input("Verb")
adverb1 = get_input("Adverb")
adverb2 = get_input("Adverb")
plural_noun1 = get_input("Plural Noun")

story = f"""
The Unexpected Meeting

One {adjective1} morning, {name1} and {name2} were walking through a {adjective2} {place_noun1}. Suddenly, they noticed a {noun1} sitting next to a {noun2}.

"That's a very {adjective3} {noun3}," said {name1}.

A stranger appeared and replied, "I know! It can {verb1} better than any other {noun4}."

"Really?" asked {name2}. "Can it also {verb2}?"

"Of course," said the stranger. "Watch this!"

The {noun5} began to {verb3} {adverb1} around the {place_noun2}.

"Wow!" exclaimed {name1}. "That's incredibly {adjective4}!"

The stranger smiled and said, "I've never seen anyone react so {adverb2}."

After talking for a few {plural_noun1}, they decided to {verb4} together and search for a {adjective5} {noun6}.

"Today has been quite {adjective6}," said {name2}.

"I couldn't agree more," replied the stranger.

"""

print(story)