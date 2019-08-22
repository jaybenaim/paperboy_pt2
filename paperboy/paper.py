class Paperboy: 
    '''
    This class will represent a paperboy and his amount of papers delivered and amount 
    of money made 
    ''' 

    def __init__(self, name='', experience='', earnings = 0): 
        self.name = name
        self.experience = experience 
        self.earnings = earnings
          
        
    def __str__(self): 
        return f'My name is {self.name}, I made {self.earnings} delivering {int(self.quota())} papers.'
    
    def quota(self): 
        papers = 50 
        new_quota = self.experience / 2
        if self.experience <= 0: 
            return papers 
        elif self.experience >= 0: 
            papers += new_quota
            return papers 
        
    def deliver(self, start_addr, end_addr): 
        

        total_houses = end_addr - start_addr + 1 
         
        if self.quota() > total_houses: 
            self.earnings += round((total_houses * .25 ) - 2, 2) 
        elif self.quota() < total_houses: 
            diff = total_houses - self.quota()
            diff *= .50
            qu = self.quota() * .25  
            total = qu + diff 
            self.earnings += round(total, 2) 
            
            
            
    def report(self): 
        return f''' 
        My name is {self.name}, 
        I\ve delivered {self.quota()} papers, 
        and I have made ${self.earnings}. :) 
        ''' 


jack = Paperboy('Jack', 5)
jack.quota() # 80
jack.deliver(1, 75) # 16.75
jack.earnings # 34.25
jack.report() # "I'm Tommy, I've been delivered 135 papers and I've earned $34.25 so far!"

print(jack) 

tommy = Paperboy("Tommy", 0)

tommy.quota() #  50
tommy.deliver(101, 160) # 17.5
tommy.earnings # 17.5
tommy.report() # "I'm Tommy, I've delivered 60 papers and I've earned $17.5 so far!"


print(tommy)

rocky = Paperboy("Rocky", 60)

rocky.quota() # 80
rocky.deliver(1, 75) # 16.75
rocky.earnings # 34.25
rocky.report() # "I'm Tommy, I've been delivered 135 papers and I've earned $34.25 so far!"

print(rocky) 
