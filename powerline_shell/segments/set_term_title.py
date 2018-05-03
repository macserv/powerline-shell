import os
import socket
from ..utils import BasicSegment


class Segment(BasicSegment):

    def add_to_powerline(self):
    
        powerline         = self.powerline
        term              = os.getenv('TERM')
        is_apple_terminal = ( 'Apple_Terminal' in os.getenv('TERM_PROGRAM') )

        if not (('xterm' in term) or ('rxvt' in term)):
            return
            
        if powerline.args.shell == 'bash':
            set_title = '\\[\\e]0;\\u@\\h: \\w\\a\\]'
            
        elif powerline.args.shell == 'zsh':
            set_title = '%{\033]0;%n@%m: %~\007%}'
            
        elif powerline.args.shell == 'tcsh':
        
            window_title_text  = "%n@%m: %/"
            set_title          = "%{\033]0;" + window_title_text + "\a%}"  # Xterm Command: Window Title
            
            if is_apple_terminal:
                set_title += "%{\033]7;" + "%/" + "\a%}"                    # OS Command: Working Directory
                set_title += "%{\033]2;" + window_title_text + "\a%}"       # OS Command: Window Title
                set_title += "%{\033]1;" + "I AM TAB" + "\a%}"              # OS Command: Tab Title
                
        else:
            set_title = '\033]0;%s@%s: %s\a' % (
                os.getenv('USER'),
                socket.gethostname().split('.')[0],
                powerline.cwd,
            )
                
        powerline.append(set_title, None, None, '')
