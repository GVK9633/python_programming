from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama3-70b-8192"),  # Replace with the latest valid model
    markdown=True
)

agent.print_response("future of agentic AI")

# https://github.com/kodigitaccount/AGENTIC_AI/tree/main
