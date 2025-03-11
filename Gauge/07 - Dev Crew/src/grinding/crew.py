from crewai.flow import Flow, start, listen
from grinding.crews.dev_crew.dev_crew import DevCrew

class DevFlow(Flow):
    @start()
    def crew_run(self):
        output = DevCrew().crew().kickoff(inputs= 
                                   {"problem": "Write a code to find the sum of all elements in an array."}
                                )
        return output.raw
    
def kickoff():
    flow = DevFlow()
    flow.kickoff()
