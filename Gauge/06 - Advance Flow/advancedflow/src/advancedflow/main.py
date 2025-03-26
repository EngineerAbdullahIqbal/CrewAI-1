from crewai.flow.flow import Flow, start, listen
from dotenv import load_dotenv, find_dotenv
from litellm import completion
from advancedflow.crews.teaching_crew.teaching_crew import TeachingCrew 

_: bool = load_dotenv(find_dotenv())

class AdvancedFlow(Flow):
    @start
    def generate_topic(self):
        response = completion(
            model = "gemini/gemini-1.5-flash",
            messages = [
                {
                    "role":"user",
                    "content":"Generate a topic for a blog post about the benefits of AI.",
                }
            ],
            max_tokens=100,
            temperature=0.5,
        )
        self.state['topic'] = response['choices'][0]['message']['content']
        print(f"STEP 1: {self.state['topic']}")
        
    @listen("generate_topic")
    def generate_content(self):
        print("STEP 2: Generating Content")
        result = TeachingCrew().crew().kcikoff(
            inputs={
                "topic": self.state['topic']
            }
        )
        print(teaching_crew)
        
        
                
def kickoff():
    flow = AdvancedFlow()
    flow.kickoff()
    