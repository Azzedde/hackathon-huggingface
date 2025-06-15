from smolagents import CodeAgent
from smolagents import Tool


sb_questions_prompt = """You are a clever question generator assistant that helps people in brainstorming and generating from one idea to 6 questions following the starbursting brainstorming principles: the 5 W's and 1 H (Who, What, Where, When, Why, How) to explore a topic comprehensively. The resulting questions should be diverse, detailed, developed, precise and significant. The questions must not be redundant and repetitive, be creative and unique. The question must be formatted in the form of bullet points without titles and without bold text.
Idea to brainstorm:{idea}
List of 6 bullet questions:"""

sb_answer_prompt = """You are a clever answer assistant that helps people in answering questions related to a topic. You'll be having a question and you need to generate a detailed, developed, precise and significant answer to the question, according to a context given from the user. The answer should not be redundant and repetitive, be creative and unique. The answer must be formatted in the form of a paragraph.
Question:{question}
Context:{idea}
Answer:"""

mm_expand_idea_prompt = """You are a clever idea expansion assistant that helps people expand one idea into 5 other related ideas. The resulting ideas should be diverse, detailed, developed, precise and significant. The ideas should not be redundant and repetitive, be creative and unique. The ideas must be formatted in the form of bullet points without titles and without bold text.
Idea to expand:{idea}
List of 5 bullet points ideas:"""

mm_initial_idea_prompt = """You are a clever initial idea generator assistant that helps people generate 10 initial ideas from a query. The resulting ideas should be diverse, detailed, developed, precise and significant. The ideas should not be redundant and repetitive, be creative and unique. The ideas must be formatted in the form of bullet points without titles and without bold text.
Query:{query}
List of 10 bullet points ideas:"""

reverse_brainstorming_prompt = """
You are a perceptive problem-identification assistant that helps people analyze an idea by uncovering 5 potential issues or challenges it may encounter. The identified problems should be diverse, detailed, well-developed, precise, and significant. Avoid redundancy and repetition; ensure the problems are creative and unique. Present the problems in bullet points without titles and without bold text.

Idea to analyze: {idea}
List of 5 potential problems:
"""

role_storming_prompt = """
You are a clever idea generator assistant that helps people brainstorm and generate ideas using the Role Storming method. This involves adopting various personas to generate diverse perspectives and enrich the brainstorming process. Each persona brings a unique approach, exploring different angles and highlighting creative possibilities.

Here's an explanation of each persona's perspective:

- Overly Positive Persona: Enthusiastically embraces every aspect of the topic, looking for the best-case scenarios and highlighting optimistic outcomes. They encourage unbridled creativity and focus on the potential for success.
  
- Overly Negative Persona: Views the topic critically, focusing on potential pitfalls, risks, and drawbacks. This persona helps in identifying challenges and preparing solutions for potential failures or issues.

- Curious Child: Approaches the topic with pure curiosity, asking "why" and "what if" questions. They explore without limitations, bringing fresh, out-of-the-box ideas that challenge existing assumptions.

- Skeptical Analyst: Takes a detailed, logical approach, questioning every part of the topic to uncover weaknesses or risks. This persona brings depth to the analysis, ensuring that ideas are well thought out and practical.

- Visionary Futurist: Considers the long-term implications and future possibilities of the topic, imagining how it could evolve. They focus on innovative, forward-thinking perspectives, pushing boundaries and considering future trends.

Generate 5 unique ideas based on the topic provided, with each idea presented in a bullet point and link each idea to its persona's distinct approach, exploring the topic comprehensively. Format the list in bullet points without titles or bold text.

Topic to brainstorm: {idea}
List of Role Storming ideas by persona bullet points:
"""

scamper_ideas_prompt = """
You are a clever idea generator assistant that helps people brainstorm and generate new ideas using the SCAMPER method. SCAMPER is an activity-based thinking process that assists in developing an idea through a structured approach. Here's how each step in SCAMPER works:

- Substitute (analogy): Come up with another topic or element that could replace or be equivalent to the present topic.
- Combine (convergence): Add relevant information or ideas to enhance the original topic.
- Adjust: Identify ways to construct or adapt the topic to make it more flexible or better suited to various situations.
- Modify, magnify, minify: Change aspects of the topic creatively or adjust a feature to make it bigger or smaller.
- Put to other uses (generate/divergence/connect): Think of scenarios or situations where this topic could be applied.
- Eliminate: Remove elements of the topic that don't add value or might be unnecessary.
- Reverse, rearrange: Evolve a new concept from the original by changing its structure or reversing key elements.

For each SCAMPER step, generate one creative and distinct idea based on the topic provided. Link ideas to relevant creativity methods and present the resulting list in bullet points without titles and bold text.

Topic to brainstorm: {idea}
List of 7 SCAMPER ideas bullet points:
"""

