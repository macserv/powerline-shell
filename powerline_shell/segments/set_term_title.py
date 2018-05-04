import os
import socket
from ..utils import BasicSegment


class Segment(BasicSegment):

    def add_to_powerline(self):
    
        powerline         = self.powerline
        shell             = powerline.args.shell
        term              = os.getenv('TERM')
        is_apple_terminal = ( 'Apple_Terminal' in os.getenv('TERM_PROGRAM') )

        if not (('xterm' in term) or ('rxvt' in term)):
            return
            
        if shell == 'bash':
            set_title = '\\[\\e]0;\\u@\\h: \\w\\a\\]'
            
        elif shell == 'zsh':
            set_title = '%{\033]0;%n@%m: %~\007%}'
            
        elif shell == 'tcsh':
            
            if is_apple_terminal:   
                set_title  = "%{\033]7;" + "%/"    + "\a%}"  # OS Command: Working Directory
#               set_title += "%{\033]2;" + "%n@%m" + "\a%}"  # OS Command: Window Title
#               set_title += "%{\033]1;" + "%c"    + "\a%}"  # OS Command: Tab Title
                
            else:
                set_title = "%{\033]0;" + "%n@%m: %/" + "\a%}"

        else:
            set_title = '\033]0;%s@%s: %s\a' % (
                os.getenv('USER'),
                socket.gethostname().split('.')[0],
                powerline.cwd,
            )
                
        powerline.append(set_title, None, None, '')
