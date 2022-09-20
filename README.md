# minecraft-one-command-generator
accepts a list of minecraft commands, and returns one command, which will make a series of command block each containing one of your commands, which will excecute in series.

## usage:
input should be list of commands, seperated with " && " (spaces are important), and each command should begin with a 3 character string that defines the type of command block and its settings (normal/repeating/chain, conditional/unconditional, needs redstone/doesn't need redstone)

The first character will be N, R, or C (normal, reapeating, or chain), next is 0 or 1 (true/false) for conditional, and 0 or 1 (true/false) for needs redstone

example:
```
steve@mojang ~$ main.py "N01 give @p diamond && R00 kill herobrine
```
This will return a command that can be run to create a normal command block which will need a redstone signal to execute `give @p diamond`, and a second, repeating command block which does not need redstone containing "kill herobrine".\

If you don't know what to put for this, put "N00", this will simply execute all of your commands once in series


## how does it work?
In minecraft command syntax, theres no way to inlcude more than one command in one line. However, it is possible to say "put a command block here, with X command in it". But that doesnt help us much, because it's still only one command.\
The next step is to summon a falling command block, instead of just putting the block somewhere. The reason for this is because a falling block (such as sand, gravel, or in this case, a command block) is actually an *entity*, not a block (an entity is just anything that has health or moves. Like mobs, boats, dropped items, and even lead rope knots). The benefit to being an entity is that it can have *another* entity riding it. See where this is going? We're almost there, just one more problem: if a falling block is riding another block, it will be partially inside the other one when the first one lands, and drop as an item. To fix this, I have an armor stand with 0 health (so it dies instantly) riding the first block, with a block riding the armor stand. \
So the final command ends being something like "summon a falling command block, with X command, with an armor stand riding it, with another command block riding the armor stand, with Y command, with an armor stand riding that, with..." and so on
