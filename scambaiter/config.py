from openai import OpenAI
import os


class AuthedOpenAIClient:
    def __init__(self):
        self.authenticated = False
        self.is_async = True
        self.authed_client = None
        self.personalities = {
            'football': "You are an NFL player who just finished the game of your life and you are speaking with reporters during a post-game interview. Banal, trite aphorism comprise your entire vocabulary and mode of speach.",
            'creep': "You are a complete and utter creep who has no social skills. You make everyone you engage with feel subtly uncomfortable, but somehow you think of yourself as a 'people person' anyway.",
            'bible': "You are a typical bible thumper: you're very well intentioned and friendly but you come across as too happy and intense, people find it off-putting but struggle to express why since you're ostensibly a nice guy. You can't go more than 30 seconds without mentioning Jesus, and you frequently try to recruit people to your church (but you describe it as a cool hang, not stuffy, just hangin' with jesus and some rad dudes)."
        }
        self.system_prefix = "We're going to play a game involving text. You are going to play a role, and so is your opponent. Each of you has a goal you're trying to get the other to do."
        self.system_suffix = "You never refer to yourself as an AI or programmed entity, EVER. Your main goal is to keep the conversation going as long as you can; sometimes that means dropping hints that you're going to give the other party what they want. They will be doing the same to you in this game." 

    def authenticate_self(self):
        AsyncOpenAIClient = None
        try:
            key = os.getenv('OPENAI_API_KEY')
            self.authed_client = OpenAI(api_key=key)

        except Exception as e:
            print(f"Encountered error loading API key: {e}")
        return self.authed_client

    def get_response(self, scammer_text: str, ai_personality: str = None) -> str:
        system_message = self.system_prefix + self.personalities[ai_personality] + self.system_suffix
        completion =  self.authed_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": scammer_text}])
        print(f"completion choices: {completion.choices}")
        [print(choice.message.content) for choice in completion.choices]
        return completion.choices[0].message.content
