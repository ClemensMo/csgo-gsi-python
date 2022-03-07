import time

from lights import handle_light_events
from server import GSIServer

if __name__ == '__main__':
    server = GSIServer(("192.168.0.174", 3000), "S8RL9Z6Y22TYQK45JB4V8PHRJJMD9DS9")
    server.start_server()

    while True:
        print(server.gamestate.map.name)
        print(server.get_info("player", "state", "flashed"))
        handle_light_events(server.get_info("player", "state", "flashed"),
                            server.get_info("player", "state", "flashed"),
                            server.get_info("player", "state", "health"),
                            server.get_info("player", "state", "burning"))