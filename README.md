# fusion-fission-choices

## What is this repository?

`fusion-fission-choices` is a simple utility written in Python for identifying preferable elements to use for fusion with the Alchemistry Minecraft Mod.

## Where is the Fission part?

As of now, I have only implemented the fusion part, since it's drastically easier. The fission module for this will come later, if I decide I need it, but since the fission recipes come in JEI automatically... I'll be okay.

## Configuration Options

The `elements` portion refers to the scores of each element, each being the atomic number of the element.

---

`minimumScore` refers to the mimimum score all elements must reach to be printed out. Settings this to -1 will make all elements be printed out.

---

`noNegatives` refers to whether it should filter out elements that have a negative score (ie. while using default configs, filter out elements without a score set)

A set of elements with the score (-1, 5) would get filtered out, while a set with the scores (78, 12) would not.

---

`fullPrint` refers to whether it should print out the Symbol or the Name of the Element