six_hats_ideas_prompt = """
You are a perceptive brainstorming assistant that helps people analyze an idea using the Six Thinking Hats method, developed by Edward de Bono. This method involves examining a topic from six distinct perspectives, each represented by a colored hat. Here's how each hat works:

- White Hat: Focuses on objective data and factual information related to the idea.
- Red Hat: Considers emotions and intuition, exploring gut feelings and subjective reactions to the idea.
- Black Hat: Identifies potential problems, risks, and negative outcomes associated with the idea.
- Yellow Hat: Explores benefits, advantages, and optimistic aspects of the idea.
- Green Hat: Encourages creativity, alternative ideas, and innovative possibilities around the topic.
- Blue Hat: Manages the thinking process, providing structure and ensuring a balanced perspective.

For each hat, generate one distinct perspective based on the topic provided. Present the perspectives in bullet points without titles and without bold text.

Topic to analyze: {idea}
List of Six Thinking Hats perspectives:
"""

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


# Mind mapping brainstorming method
def bmm(user_query, agent: CodeAgent):
    output_content = []
    output_content.append(f"# Mind Mapping Brainstorming for: {user_query}\n")

    class InitialIdeaGenerator(Tool):
        name = "initial_idea_generator"
        description = "Generates 10 initial ideas from a query. Takes 'query' as input and returns bullet points."
        inputs = {"query": {"type": "string", "description": "The query to generate initial ideas for."}}
        output_type = "string"

        def forward(self, query: str) -> str:
            ideas_raw = agent.run(mm_initial_idea_prompt.format(query=query))
            if isinstance(ideas_raw, list):
                ideas_raw = "".join(ideas_raw)
            ideas = _parse_bullet_points(ideas_raw)
            return "\n".join(ideas)

    class IdeaExpander(Tool):
        name = "idea_expander"
        description = "Expands one idea into 5 related ideas. Takes 'idea' as input and returns bullet points."
        inputs = {"idea": {"type": "string", "description": "The idea to expand."}}
        output_type = "string"

        def forward(self, idea: str) -> str:
            expanded_ideas_raw = agent.run(mm_expand_idea_prompt.format(idea=idea))
            if isinstance(expanded_ideas_raw, list):
                expanded_ideas_raw = "".join(expanded_ideas_raw)
            expanded_ideas = _parse_bullet_points(expanded_ideas_raw)
            return "\n".join(expanded_ideas)

    initial_idea_tool = InitialIdeaGenerator()
    idea_expander_tool = IdeaExpander()

    # Generate 10 initial ideas
    initial_ideas_raw = initial_idea_tool.forward(user_query)
    initial_ideas = _parse_bullet_points(initial_ideas_raw)

    output_content.append("#### Initial Ideas:\n")
    output_content.append(initial_ideas_raw + "\n")

    # Expand each initial idea
    for i, idea in enumerate(initial_ideas):
        output_content.append(f"- **Idea {i+1}:** {idea}\n")
        
        expanded_ideas_raw = idea_expander_tool.forward(idea)
        expanded_ideas = _parse_bullet_points(expanded_ideas_raw)
        
        output_content.append(f"  - **Expanded Ideas:**\n")
        for expanded_idea in expanded_ideas:
            output_content.append(f"    - {expanded_idea}\n")
        
        output_content.append("\n")

    return "\n".join(output_content)



