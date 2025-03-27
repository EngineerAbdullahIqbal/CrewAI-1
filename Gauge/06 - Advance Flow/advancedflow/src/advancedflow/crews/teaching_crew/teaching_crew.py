from crewai import Agent, Task, Crew , Process
from crewai.project import CrewBase, agent, crew , task 
from crewai import LLM
import os

my_llm = LLM(
    model=os.getenv("MODEL"),
    api_key=os.getenv("GEMINI_API_KEY"),
)

@CrewBase
class TeachingCrew:
   # 1. Agent 
   agents_config = "config/agents.yaml"
   tasks_config = "config/tasks.yaml"
   
   @agent
   def senior_lecturer(self) -> Agent:
       return Agent(
           config=self.agents_config["senior_lecturer"],
           llm=my_llm
       )
       
   # 2. Task
   @task
   def take_lecture(self) -> Task:
       return Task(
           config=self.tasks_config["take_lecture"], 
       )
   
   # 3. Crew
   @crew
   def crew(self) -> Crew:
       return  Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
            # process=Process.sequential,
            llm=my_llm
       )