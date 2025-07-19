# Simple in-memory queue
queue = {}

def add_to_queue(chat_id, song):
    if chat_id in queue:
        queue[chat_id].append(song)
    else:
        queue[chat_id] = [song]

def get_queue(chat_id):
    return queue.get(chat_id, [])

def pop_next(chat_id):
    if chat_id in queue and len(queue[chat_id]) > 0:
        return queue[chat_id].pop(0)
    return None

def clear_queue(chat_id):
    queue.pop(chat_id, None)
