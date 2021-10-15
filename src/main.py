from lib.startup import MiceInkStartup

def main():
    startup = MiceInkStartup()
    startup.start() # starts main miceink process

try:
    main()
except KeyboardInterrupt:
    print("KeyboardInterrupt: Exiting...")