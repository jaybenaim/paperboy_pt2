from django.db import models 
from django.forms import ModelForm
from django import forms 
class Paperboy(models.Model): 
    name = models.CharField(max_length=255) 
    experience = models.FloatField(null=False) 
    start_house_number = models.IntegerField(null=False)
    end_house_number = models.IntegerField(null=False)
    total_earnings = []
    earnings = 0 

        
    def __str__(self): 
        return f'My name is {self.name}, I made {self.earnings} delivering {int(self.quota())} papers.'
    
    @classmethod 
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
    @classmethod 
    def total_earnings(cls): 
        return sum(total_earnings) 


# class Paperboy(ModelForm): 
#     class Meta: 
#         model = Paperboy
#         fields = ['name', 'experience' , 'earnings']

