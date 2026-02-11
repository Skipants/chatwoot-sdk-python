"""Async usage example for the Chatwoot SDK."""

import asyncio

from chatwoot import AsyncChatwootClient


async def main():
    """Main async function demonstrating async SDK usage."""
    # Initialize the async client
    async with AsyncChatwootClient(
        base_url="https://app.chatwoot.com",
        api_token="your_api_token_here",
    ) as client:
        # Fetch profile
        profile = await client.profile.get()
        print(f"Logged in as: {profile.name} ({profile.email})")

        account_id = profile.account_id

        # Fetch multiple resources concurrently
        inboxes_task = client.inboxes.list(account_id=account_id)
        conversations_task = client.conversations.list(
            account_id=account_id,
            status="open",
        )
        contacts_task = client.contacts.list(account_id=account_id)
        agents_task = client.agents.list(account_id=account_id)

        # Wait for all tasks to complete
        inboxes, conversations, contacts, agents = await asyncio.gather(
            inboxes_task,
            conversations_task,
            contacts_task,
            agents_task,
        )

        print("\nFetched resources:")
        print(f"  Inboxes: {len(inboxes)}")
        print(f"  Open conversations: {len(conversations)}")
        print(f"  Contacts: {len(contacts)}")
        print(f"  Agents: {len(agents)}")

        # Process a conversation if available
        if conversations:
            conversation = conversations[0]
            print(f"\nProcessing conversation #{conversation.display_id}")

            # Fetch messages
            messages = await client.messages.list(
                account_id=account_id,
                conversation_id=conversation.id,
            )
            print(f"  Messages: {len(messages)}")

            # Get conversation labels
            labels = await client.conversations.labels.list(
                account_id=account_id,
                conversation_id=conversation.id,
            )
            print(f"  Labels: {labels}")

        print("\nDone!")


if __name__ == "__main__":
    asyncio.run(main())
