from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class TeachingCrew:
   # 1. Agent 
   agent_config = "config/agents.yaml"
   task_config = "config/tasks.yaml"
   
   @agent
   def sir_me_agent(self) -> Agent:
       return Agent(
           config=self.agent_config["sir_me"],
       )
       
   # 2. Task
   @task
   def describe_topic_task(self) -> Task:
       return Task(
           config=self.task_config["describe_topic"],
       )
   
   # 3. Crew
   def teaching_crew(self) -> Crew:
       return  Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True
       )