import random

# Names:
# Date:
# Pokemon Simulator

# Initialize

# Global variables
pokemon_level = 0
pokemon_name = " "
pokemon_ascii_art = ""

# Functions

# Function to evolve Pokémon based on level
def evolve_pokemon():
    global pokemon_level, pokemon_name, pokemon_ascii_art
    if pokemon_level >= 10:
        pokemon_name = "Charizard"
        
        print("                 .\"-,.__\n");
        print("                 `.     `.  ,\n");
        print("              .--'  .._,'\"-' `.\n");
        print("             .    .'         `'\n");
        print("             `.   /          ,'\n");
        print("               `  '--.   ,-\"'\n");
        print("                `\"`   |  \\\n");
        print("                   -. \\, |\n");
        print("                    `--Y.'      ___.\n");
        print("                         \\     L._, \\\n");
        print("               _.,        `.   <  <\\                _\n");
        print("             ,' '           `, `.   | \\            ( `\n");
        print("          ../, `.            `  |    .\\`.           \\ \\_\n");
        print("         ,' ,..  .           _.,'    ||\\l            )  '\".\n");
        print("        , ,'   \\           ,'.-.`-._,'  |           .  _._`.\n");
        print("      ,' /      \\ \\        `' ' `--/   | \\          / /   ..\\\n");
        print("    .'  /        \\ .         |\\__ - _ ,'` `        / /     `.`.\n");
        print("    |  '          ..         `-...-\"  |  `-'      / /        . `.\n");
        print("    | /           |L__           |    |          / /          `. `.\n");
        print("   , /            .   .          |    |         / /             ` `\n");
        print("  / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \\\n");
        print(" / .           \\\"`_/. `-_ \\_,.  ,'    +-' `-'  _,        ..,-.    \\`.\n");
        print(".  '         .-f    ,'   `    '.       \\__.---'     _   .'   '     \\ \\\n");
        print("' /          `.'    l     .' /          \\..      ,_|/   `.  ,'`     L`\n");
        print("|'      _.-\"\"` `.    \\ _,'  `            \\ `.___`.'\"`-.  , |   |    | \\\n");
        print("||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|\n");
        print("||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||\n");
        print("|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||\n");
        print("||/            _,-------7 '              . |  `-'    l         /    `||\n");
        print(". |          ,' .-   ,' ||               | .-.        `.      .'     ||\n");
        print(" `'        ,'    `\".'    |               |    `.        '. -.'       `'\n");
        print("          /      ,'      |               |,'    \\-.._,.'/'\n");
        print("          .     /        .               .       \\    .''\n");
        print("        .`.    |         `.             /         :_,'.'\n");
        print("          \\ `...\\   _     ,'-.        .'         /_.-'\n");
        print("           `-.__ `,  `'   .  _.>----''.  _  __  /\n");
        print("                .'        /\"'          |  \"'   '_\n");
        print("               /_|.-'\\ ,\".             '.'`__'-( \\\n");
        print("                 / ,\"'\"\\,'               `/  `-.|\" mh\n");
        
    elif pokemon_level >= 5:
        pokemon_name = "Charmeleon"
        
        print("                      ,-'`\\\n");
        print("                  _,\"'    j\n");
        print("           __....+       /               .\n");
        print("       ,-'\"             /               ; `-._.'.\n");
        print("      /                (              ,'       .'\n");
        print("     |            _.    \\             \\   ---._ `-.\n");
        print("     ,|    ,   _.'  Y    \\             `- ,'   \\   `.`.\n");
        print("     l'    \\ ,'._,\\ `.    .              /       ,--. l\n");
        print("  .,-        `._  |  |    |              \\       _   l .\n");
        print(" /              `\"--'    /              .'       ``. |  )\n");
        print(".\\    ,                 |                .        \\ `. '\n");
        print("`.                .     |                '._  __   ;. \\'\n");
        print("  `-..--------...'       \\                  `'  `-\"'.  \\\n");
        print("      `......___          `._                        |  \\\n");
        print("               /`            `..                     |   .\n");
        print("              /|                `-.                  |    L\n");
        print("             / |               \\   `._               .    |\n");
        print("           ,'  |,-\"-.   .       .     `.            /     |\n");
        print("         ,'    |     '   \\      |       `.         /      |\n");
        print("       ,'     /|       \\  .     |         .       /       |\n");
        print("     ,'      / |        \\  .    +          \\    ,'       .'\n");
        print("    .       .  |         \\ |     \\          \\_,'        / j\n");
        print("    |       |  L          `|      .          `        ,' '\n");
        print("    |    _. |   \\          /      |           .     .' ,'\n");
        print("    |   /  `|    \\        .       |  /        |   ,' .'\n");
        print("    |   ,-..\\     -.     ,        | /         |,.' ,'\n");
        print("    `. |___,`    /  `.   /`.       '          |  .'\n");
        print("      '-`-'     j     ` /.\"7-..../|          ,`-'\n");
        print("                |        .'  / _/_|          .\n");
        print("                `,       `\"'/\"'    \\          `.\n");
        print("                  `,       '.       `.         |\n");
        print("             __,.-'         `.        \\'       |\n");
        print("            /_,-'\\          ,'        |        _.\n");
        print("             |___.---.   ,-'        .-':,-\"`\\,' .\n");
        print("                  L,.--\"'           '-' |  ,' `-.\\\n");
        print("                                        `.' mh\n");
    else:
        pokemon_name = "Charmander"
        print("              _.--\"\"`-..\n");
        print("            ,'          `.\n");
        print("          ,'          __  `.\n");
        print("         /|          \" __   \\\n");
        print("        , |           / |.   .\n");
        print("        |,'          !_.'|   |\n");
        print("      ,'             '   |   |\n");
        print("     /              |`--'|   |\n");
        print("    |                `---'   |\n");
        print("     .   ,                   |                       ,\".\n");
        print("      ._     '           _'  |                    , ' \\ `\n");
        print("  `.. `.`-...___,...---\"\"    |       __,.        ,`\"   L,|\n");
        print("  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \\\n");
        print("-:..     `. `-..--_.,.<       `\"      / `.        `-/ |   .\n");
        print("  `,         \"\"\"\"'     `.              ,'         |   |  ',,\n");
        print("    `.      '            '            /          '    |'. |/\n");
        print("      `.   |              \\       _,-'           |       ''\n");
        print("        `._'               \\   '\"\\                .      |\n");
        print("           |                '     \\                `._  ,'\n");
        print("           |                 '     \\                 .'|\n");
        print("           |                 .      \\                | |\n");
        print("           |                 |       L              ,' |\n");
        print("           `                 |       |             /   '\n");
        print("            \\                |       |           ,'   /\n");
        print("          ,' \\               |  _.._ ,-..___,..-'    ,'\n");
        print("         /     .             .      `!             ,j'\n");
        print("        /       `.          /        .           .'/\n");
        print("       .          `.       /         |        _.'.'\n");
        print("        `.          7`'---'          |------\"'_.'\n");
        print("       _,.`,_     _'                ,''-----\"'\n");
        print("   _,-_    '       `.     .'      ,\\\n");
        print("   -\" /`.         _,'     | _  _  _.|\n");
        print("    \"\"--'---\"\"\"\"\"'        `' '! |! /\n");
        print("                            `\" \" -' mh\n");
        print("\n");
        print("\n");

# Function to display evolution messages
def display_pokemon():
    print("\nName: " + pokemon_name)
    print("Level: " + pokemon_level)
    print("Pokemon Art:")
    print(pokemon_ascii_art)

# Main

# User interaction loop / This while loop will keep running until you use the break command to end loop
while True:
    # Collect input
    print("\nMenu:")
    print("1. Train (increases pokemon level by 1)")
    print("2. Gym Battle (increases pokemon level by 2)")
    print("3. Display Pokemon")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Process Information
    if choice == '1':
        pokemon_level += 1
        evolve_pokemon()
    elif choice == '2':
        pokemon_level += 2
        evolve_pokemon()
    elif choice == '3':
        display_pokemon()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")