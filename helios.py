''' Helios - init, start, save, reset workspaces

copyright 2020, Franz Ludwig Kostelezky <info@kostelezky.com>

add command-alias:
    - Windows: add directory to %PATH%
'''

import os
import sys
import pickle
import webbrowser

class Helios():
    '''
    docstring
    '''

    def __init__(self):
        ''' Call this at first time

        Path to browser may vary  on different operating systems.

        Class-variables:
            - (str) _browser_path
            - (dict of 2d array) _workspace
        '''

        self._browser_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        self._workspace = {
            'main': [['websites', 'github.com/flemk/helios'],
                ['shell commands', 'echo hello world']], 
            'private': [['mail.google.com'],
                []]
        }

    def workspace_print(self, workspace=None):
        ''' Print out all workspaces
        '''

        if workspace is None:
            # print all workspaces
            for workspace, content in self._workspace.items():
                web, cmd = content
                print('%s:' % (workspace))
                print('  -web:')
                [print('    %s' % (el)) for el in web]
                print('  -cmd:')
                [print('    %s' % (el)) for el in cmd]
                print('\n')
        else:
            # print only one workspace
            web, cmd = self._workspace[workspace]
            print('%s:' % (workspace))
            print('  -web:')
            [print('    %s' % (el)) for el in web]
            print('  -cmd:')
            [print('    %s' % (el)) for el in cmd]

        input('PRESS ENTER TO EXIT')

    def workspace_edit(self, workspace=None, action=None, appendix=None):
        '''
        '''
        if action is None or workspace is None:
            print('Information missing (action|workspace)')
            return 1

        if action == 'new':
            print('Creating new workspace %s' % (workspace))
            self._workspace[workspace] = [[], []]
        elif action == 'remove':
            if input('Do you want to remove %s ? (y/n)' % (workspace)) == 'y':
                del self._workspace[workspace]
            else:
                print('removing aborted')
        elif action == 'add-web' and appendix is not None:
            print('Appending web: %s to %s' % (appendix, workspace))
            self._workspace[workspace][0].append(appendix)
        elif action == 'add-cmd' and appendix is not None:
            print('Appending cmd: %s to %s' % (appendix, workspace))
            self._workspace[workspace][1].append(appendix)
        else:
            print('no action has been specified')
            return 1

    def workspace_start(self, workspace='main'):
        '''
        '''
        for el in self._workspace[workspace][0]:
            webbrowser.get(self._browser_path).open(el)

        for el in self._workspace[workspace][1]:
            os.system(el)

def print_usage():
    ''' prints usage via print and awaits input (pauses) then exits.
    '''
    print('helios.py param1 [param2, ...]\n')
    print('for more information visit: github.com/flemk/helios')
    print('')
    print('param1')
    print('  help')
    print('  open [name of workspace]')
    print('  print [name of workspace]')
    print('  edit <name of workspace>')
    print('    new')
    print('    remove')
    print('    add-web <weblink>: add weblink to workspace. No spaces allowed.')
    print('    add-cmd <command>: add cmd to workspace. No spaces allowed')
    input('PRESS ENTER TO EXIT')

def main():
    ''' selects which action should be performed
    '''

    # if helios has already been configured, load configuration of config_path
    script_path = os.path.dirname(sys.argv[0])
    config_path = os.path.join(script_path, 'config.pkl')
    print(config_path)
    try:
        #h = load(config_path, allow_pickle=True)
        h = pickle.load(open(config_path, 'rb'))
    except FileNotFoundError:
        h = Helios()
        #save(config_path, h)
        with open(config_path, 'wb') as file:
            pickle.dump(h, file, pickle.HIGHEST_PROTOCOL)

    # parse command line arguments
    args = sys.argv
    l = len(args)
    if l > 1:
        if args[1] == 'help':
            print_usage()
        elif args[1] == 'print':
            t = None if l < 3 else args[2]
            h.workspace_print(t)
        elif args[1] == 'open' and l >= 2:
            t = 'main' if l <= 2 else args[2]
            print('Opening %s' % (t))
            h.workspace_start(t)
        elif args[1] == 'edit' and l >= 4:
            print('Editing %s' % (args[2]))
            t = None if l <= 4 else args[4]
            h.workspace_edit(workspace=args[2], action=args[3], appendix=t)

            with open(config_path, 'wb') as file:
                pickle.dump(h, file, pickle.HIGHEST_PROTOCOL)
    else:
        print_usage()

if __name__ == "__main__":
    main()