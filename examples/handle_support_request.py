"""Handle an inbound support request end-to-end.

Creates a contact, starts a conversation, sends a welcome message,
and assigns it to an agent.
"""

import sys

from chatwoot import ChatwootClient

BASE_URL = "http://localhost:3000"
API_TOKEN = "your-api-token"
ACCOUNT_ID = 1


def main() -> None:
    with ChatwootClient(base_url=BASE_URL, api_token=API_TOKEN) as client:
        # 1. Pick an inbox (use the first API-type inbox, or any available one)
        inboxes = client.inboxes.list(ACCOUNT_ID)
        if not inboxes:
            print("No inboxes found. Create one in the Chatwoot dashboard first.")
            sys.exit(1)
        inbox = inboxes[0]
        print(f"Using inbox: {inbox.name} (id={inbox.id})")

        # 2. Create a contact
        result = client.contacts.create(
            ACCOUNT_ID,
            inbox_id=inbox.id,
            name="Jane Doe",
            email="jane.doe@example.com",
            phone_number="+1234567890",
        )
        contact = result.contact
        source_id = result.contact_inbox.source_id
        print(f"Created contact: {contact.name} (id={contact.id})")

        # 3. Start a conversation
        conversation = client.conversations.create(
            ACCOUNT_ID,
            source_id=source_id,
            inbox_id=inbox.id,
            contact_id=contact.id,
        )
        print(f"Created conversation: id={conversation.id}")

        # 4. Send a welcome message
        message = client.messages.create(
            ACCOUNT_ID,
            conversation_id=conversation.id,
            content="Hi Jane! Thanks for reaching out. How can we help you today?",
            message_type="outgoing",
        )
        print(f"Sent message: id={message.id}")

        # 5. Assign to an agent
        agents = client.agents.list(ACCOUNT_ID)
        if agents:
            agent = agents[0]
            client.conversations.assign(
                ACCOUNT_ID,
                conversation_id=conversation.id,
                assignee_id=agent.id,
            )
            print(f"Assigned to agent: {agent.name}")

        # 6. Add a label
        client.conversations.labels.add(
            ACCOUNT_ID, conversation.id, labels=["new-request"]
        )
        print("Added label: new-request")


if __name__ == "__main__":
    main()
