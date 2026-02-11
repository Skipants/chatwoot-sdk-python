"""Conversation workflow example for the Chatwoot SDK."""

from chatwoot import ChatwootClient

# Initialize client
client = ChatwootClient(
    base_url="https://app.chatwoot.com",
    api_token="your_api_token_here",
)

# Get profile to retrieve account ID
profile = client.profile.get()
account_id = profile.account_id
print(f"Working with account: {account_id}")

# List open conversations assigned to me
print("\n=== My Open Conversations ===")
conversations = client.conversations.list(
    account_id=account_id,
    status="open",
    assignee_type="me",
    page=1,
)
print(f"Found {len(conversations)} conversations")

for conv in conversations:
    print(f"\nConversation #{conv.display_id}:")
    print(f"  Status: {conv.status}")
    print(f"  Unread: {conv.unread_count}")
    print(f"  Labels: {', '.join(conv.labels) if conv.labels else 'None'}")

    # Get messages
    messages = client.messages.list(
        account_id=account_id,
        conversation_id=conv.id,
    )
    print(f"  Messages: {len(messages)}")

    if messages:
        last_message = messages[-1]
        print(f"  Last message: {last_message.content[:50]}...")

# Search for conversations with specific labels
print("\n=== Conversations with 'urgent' label ===")
urgent_conversations = client.conversations.list(
    account_id=account_id,
    status="open",
    labels=["urgent"],
)
print(f"Found {len(urgent_conversations)} urgent conversations")

# Create a new conversation (example)
print("\n=== Creating New Conversation ===")
# First, get an inbox to use
inboxes = client.inboxes.list(account_id=account_id)
if inboxes:
    inbox_id = inboxes[0].id

    # Create or get a contact
    contacts = client.contacts.list(account_id=account_id, page=1)
    if contacts:
        contact_id = contacts[0].id

        # Create conversation (uncomment to test)
        # new_conversation = client.conversations.create(
        #     account_id=account_id,
        #     source_id=f"sdk-test-{int(time.time())}",
        #     inbox_id=inbox_id,
        #     contact_id=contact_id,
        # )
        # print(f"Created conversation: {new_conversation.id}")
        #
        # # Send a message
        # message = client.messages.create(
        #     account_id=account_id,
        #     conversation_id=new_conversation.id,
        #     content="Hello! This is a test message from the SDK.",
        #     message_type="outgoing",
        # )
        # print(f"Sent message: {message.id}")
        #
        # # Add labels to conversation
        # labels = client.conversations.labels.add(
        #     account_id=account_id,
        #     conversation_id=new_conversation.id,
        #     labels=["sdk-test", "automated"],
        # )
        # print(f"Added labels: {labels}")
        #
        # # Assign to yourself
        # updated_conversation = client.conversations.assign(
        #     account_id=account_id,
        #     conversation_id=new_conversation.id,
        #     assignee_id=profile.id,
        # )
        # print(f"Assigned to: {profile.name}")
        #
        # # Resolve the conversation
        # resolved_conversation = client.conversations.toggle_status(
        #     account_id=account_id,
        #     conversation_id=new_conversation.id,
        #     status="resolved",
        # )
        # print(f"Status: {resolved_conversation.status}")

        print("(Commented out - uncomment to test creation)")

# Get conversation counts
print("\n=== Conversation Counts ===")
counts = client.conversations.get_counts(account_id=account_id, status="open")
print(f"Open conversations: {counts}")

# Clean up
client.close()
print("\nDone!")
