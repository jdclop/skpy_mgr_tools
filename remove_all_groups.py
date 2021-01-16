from skpy import Skype, SkypeChats, SkypeApiException

class SkypeManager(Skype):

    def __init__(self,user,pwd):        
        self.elements = {}
        self.usr = user
        self.password = pwd
        super().__init__(self)        


    def connect(self):
        self.conn.soapLogin(self.usr,self.password)
    
    def remove_all_groups(self):
        print("Showing all chats to be deleted...",end="\n\n")
        self.getChats()
        sure = input("Are you sure to remove all chats? y/n")        
        sure = True if sure == "y" else False
        if sure:
            self.remove_groups()
        print("\nFinished.")
        

    def getChats(self):
        
        self.skc = SkypeChats(self)
        chts = self.skc.recent()
        while chts:
            for el in chts:
                if el.startswith("19"):                                                            
                    self.elements[el] = chts.get(el).topic
                    print(chts.get(el).topic,"->",el)            
                        
            chts = self.skc.recent()

        
    def remove_groups(self):
        for k,v in self.elements.items():
            try:
                print("Leaving",v,"with key:",k,"...",end="")
                self.skc.chat(k).leave()
                print("Left Success!")
                print("Deleting",v,"with key:",k,"...",end="")
                self.skc.chat(k).delete()
                print("Deletion Success!")
            except SkypeApiException as sae:
                print("Failed! :(")
                print("\tCaused by:",sae)
        
            
    

user = "YOUR SKYPE USER HERE"
pwd = "YOUR PASSWORD HERE"

sk = SkypeManager(user,pwd)
sk.connect()
sk.remove_all_groups()
