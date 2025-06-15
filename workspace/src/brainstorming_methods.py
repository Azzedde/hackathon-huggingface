from smolagents import CodeAgent
from smolagents import Tool


sb_questions_prompt = """You are a clever question generator assistant that helps people in brainstorming and generating from one idea to 6 questions following the starbursting brainstorming principles: the 5 W's and 1 H (Who, What, Where, When, Why, How) to explore a topic comprehensively. The resulting questions should be diverse, detailed, developed, precise and significant. The questions must not be redundant and repetitive, be creative and unique. The question must be formatted in the form of bullet points without titles and without bold text.
Idea to brainstorm:{idea}
List of 6 bullet questions:"""

sb_answer_prompt = """You are a clever answer assistant that helps people in answering questions related to a topic. You'll be having a question and you need to generate a detailed, developed, precise and significant answer to the question, according to a context given from the user. The answer should not be redundant and repetitive, be creative and unique. The answer must be formatted in the form of a paragraph.
Question:{question}
Context:{idea}
Answer:"""


# Helper function to parse bullet points from a string
def _parse_bullet_points(text: str) -> list[str]:
    return [line.strip() for line in text.split('\n') if line.strip().startswith('- ') or line.strip().startswith('* ')]


# wrapping up the starbursting chains
def sb(user_query, agent: CodeAgent):
    output_content = []
    output_content.append(f"# Brainstorming for: {user_query}\n")

    class StarburstingQuestionsGenerator(Tool):
        name = "starbursting_questions_generator"
        description = "Generates 6 questions following the starbursting brainstorming principles: the 5 W's and 1 H (Who, What, Where, When, Why, How) to explore a topic comprehensively. Takes 'idea' as input and returns bullet points."
        inputs = {"idea": {"type": "string", "description": "The idea to generate starbursting questions for."}}
        output_type = "string"

        def forward(self, idea: str) -> str:
            questions_raw = agent.run(sb_questions_prompt.format(idea=idea))
            if isinstance(questions_raw, list):
                questions_raw = "".join(questions_raw)
            questions = _parse_bullet_points(questions_raw)
            return "\n".join(questions)

    class QuestionAnswerer(Tool):
        name = "question_answerer"
        description = "Generates a detailed, developed, precise and significant answer to a question according to a given context. Takes 'question' and 'idea' as input and returns a paragraph answer."
        inputs = {"question": {"type": "string", "description": "The question to answer."},
                  "idea": {"type": "string", "description": "The context idea for the answer."}}
        output_type = "string"

        def forward(self, question: str, idea: str) -> str:
            return agent.run(sb_answer_prompt.format(question=question, idea=idea))

    sb_questions_tool = StarburstingQuestionsGenerator()
    sb_answer_tool = QuestionAnswerer()

    questions_raw = sb_questions_tool.forward(user_query)
    # questions = _parse_bullet_points(questions_raw) # No need to parse here, already parsed in StarburstingQuestionsGenerator

    output_content.append("#### Starbursting Questions:\n")
    output_content.append(questions_raw + "\n") # Append questions directly

    for j, question in enumerate(questions_raw):
        output_content.append(f"- **Question {j+1}:** {question}\n")

        answer = sb_answer_tool.forward(question=question, idea=user_query)
        output_content.append(f"  - **Answer:** {answer}\n")
    output_content.append("\n") # Add a newline for separation between ideas

    return "\n".join(output_content)