import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    for i in range(1, 6):
        # Задержка обратно пропорциональная силе
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    # Создаем три задачи для участников
    tasks = [
        start_strongman('Pasha', 3),
        start_strongman('Denis', 4),
        start_strongman('Apollon', 5)
    ]

    # Ожидаем выполнения всех задач
    await asyncio.gather(*tasks)


# Запускаем асинхронную функцию
if __name__ == "__main__":
    asyncio.run(start_tournament())