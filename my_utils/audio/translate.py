import language_constants
import openai, os

openai.api_key = os.getenv("api_key")


def translate(to_langs=[], prompt):
	lang_list = [": ".join([str(lang), str(idx)]) for lang, idx in enumerate(to_langs)]

	response = openai.Completion.create(
	  model="text-davinci-003",
	  prompt="Translate this into 1. French, 2. Spanish and 3. Japanese:\n\n{prompt}\n\n",
	  temperature=0.3,
	  max_tokens=1000,
	  top_p=1.0,
	  frequency_penalty=0.0,
	  presence_penalty=0.0
)