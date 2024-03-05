# Symposium
Interaction with multiple language models.
## Anthropic
## OpenAI
#### Completion
```python
kwargs = {
    "model":                "gpt-3.5-turbo-instructions",
    "prompt":               str,
    "suffix":               str,
    "max_tokens_to_sample": 5,
    "n":                    1,
    "best_of":              None,
    "stop_sequences":       ["stop"],
    "seed":                 None,
    "frequency_penalty":    None,
    "presence_penalty":     None,
    "logit_bias":           None,
    "logprobs":             None,
    "top_logprobs":         None,
    "temperature":          0.5,
    "top_p":                0.5,
    "user":                 None
}
gpt_complete(prompt, **kwargs)
```
