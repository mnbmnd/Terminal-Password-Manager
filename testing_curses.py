import curses

def get_password_with_reveal(stdscr):
    """Get password with ability to reveal by holding spacebar"""
    curses.curs_set(1)
    stdscr.clear()
    
    prompt = "Enter password (hold SPACE to reveal): "
    stdscr.addstr(0, 0, prompt)
    stdscr.refresh()
    
    password = []
    reveal = False
    cursor_pos = len(prompt)
    
    while True:
        stdscr.move(0, cursor_pos)
        key = stdscr.getch()
        
        # Enter key - submit password
        if key in [curses.KEY_ENTER, 10, 13]:
            break
            
        # Spacebar - toggle reveal
        elif key == ord(' '):
            reveal = not reveal
            # Redraw password with current reveal state
            stdscr.move(0, len(prompt))
            stdscr.clrtoeol()
            if reveal:
                stdscr.addstr(''.join(password))
            else:
                stdscr.addstr('*' * len(password))
            cursor_pos = len(prompt) + len(password)
            
        # Backspace
        elif key in [curses.KEY_BACKSPACE, 127, 8]:
            if password:
                password.pop()
                stdscr.move(0, len(prompt))
                stdscr.clrtoeol()
                if reveal:
                    stdscr.addstr(''.join(password))
                else:
                    stdscr.addstr('*' * len(password))
                cursor_pos = len(prompt) + len(password)
                
        # Regular character
        elif 32 <= key <= 126:  # Printable ASCII
            char = chr(key)
            password.append(char)
            if reveal:
                stdscr.addch(char)
            else:
                stdscr.addch('*')
            cursor_pos += 1
    
    return ''.join(password)

def main(stdscr):
    password = get_password_with_reveal(stdscr)
    
    # Clear screen and show result
    stdscr.clear()
    stdscr.addstr(0, 0, f"Password received: {password}")
    stdscr.addstr(1, 0, f"Length: {len(password)}")
    stdscr.addstr(2, 0, "Press any key to exit...")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)