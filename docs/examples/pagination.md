# Pagination

Two resources support pagination via a `page` parameter — `conversations.list` and `contacts.list`. Both return an empty list when the page is beyond the last one, which is the natural loop terminator.

## Fetch all open conversations

```python
from chatwoot import ChatwootClient

client = ChatwootClient(base_url="...", api_token="...")

all_conversations = []
page = 1

while True:
    batch = client.conversations.list(account_id=1, status="open", page=page)
    if not batch:
        break
    all_conversations.extend(batch)
    page += 1

print(f"Total: {len(all_conversations)} conversations")
```

## Fetch all contacts

```python
all_contacts = []
page = 1

while True:
    batch = client.contacts.list(account_id=1, page=page)
    if not batch:
        break
    all_contacts.extend(batch)
    page += 1
```

## Async variant

```python
import asyncio
from chatwoot import AsyncChatwootClient

async def fetch_all_conversations(account_id: int) -> list:
    async with AsyncChatwootClient(base_url="...", api_token="...") as client:
        results = []
        page = 1
        while True:
            batch = await client.conversations.list(
                account_id=account_id, status="open", page=page
            )
            if not batch:
                break
            results.extend(batch)
            page += 1
        return results

conversations = asyncio.run(fetch_all_conversations(account_id=1))
```

## Process page-by-page without loading everything

If the full dataset is large, process each page immediately rather than collecting all results first:

```python
page = 1

while True:
    batch = client.conversations.list(account_id=1, status="open", page=page)
    if not batch:
        break
    for conversation in batch:
        process(conversation)  # handle one at a time
    page += 1
```
