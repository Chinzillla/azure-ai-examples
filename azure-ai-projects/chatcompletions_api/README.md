## Chat Completions API examples

These examples use the Azure AI Projects OpenAI client with the Chat Completions API.

Set up a local environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Create a `.env` file from `.env.example` and set:

```text
AZURE_AI_PROJECT_ENDPOINT=
AZURE_OPENAI_DEPLOYMENT=
AZURE_OPENAI_CHAT_DEPLOYMENT=
```

`AZURE_OPENAI_CHAT_DEPLOYMENT` is optional. If it is not set, the examples use `AZURE_OPENAI_DEPLOYMENT`.

Run an example:

```powershell
python .\1_2turn.py
python .\2_looped.py
python .\3_manual_history.py
python .\4_streaming_resp.py
python .\5_async_streaming_resp.py
```

Files:

- `1_2turn.py`: makes two Chat Completions requests.
- `2_looped.py`: keeps conversational context in a loop.
- `3_manual_history.py`: shows explicit manual history tracking.
- `4_streaming_resp.py`: streams a sync Chat Completions response.
- `5_async_streaming_resp.py`: streams an async Chat Completions response.
