"""Basic usage example for the Chatwoot SDK."""

from chatwoot import ChatwootClient

# Use as a context manager for automatic cleanup
with ChatwootClient(
    base_url="https://app.chatwoot.com", api_token="your_api_token_here"
) as client:
    # Fetch your profile
    profile = client.profile.get()
    print(f"Logged in as: {profile.name} ({profile.email})")
    print(f"Role: {profile.role}")

    # Get your account ID from the profile
    account_id = profile.account_id

    # List all inboxes
    inboxes = client.inboxes.list(account_id=account_id)
    print(f"\nInboxes ({len(inboxes)}):")
    for inbox in inboxes:
        print(f"  - {inbox.name} ({inbox.channel_type})")

    # List open conversations
    conversations = client.conversations.list(
        account_id=account_id,
        status="open",
        assignee_type="all",
        page=1,
    )
    print(f"\nOpen conversations: {len(conversations)}")

    # Get details of the first conversation
    if conversations:
        conversation = conversations[0]
        print(f"\nConversation #{conversation.display_id}:")
        print(f"  Status: {conversation.status}")
        print(f"  Unread count: {conversation.unread_count}")
        print(f"  Labels: {conversation.labels}")

        # List messages in the conversation
        messages = client.messages.list(
            account_id=account_id,
            conversation_id=conversation.id,
        )
        print(f"  Messages: {len(messages)}")

        # Send a message (uncomment to test)
        # message = client.messages.create(
        #     account_id=account_id,
        #     conversation_id=conversation.id,
        #     content="Hello from the Python SDK!",
        #     message_type="outgoing",
        # )
        # print(f"  Sent message: {message.id}")

    # List contacts
    contacts = client.contacts.list(account_id=account_id, page=1)
    print(f"\nContacts: {len(contacts)}")
    if contacts:
        contact = contacts[0]
        print(f"  First contact: {contact.name} ({contact.email})")

    # List agents
    agents = client.agents.list(account_id=account_id)
    print(f"\nAgents: {len(agents)}")
    for agent in agents:
        print(f"  - {agent.name} ({agent.role})")

    # List teams
    teams = client.teams.list(account_id=account_id)
    print(f"\nTeams: {len(teams)}")
    for team in teams:
        print(f"  - {team.name}")

print("\nDone!")
