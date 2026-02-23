MAX_MEMORY_MESSAGES = 10  # Keep last 10 messages


def initialize_memory():
    return []


def add_message(memory, role, content):
    memory.append({
        "role": role,
        "content": content
    })

    # Trim memory if too long
    if len(memory) > MAX_MEMORY_MESSAGES:
        memory = memory[-MAX_MEMORY_MESSAGES:]

    return memory


def format_conversation(memory):
    formatted = ""
    for msg in memory:
        formatted += f"{msg['role'].capitalize()}: {msg['content']}\n"
    return formatted