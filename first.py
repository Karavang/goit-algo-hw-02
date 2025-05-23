from queue import Queue

queue = Queue()

def generate_request():
    data = "Заявка"
    queue.add(data)


def process_request():
    if not queue.is_empty():
        data = queue.get()
        queue.remove(data)
        # Обробити заявку, я не дуже зрозумів, що потрібно робити
        print(f"Обробка заявки: {data}")
    else:
        print("Черга порожня, немає заявок для обробки.")


def main():
    queue.initialize()
    while True:
        generate_request()
        process_request()
