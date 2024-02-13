# # import required module
# from difflib import SequenceMatcher,get_close_matches
#
# # assign parameters
# par1 = "gfg"
# par2 = "GfG"
# # compare
# print(SequenceMatcher(None, par1, par2).ratio())

# # import required module
# import difflib
#
# # assign parameters
# par1 = 'Geeks for geeks!'
# par2 = 'geeks'
#
# # compare
# matches = difflib.SequenceMatcher(
#     None, par1, par2).get_matching_blocks()
#
# for ele in matches:
#     print(par1[ele.a:ele.a + ele.size])


# # import required module
# import difflib
#
# # assign parameters
# string = "Geeks4geeks"
# listOfStrings = ["for", "Gks", "G4g", "geeks"]
#
# # find common strings
# print(difflib.get_close_matches(string, listOfStrings))
