class GPTWrapper:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openai.com/v1/engines/davinci-codex/completions"

    def _make_request(self, prompt: str, max_tokens: int = 100):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": prompt,
            "max_tokens": max_tokens
        }
        response = requests.post(self.base_url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def generate_text(self, prompt: str, max_tokens: int = 100):
        response = self._make_request(prompt, max_tokens)
        return response['choices'][0]['text']

# Example usage:
# wrapper = GPTWrapper(api_key="your_api_key_here")
# result = wrapper.generate_text("Write a poem about the sea.")
# print(result)