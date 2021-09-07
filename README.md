# minecraft-one-command-generator
accepts a list of minecraft commands, and returns one command which will run all of them

## usage:
input should be list of commands, seperated with " && " (spaces are important), and each command should begin with a 3 character settings-string, such as "R01" (this one means reapeating, unconditional, needs redstone)

first char of settings-string is N, R, or C (normal, reapeating, or chain), next is 0 or 1 for conditional, and 0 or 1 for needs redstone

example:
```steve@mojang: ~/minecraft-one-command-generator$ main.py "N01 give @p diamond && R00 kill herobrine```
