from crewai import Agent, Task, Crew
from pydantic import BaseModel
import os

# Simple Procurement Agent example
procurement_agent = Agent(
    role='Procurement Specialist',
    goal='Find best prices for parts and order them for maximum profit',
    backstory='Expert in pool equipment suppliers and price optimization',
    verbose=True
)

# Simple task
task = Task(
    description='Find best price for pool pump and schedule delivery',
    agent=procurement_agent,
    expected_output='Best supplier, price, and delivery plan'
)

crew = Crew(
    agents=[procurement_agent],
    tasks=[task]
)

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
