from strands import Agent
from strands.models import BedrockModel
import session

aws_session = session.Session(profile_name='default', region_name='us-east-1')

bedrock_model = BedrockModel(
    model_id="us.anthropic.claude-haiku-4-5-20251001-v1:0",
    boto_session=aws_session.create_session()
)

agent = Agent(
    model=bedrock_model, 
    name='Bedrock',
    system_prompt='''Eres un asistente de lenguaje natural llamado Bedrock.
    Cuando el usuario inicie la conversación, preséntate de forma amigable 
    y ofrece tu ayuda.''')

# Ask the agent a question
response = agent("Haz de cuenta que eres un experto en historia y dime quién fue el primer presidente de los Estados Unidos.")
print(response)