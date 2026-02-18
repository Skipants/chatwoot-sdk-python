# Chatwoot Python SDK

A modern, type-safe Python SDK for the [Chatwoot](https://www.chatwoot.com/) API. Provides both synchronous and asynchronous clients with full type hints and Pydantic models.

## Features

- **Type-safe** — Full type hints and Pydantic v2 models for all responses
- **Async support** — Both sync (`ChatwootClient`) and async (`AsyncChatwootClient`) clients
- **Comprehensive** — Covers all major Chatwoot API resources
- **Error handling** — Typed exceptions for every HTTP error class

## Installation

```bash
pip install chatwoot-sdk
# or
uv add chatwoot-sdk
```

## Quick Start

```python
from chatwoot import ChatwootClient

client = ChatwootClient(
    base_url="https://app.chatwoot.com",
    api_token="your_api_token_here"
)

profile = client.profile.get()
print(f"Logged in as: {profile.name}")

conversations = client.conversations.list(account_id=1, status="open")

client.close()
```

### Context manager

```python
with ChatwootClient(base_url="...", api_token="...") as client:
    profile = client.profile.get()
```

### Async client

```python
import asyncio
from chatwoot import AsyncChatwootClient

async def main():
    async with AsyncChatwootClient(base_url="...", api_token="...") as client:
        profile = await client.profile.get()
        conversations = await client.conversations.list(account_id=1, status="open")

asyncio.run(main())
```

## Error Handling

```python
from chatwoot import (
    ChatwootClient,
    ChatwootAuthError,
    ChatwootNotFoundError,
    ChatwootValidationError,
)

try:
    conversation = client.conversations.get(account_id=1, conversation_id=999)
except ChatwootAuthError:
    print("Bad token")
except ChatwootNotFoundError:
    print("Conversation not found")
except ChatwootValidationError as e:
    for err in e.errors or []:
        print(f"  {err['field']}: {err['message']}")
```

## API Resources

| Resource | Description |
|---|---|
| `client.profile` | Current user profile |
| `client.conversations` | Conversation management |
| `client.messages` | Send and manage messages |
| `client.contacts` | Contact management |
| `client.inboxes` | Inbox configuration |
| `client.teams` | Team management |
| `client.agents` | Agent management |
