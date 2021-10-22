from lib.app import MiceInkApp

def main():
    startup = MiceInkApp()
    startup.start() # starts main miceink process

try:
    main()
except KeyboardInterrupt:
    print("KeyboardInterrupt: Exiting...")