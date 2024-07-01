from collections import deque

graph = {}


graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


mango_seller = {
    "you": False,
    "bob": False,
    "alice": False,
    "claire": True,
    "anuj": False,
    "peggy": False,
    "thom": False,
    "jonny": False
}



def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if mango_seller[person]:
                print (person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")

