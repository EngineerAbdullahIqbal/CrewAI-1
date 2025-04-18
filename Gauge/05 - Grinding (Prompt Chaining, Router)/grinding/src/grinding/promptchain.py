from crewai.flow.flow import Flow , start , listen
from litellm import completion

API_KEY = "AIzaSyALmE5GLBYqPFTWOJq-cy4tr2MRPXG12Ac"


class CityFunFact(Flow):

    @start()
    def genertate_random_city(self):
        result = completion(
            model="gemini/gemini-1.5-flash",
            api_key=API_KEY,
            messages=[{"content":"Generate any random city name From Pakistan",
                       "role":"user"}]
        )
        city = result['choices'][0]['message']['content']
        print(f"City Name: {city}")
        return city
    
    @listen(genertate_random_city)
    def genertate_fun_fact(self , city_name):
        result = completion(
            model="gemini/gemini-2.0-flash-exp",
            api_key=API_KEY,
            messages=[{"content":f"Write some FunFAct About {city_name} City",
                       "role":"user"}]
        )
        fun_fact = result['choices'][0]['message']['content']
        print(f"City Name: {fun_fact}")
        self.state['fun_fact'] = fun_fact

    @listen(genertate_fun_fact)
    def save_fun_fact(self):
        with open('FunFact.md' , 'w') as f:
            f.write(self.state['fun_fact'])
            return self.state['fun_fact']

def kickoff():
    obj = CityFunFact()
    result = obj.kickoff()
    print(result)


def plot():
    obj = CityFunFact()
    obj.plot()