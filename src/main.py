from lib.app import InkApp

def main():
    startup = InkApp()
    startup.start() # starts main app process

try:
    main()
except KeyboardInterrupt:
    print("KeyboardInterrupt: Exiting...")