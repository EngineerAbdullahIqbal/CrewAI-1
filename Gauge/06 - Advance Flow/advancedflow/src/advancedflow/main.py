from crewai.flow.flow import Flow, start, listen
from dotenv import load_dotenv, find_dotenv
from litellm import completion
from advancedflow.crews.teaching_crew.teaching_crew import TeachingCrew 
import os

load_dotenv(find_dotenv())

class AdvancedFlow(Flow):
    @start()
    def generate_topic(self):
        response = completion(
            model = os.getenv("MODEL"),
            messages = [
                {
                    "role":"user",
                    "content":"select a topic for a blog post about the benefits of AI.",
                }
            ],
            max_tokens=100,
            temperature=0.5,
        )
        self.state['topic'] = response['choices'][0]['message']['content']
        print(f"STEP 1: {self.state['topic']}")
        return self.state['topic']

    @listen("generate_topic")
    def generate_content(self):
        print("STEP 2: Generating Content")
        result = ( 
            TeachingCrew()
            .crew()
            .kickoff(inputs={
                "topic": self.state['topic']
            }
        )
        )

        print("Genrated Content", result.raw)
        self.state['content'] = result.raw
        
        
                
def kickoff():
    flow = AdvancedFlow()
    flow.kickoff()


if __name__ == "__main__":
    kickoff()
    