string="0.2 Naseem Shah to Rahul, out Bowled!! Golden duck for Rahul! Maiden T20I wicket for Naseem Shah. He's on a celebratory run. 142kph, a tentative Rahul dangles his bat at this short of length ball outside off. A nothing shot and he deflects it onto the sticks via an inside edge. Perfect start for Pakistan. Rahul b Naseem Shah 0(1)"
# ind=.find(".")
import regex as re
ind=len(string)-string[::-1].find(".")
# print(string[ind:])
pp=re.search(r"\d*(\W*(\d*)\)\W)",string)
print(pp)