# Reverse brainstorming method
def rb(user_query, agent: CodeAgent):
    output_content = []
    output_content.append(f"# Reverse Brainstorming for: {user_query}\n")

    class ProblemIdentifier(Tool):
        name = "problem_identifier"
        description = "Identifies 5 potential issues or challenges for a given idea. Takes 'idea' as input and returns bullet points."
        inputs = {"idea": {"type": "string", "description": "The idea to analyze for problems."}}
        output_type = "string"

        def forward(self, idea: str) -> str:
            problems_raw = agent.run(reverse_brainstorming_prompt.format(idea=idea))
            if isinstance(problems_raw, list):
                problems_raw = "".join(problems_raw)
            problems = _parse_bullet_points(problems_raw)
            return "\n".join(problems)

    class InitialIdeaGenerator(Tool): # Reusing the InitialIdeaGenerator from bmm
        name = "initial_idea_generator"
        description = "Generates 10 initial ideas from a query. Takes 'query' as input and returns bullet points."
        inputs = {"query": {"type": "string", "description": "The query to generate initial ideas for."}}
        output_type = "string"

        def forward(self, query: str) -> str: # Changed return type to str
            ideas_raw = agent.run(mm_initial_idea_prompt.format(query=query))
            if isinstance(ideas_raw, list):
                ideas_raw = "".join(ideas_raw)
            ideas = _parse_bullet_points(ideas_raw)
            return "\n".join(ideas) # Return joined string

    problem_identifier_tool = ProblemIdentifier()
    initial_idea_tool = InitialIdeaGenerator()

    # Generate 10 initial ideas
    initial_ideas_raw = initial_idea_tool.forward(user_query)
    initial_ideas = _parse_bullet_points(initial_ideas_raw)

    output_content.append("#### Initial Ideas:\n")
    output_content.append(initial_ideas_raw + "\n")

    # Identify problems for each initial idea
    for i, idea in enumerate(initial_ideas):
        output_content.append(f"- **Idea {i+1}:** {idea}\n")
        
        problems_raw = problem_identifier_tool.forward(idea)
        problems = _parse_bullet_points(problems_raw)
        
        output_content.append(f"  - **Potential Problems:**\n")
        for problem in problems:
            output_content.append(f"    - {problem}\n")
        
        output_content.append("\n")

    return "\n".join(output_content)


# Role storming brainstorming method
def rs(user_query, agent: CodeAgent):
    output_content = []
    output_content.append(f"# Role Storming Brainstorming for: {user_query}\n")

    class RoleStormingGenerator(Tool):
        name = "role_storming_generator"
        description = "Generates 5 unique ideas using the Role Storming method with different personas. Takes 'idea' as input and returns bullet points."
        inputs = {"idea": {"type": "string", "description": "The idea to generate role storming perspectives for."}}
        output_type = "string"

        def forward(self, idea: str) -> str:
            role_ideas_raw = agent.run(role_storming_prompt.format(idea=idea))
            if isinstance(role_ideas_raw, list):
                role_ideas_raw = "".join(role_ideas_raw)
            role_ideas = _parse_bullet_points(role_ideas_raw)
            return "\n".join(role_ideas)

    class InitialIdeaGenerator(Tool):
        name = "initial_idea_generator"
        description = "Generates 10 initial ideas from a query. Takes 'query' as input and returns bullet points."
        inputs = {"query": {"type": "string", "description": "The query to generate initial ideas for."}}
        output_type = "string"

        def forward(self, query: str) -> str:
            ideas_raw = agent.run(mm_initial_idea_prompt.format(query=query))
            if isinstance(ideas_raw, list):
                ideas_raw = "".join(ideas_raw)
            ideas = _parse_bullet_points(ideas_raw)
            return "\n".join(ideas)

    role_storming_tool = RoleStormingGenerator()
    initial_idea_tool = InitialIdeaGenerator()

    # Generate 10 initial ideas
    initial_ideas_raw = initial_idea_tool.forward(user_query)
    initial_ideas = _parse_bullet_points(initial_ideas_raw)

    output_content.append("#### Initial Ideas:\n")
    output_content.append(initial_ideas_raw + "\n")

    # Generate role storming perspectives for each initial idea
    for i, idea in enumerate(initial_ideas):
        output_content.append(f"- **Idea {i+1}:** {idea}\n")
        
        role_ideas_raw = role_storming_tool.forward(idea)
        role_ideas = _parse_bullet_points(role_ideas_raw)
        
        output_content.append(f"  - **Role Storming Perspectives:**\n")
        for role_idea in role_ideas:
            output_content.append(f"    - {role_idea}\n")
        
        output_content.append("\n")

    return "\n".join(output_content)


