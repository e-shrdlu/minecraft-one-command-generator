# minecraft-one-command-generator
accepts a list of minecraft commands, and returns one command which will run all of them

## usage:
input should be list of commands, seperated with " && " (spaces are important), and each command should begin with a 3 character settings-string, such as "R01" (this one means reapeating, unconditional, needs redstone)

first char of settings-string is N, R, or C (normal, reapeating, or chain), next is 0 or 1 for conditional, and 0 or 1 for needs redstone

example:
```steve@mojang: ~/minecraft-one-command-generator$ main.py "N01 give @p diamond && R00 kill herobrine```

## how does it work?
In minecraft command syntax, theres no way to inlcude more than one command in one line. However, it is possible to say "put a command block here, with X command in it". But that doesnt help us much, because it's still only one command.\
The next step is to summon a falling command block, instead of just putting the block somewhere. The reason for this is because a falling block (such as sand, gravel, or in this case, a command block) is actually an *entity*, not a block (an entity is just anything that has health or moves. Like mobs, boats, dropped items, and even lead rope knots). The benefit to being an entity is that it can have *another* entity riding it. See where this is going? We're almost there, just one more problem: if a falling block is riding another block, it will be partially inside the other one when the first one lands, and drop as an item. To fix this, I have an armor stand with 0 health (so it dies instantly) riding the first block, with a block riding the armor stand. \
So the final command ends being something like "summon a falling command block, with X command, with an armor stand riding it, with another command block riding the armor stand, with Y command" and so on
