import sys

commandList = []

class commandblockcommand:
    def __init__(self, command, blockType, conditional, needsRedstone):
        self.command = command # str, command to execute
        self.blockType = blockType # str, "command_block", "repeating_command_block", or "chain_command_block". defines type of command block to be spawned
        self.needsRedstone = needsRedstone # bool. determines if command block needs redstone to run
        self.conditional = conditional # str, "true" or "false". determines if chain command block needs previous command block to be succesful to run

    def generate_summon_command(self):
        # generates base summon command. will be used to summon first command block, which everything else is 'riding' on
        #  using python f-strings, all '{{' and '}}' will be rendered as a single '{' or '}', and all like '{self.command}' will be rendered as the contents of self.command, etc
        return f'/summon minecraft:falling_block ~ ~2 ~ {{Time:1,Motion:[0d,0d,0d],BlockState:{{Name:"{self.blockType}",Properties:{{facing:"up"}}}},TileEntityData:{{auto:{int(not self.needsRedstone)},Command:"{self.command}"}}%s}}'

    def generate_additional_command(self):
        # generates string to add to base to add additional command. this adds a 'rider', the rider being a falling command block
        # uses f-strings, see above
        return f',Passengers:[{{id:armor_stand,Health:0,Passengers:[{{id:falling_block,Time:1,BlockState:{{Name:"{self.blockType}",Properties:{{conditional:"{self.conditional}",facing:"up"}}}},TileEntityData:{{auto:{int(not self.needsRedstone)},Command:"{self.command}"}}%s}}]}}]'

def build_command():
    global commandList
    one_command = commandblockcommand("/fill ~ ~ ~ ~ ~-1 ~ air", "command_block", False, False).generate_summon_command()
    for c in commandList:
        one_command = one_command % c.generate_additional_command()
    one_command = one_command % ""
    return one_command

def parse_user_input(userInput):
    # user input should be list of commands, seperated with " && " (spaces are important), and each command should begin with a 3 character string like "R01" (reapeating, unconditional, needs redstone)
    # first char is N, R, or C (normal, reapeating, or chain), next is 0 or 1 for conditional, and 0 or 1 for needs redstone
    # for example:
    # main.py "N01 give @p diamond && R00 kill herobrine"
    global commandList
    userInput = userInput.split(' && ')
    for c in userInput:
        settings=c[:3].upper()
        command=c[4:]
        # character 4 should be a space and is ignored
        blockType = {'N':'command_block', 'R':'repeating_command_block', 'C':'chain_command_block'}[settings[0]]
        conditional = bool(int(settings[1]))
        needsRedstone = bool(int(settings[2]))
        commandList.append(commandblockcommand(command, blockType, conditional, needsRedstone))


def main():
    try:
        parse_user_input(sys.argv[1])
    except Exception as e:
        print(e)
        print('''usage:
        input should be list of commands, seperated with " && " (spaces are important), and each command should begin with a 3 character settings-string, such as "R01" (this one means reapeating, unconditional, needs redstone)

        first char of settings-string is N, R, or C (normal, reapeating, or chain), next is 0 or 1 for conditional, and 0 or 1 for needs redstone

        example:
        steve@mojang: ~/minecraft-one-command-generator$ main.py "N01 give @p diamond && R00 kill herobrine"''')
        quit()
    print(build_command())

if __name__=="__main__":
    main()
