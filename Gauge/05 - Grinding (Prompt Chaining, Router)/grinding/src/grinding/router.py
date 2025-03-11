from crewai.flow.flow import Flow, start, listen, router
import random

class CityFlow(Flow):

    @start()
    def choose_city(self):
        print("Hello!")
        cities = ["New York", "London", "Tokyo"]
        selected_city = random.choice(cities)
        self.state['city'] = selected_city

    @router(choose_city)
    def route_city(self):
        if self.state['city'] == "New York":
            return "New York"
        elif self.state['city'] == "London":
            return "London"
        else:
            return "Tokyo"

    @listen("New York")
    def fun_fact_ny(self):
        return f"Write some fun fact about {self.state['city']} city."
    
    @listen("London")
    def fun_fact_london(self):
        return f"Write some fun fact about {self.state['city']} city."
    
    @listen("Tokyo")
    def fun_fact_tokyo(self):
        return f"Write some fun fact about {self.state['city']} city."

def kickoff():
    obj = CityFlow()
    result = obj.kickoff()
    print(result)

def plot():
    obj = CityFlow()
    obj.plot()
