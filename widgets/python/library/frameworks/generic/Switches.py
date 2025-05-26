import sys
import argparse

class Switch:
    def __init__(self, name, switches, help_text, is_required=False):
        self.name = name
        self.switches = switches.split(',')
        self.help_text = help_text
        self.is_required = is_required
        self.active = False
        self.values = []

class Switches:
    def __init__(self):
        self.switches = {}

    def register(self, name, switches, help, isRequired=False):
        self.switches[name] = Switch(name, switches, help, isRequired)

    def process(self):
        args = sys.argv[1:]
        found_switches = set()
        
        for i, arg in enumerate(args):
            for switch in self.switches.values():
                if arg in switch.switches:
                    switch.active = True
                    found_switches.add(switch.name)
                    if i + 1 < len(args) and not args[i + 1].startswith('-'):
                        switch.values = args[i + 1].split(',')
        
        missing_required = [sw.name for sw in self.switches.values() if sw.is_required and not sw.active]
        if '--help' in args or missing_required:
            self.show_help(missing_required)

    def isActive(self, name):
        return self.switches.get(name, Switch("", "", "")).active

    def value(self, name):
        return ','.join(self.switches.get(name, Switch("", "", "")).values)

    def values(self, name):
        return self.switches.get(name, Switch("", "", "")).values

    def show_help(self, missing_required):
        print("\033[1;36m{}\033[0m".format(app.app))
        print("\033[1;33m{}\033[0m".format(app.name))
        print("\033[1;37;46m{}\033[0m".format(app.description))
        print("\nAvailable Switches:")

        for i, switch in enumerate(self.switches.values()):
            color = "\033[1;36m" if i % 2 == 0 else "\033[1;36m"
            print(f"{color}{switch.name:<15}\033[0m - {switch.help_text:<30} {', '.join(switch.switches)}")

        if missing_required:
            print("\n\033[1;31mMissing required switches:\033[0m", ', '.join(missing_required))
        sys.exit(1)

class App:
    def __init__(self):
        self.app = ""
        self.name = ""
        self.description = ""
        self.tags = ""

    def register(self, app, name, description, tags):
        self.app = app
        self.name = name
        self.description = description
        self.tags = tags



def init():
    return App(), Switches()

# Example usage:
if __name__ == "__main__":
    switches = Switches()
    app = App()
    app.register(
        app='myFiles.py', 
        name='File Search Tool', 
        description='Searches for files in a given folder with optional recursion', 
        tags='utility,os navigation,os,file,search'
    )

    switches.register(name='Folders', switches='-f,-fo,-folder,-folders', help='Specify folders', isRequired=True)
    switches.register(name='Recursive', switches='-r,-recursive', help='Enable recursion', isRequired=False)
    
    switches.process()



    # Example to check switches
    if switches.isActive('Folders'):
        print("Folders switch is active:", switches.value('Folders'))
