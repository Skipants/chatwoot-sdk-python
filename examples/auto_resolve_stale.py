"""Auto-resolve stale conversations.

Lists open conversations, skips any with urgent or high priority,
resolves the rest if they've been idle past a threshold, and posts
a closing message.
"""

import time

from chatwoot import ChatwootClient
from chatwoot.types.common import ConversationPriority
from chatwoot.types.conversation import Conversation

BASE_URL = "http://localhost:3000"
API_TOKEN = "your-api-token"
ACCOUNT_ID = 1

STALE_THRESHOLD_HOURS = 48
CLOSING_MESSAGE = (
    "This conversation has been automatically resolved due to inactivity. "
    "Feel free to reopen it if you need further assistance!"
)


def is_stale(conversation: Conversation) -> bool:
    """Check if a conversation has been idle past the threshold."""
    last_activity = conversation.timestamp or conversation.created_at
    if last_activity is None:
        return False
    age_hours = (time.time() - last_activity) / 3600
    return age_hours > STALE_THRESHOLD_HOURS


def main() -> None:
    with ChatwootClient(base_url=BASE_URL, api_token=API_TOKEN) as client:
        page = 1
        resolved_count = 0
        skipped_priority = 0

        while True:
            conversations = client.conversations.list(
                ACCOUNT_ID, status="open", page=page
            )
            if not conversations:
                break

            for convo in conversations:
                # Skip high-priority conversations
                if convo.priority in (ConversationPriority.URGENT, ConversationPriority.HIGH):
                    skipped_priority += 1
                    print(
                        f"  Skipping conversation {convo.id} "
                        f"(priority={convo.priority})"
                    )
                    continue

                if not is_stale(convo):
                    continue

                # Send a closing message before resolving
                client.messages.create(
                    ACCOUNT_ID,
                    conversation_id=convo.id,
                    content=CLOSING_MESSAGE,
                    message_type="outgoing",
                )
                client.conversations.toggle_status(
                    ACCOUNT_ID, convo.id, status="resolved"
                )
                resolved_count += 1
                print(f"  Resolved conversation {convo.id}")

            page += 1

        print(
            f"\nDone. Resolved {resolved_count} conversations, "
            f"skipped {skipped_priority} high-priority."
        )


if __name__ == "__main__":
    main()
