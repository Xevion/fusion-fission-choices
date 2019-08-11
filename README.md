# fusion-fission-choices

## What is this repository?

`fusion-fission-choices` is a simple utility written in Python for identifying preferable elements to use for fusion with the Alchemistry Minecraft Mod.

I apologize if stuff is unclear or is just plain strange, I am not used to producing configuration or documentation, but I strive for the best, so please open an issue or send a pull request in if you find something to be out of order.

## Where is the Fission part?

As of now, I have only implemented the fusion part, since it's drastically easier. The fission module for this will come later, if I decide I need it, but since the fission recipes come in JEI automatically... I'll be okay.

## To-do

* Implement Fission

* Better configuration options

* Automatic scoring system

## Configuration Options

The `elements` portion refers to the scores of each element, each being the atomic number of the element.

---

`minimumScore` refers to the mimimum score all elements must reach to be printed out. Settings this to -1 will make all elements be printed out.

---

`reverseIndividualOrder` refers to whether or not the program should reverse the output of the lists so that individual list printouts should have elements with higher scores.

---

`reverseOrder` refers to the order in which the list of lists is sorted, `False` being longer lists at the top and `True` being shorter lists at the top, and vice-verse for the bottom.

---


`noNegatives` refers to whether it should filter out elements that have a negative score (ie. while using default configs, filter out elements without a score set).

A set of elements with the score (-1, 5) would get filtered out, while a set with the scores (78, 12) would not.

---

`fullPrint` refers to whether it should print out the Symbol or the Name of the Element.

---

`eliminateEmpty` refers to whether the program should remove specified elements if they contained no matching tuples.

---

`showScore` refers to whether or not the program shows the score calculated alongside each element.

`showScoreZFill` refers to whether or not to apply applicable ZFill arguments to the score display.