# SCAMPER brainstorming method
def sc(user_query, agent: CodeAgent):
    output_content = []
    output_content.append(f"# SCAMPER Brainstorming for: {user_query}\n")

    class ScamperIdeasGenerator(Tool):
        name = "scamper_ideas_generator"
        description = "Generates 7 ideas using the SCAMPER method (Substitute, Combine, Adjust, Modify, Put to other uses, Eliminate, Reverse). Takes 'idea' as input and returns bullet points."
        inputs = {"idea": {"type": "string", "description": "The idea to generate SCAMPER variations for."}}
        output_type = "string"

        def forward(self, idea: str) -> str:
            scamper_ideas_raw = agent.run(scamper_ideas_prompt.format(idea=idea))
            if isinstance(scamper_ideas_raw, list):
                scamper_ideas_raw = "".join(scamper_ideas_raw)
            scamper_ideas = _parse_bullet_points(scamper_ideas_raw)
            return "\n".join(scamper_ideas)

    class InitialIdeaGenerator(Tool):
        name = "initial_idea_generator"
        description = "Generates 10 initial ideas from a query. Takes 'query' as input and returns bullet points."
        inputs = {"query": {"type": "string", "description": "The query to generate initial ideas for."}}
        output_type = "string"

        def forward(self, query: str) -> str:
            ideas_raw = agent.run(mm_initial_idea_prompt.format(query=query))
            if isinstance(ideas_raw, list):
                ideas_raw = "".join(ideas_raw)
            ideas = _parse_bullet_points(ideas_raw)
            return "\n".join(ideas)

    scamper_tool = ScamperIdeasGenerator()
    initial_idea_tool = InitialIdeaGenerator()

    # Generate 10 initial ideas
    initial_ideas_raw = initial_idea_tool.forward(user_query)
    initial_ideas = _parse_bullet_points(initial_ideas_raw)

    output_content.append("#### Initial Ideas:\n")
    output_content.append(initial_ideas_raw + "\n")

    # Generate SCAMPER ideas for each initial idea
    for i, idea in enumerate(initial_ideas):
        output_content.append(f"- **Idea {i+1}:** {idea}\n")
        
        scamper_ideas_raw = scamper_tool.forward(idea)
        scamper_ideas = _parse_bullet_points(scamper_ideas_raw)
        
        output_content.append(f"  - **SCAMPER Variations:**\n")
        for scamper_idea in scamper_ideas:
            output_content.append(f"    - {scamper_idea}\n")
        
        output_content.append("\n")

    return "\n".join(output_content)


# Six Thinking Hats brainstorming method
def sh(user_query, agent: CodeAgent):
    output_content = []
    output_content.append(f"# Six Thinking Hats Brainstorming for: {user_query}\n")

    class SixHatsGenerator(Tool):
        name = "six_hats_generator"
        description = "Generates 6 perspectives using the Six Thinking Hats method (White, Red, Black, Yellow, Green, Blue). Takes 'idea' as input and returns bullet points."
        inputs = {"idea": {"type": "string", "description": "The idea to analyze with Six Thinking Hats."}}
        output_type = "string"

        def forward(self, idea: str) -> str:
            six_hats_raw = agent.run(six_hats_ideas_prompt.format(idea=idea))
            if isinstance(six_hats_raw, list):
                six_hats_raw = "".join(six_hats_raw)
            six_hats = _parse_bullet_points(six_hats_raw)
            return "\n".join(six_hats)

    class InitialIdeaGenerator(Tool):
        name = "initial_idea_generator"
        description = "Generates 10 initial ideas from a query. Takes 'query' as input and returns bullet points."
        inputs = {"query": {"type": "string", "description": "The query to generate initial ideas for."}}
        output_type = "string"

        def forward(self, query: str) -> str:
            ideas_raw = agent.run(mm_initial_idea_prompt.format(query=query))
            if isinstance(ideas_raw, list):
                ideas_raw = "".join(ideas_raw)
            ideas = _parse_bullet_points(ideas_raw)
            return "\n".join(ideas)

    six_hats_tool = SixHatsGenerator()
    initial_idea_tool = InitialIdeaGenerator()

    # Generate 10 initial ideas
    initial_ideas_raw = initial_idea_tool.forward(user_query)
    initial_ideas = _parse_bullet_points(initial_ideas_raw)

    output_content.append("#### Initial Ideas:\n")
    output_content.append(initial_ideas_raw + "\n")

    # Generate Six Thinking Hats perspectives for each initial idea
    for i, idea in enumerate(initial_ideas):
        output_content.append(f"- **Idea {i+1}:** {idea}\n")
        
        six_hats_raw = six_hats_tool.forward(idea)
        six_hats = _parse_bullet_points(six_hats_raw)
        
        output_content.append(f"  - **Six Thinking Hats Perspectives:**\n")
        for perspective in six_hats:
            output_content.append(f"    - {perspective}\n")
        
        output_content.append("\n")

    return "\n".join(output_content)